#
# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import platform
import os
import re
from sys import exit

import click
from tabulate import tabulate

from util.logger import initialize_logger
from util.cli_state import common_options, verify_user_privileges
from util.config import TBLT_TABLE_FORMAT
from util.k8s.k8s_info import get_current_user, get_users_samba_password, is_current_user_administrator, \
    get_kubectl_host
from util.aliascmd import AliasGroup, AliasCmd
from util.system import handle_error, execute_system_command
from cli_text_consts import MountCmdTexts as Texts


logger = initialize_logger(__name__)

NAUTA_IDENTITY_STRING = "domain=NAUTA"


class ShareData():
    LINUX_MOUNTS_LIST_HEADERS = ["Username", "Remote location", "Local folder"]
    WIN_MOUNTS_LIST_HEADERS = ["Status", "Local folder", "Remote location", "Network"]

    def __init__(self, remote_share: str = None, local_share: str = None, username: str = None,
                 status: str = None, network: str = None):
        self.remote_share = remote_share
        self.local_share = local_share
        self.username = username
        self.status = status
        self.network = network

    def linux_osx_tabular_format(self):
        return [self.username, self.remote_share, self.local_share]

    def windows_tabular_format(self):
        return [self.status, self.local_share, self.remote_share, self.network]


def is_admin():
    try:
        return is_current_user_administrator()
    except Exception:
        handle_error(logger, Texts.ADMIN_CHECK_ERROR_MSG, Texts.ADMIN_CHECK_ERROR_MSG,
                     add_verbosity_msg=click.get_current_context().obj.verbosity == 0)
        exit(1)


def print_unmount():
    click.echo()
    unmount_command = get_unmount_command()
    click.echo(Texts.UNMOUNT_CMD.format(command=unmount_command))

    if platform.system() == "Linux":
        click.echo(Texts.UNMOUNT_OPTIONS_MSG)
        click.echo(Texts.UNMOUNT_MSG_UNIX)
    elif platform.system() == "Darwin":
        click.echo(Texts.UNMOUNT_OPTIONS_OSX_MSG)
        click.echo(Texts.UNMOUNT_MSG_UNIX)
    elif platform.system() == 'Windows':
        click.echo(Texts.UNMOUNT_MSG_WIN)


@click.group(short_help=Texts.HELP, help=Texts.HELP, cls=AliasGroup, alias='m', invoke_without_command=True,
             subcommand_metavar='command [options]')
@common_options()
@click.pass_context
def mount(ctx: click.Context):
    if ctx.invoked_subcommand is None:
        verify_user_privileges(False, "mount")

        try:
            mount_command = get_mount_command()
            click.echo(Texts.MOUNT_CMD.format(command=mount_command))
        except Exception:
            handle_error(logger, Texts.GET_MOUNT_COMMAND_ERROR_MSG, Texts.GET_MOUNT_COMMAND_ERROR_MSG,
                         add_verbosity_msg=ctx.obj.verbosity == 0)
            exit(1)

        click.echo(Texts.MAIN_MSG)

        print_unmount()


def get_unmount_command() -> str:
    if platform.system() == 'Linux':
        return get_unmount_command_linux()
    elif platform.system() == 'Windows':
        return get_unmount_command_windows()
    else:  # OSX
        return get_unmount_command_osx()


def get_mount_command() -> str:
    adr = get_kubectl_host(with_port=False)
    usr = get_current_user()
    psw = get_users_samba_password(usr)

    if platform.system() == 'Linux':
        return get_mount_command_linux(usr, psw, adr)
    elif platform.system() == 'Windows':
        return get_mount_command_windows(usr, psw, adr)
    else:  # OSX
        return get_mount_command_osx(usr, psw, adr)


def get_mount_command_linux(usr: str, psw: str, adr: str) -> str:
    usr_id = str(os.getuid())
    return f"sudo mount.cifs -o username={usr},password={psw},rw,uid={usr_id} //{adr}/<NAUTA_FOLDER> <MOUNTPOINT>"


def get_unmount_command_linux() -> str:
    return f"sudo umount <MOUNTPOINT> [-fl]"


def get_mount_command_windows(usr: str, psw: str, adr: str) -> str:
    return f"net use <MOUNTPOINT> \\\\{adr}\\<NAUTA_FOLDER> /user:{usr} {psw}"


def get_unmount_command_windows() -> str:
    return f"net use <MOUNTPOINT> /d"


def get_mount_command_osx(usr: str, psw: str, adr: str) -> str:
    return f"mount_smbfs //'{usr}:{psw}'@{adr}/<NAUTA_FOLDER> <MOUNTPOINT>"


def get_unmount_command_osx() -> str:
    return f"umount <MOUNTPOINT> [-f]"


def get_mounts_linux_osx(username: str = "", is_admin: bool = False, osx: bool = False):
    output, error_code, log_output = execute_system_command(["mount"])

    if error_code:
        handle_error(logger, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG)
        exit(1)
    host = get_kubectl_host(with_port=False)
    if osx:
        username_string = f"//{username}@"
    else:
        username_string = f"username={username},"

    if osx:
        mnt_regex = "//(.*)@(.*) on (.*) \("
    else:
        mnt_regex = "(.*) on (.*) type"

    ret_list = []

    if output:
        for item in [nauta_item for nauta_item in output.split("\n") if
                     host in nauta_item and (is_admin or username_string in nauta_item)]:
            try:
                mount_data = re.search(mnt_regex, item)
                if osx:
                    # Type checking is disabled here - we are catching AttributeError exception anyway
                    username = mount_data.group(1)  # type: ignore
                    remote_location = mount_data.group(2)  # type: ignore
                    local_folder = mount_data.group(3)  # type: ignore
                else:
                    remote_location = mount_data.group(1)  # type: ignore
                    local_folder = mount_data.group(2)  # type: ignore
                    username = re.search("username=(.*?),", item).group(1)  # type: ignore

                ret_list.append(ShareData(remote_share=remote_location, local_share=local_folder, username=username))
            except Exception:
                handle_error(logger, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG)

    ret_list.sort(key=lambda x: x.username, reverse=False)

    click.echo(tabulate([x.linux_osx_tabular_format() for x in ret_list], headers=ShareData.LINUX_MOUNTS_LIST_HEADERS,
                        tablefmt=TBLT_TABLE_FORMAT))


def get_mounts_windows():
    output, error_code, log_output = execute_system_command(["net", "use"])

    if error_code:
        handle_error(logger, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG, Texts.MOUNTS_LIST_COMMAND_ERROR_MSG)
        exit(1)
    host = get_kubectl_host(with_port=False)
    data = output.split("\n")

    start_analyzing = False
    ret_list = []
    first_line = None
    second_line = None

    for item in data:
        if start_analyzing:
            if "The command completed successfully." in item:
                break
            else:
                if not first_line:
                    first_line = item
                elif not second_line:
                    second_line = item

                if first_line and second_line:
                    if host in first_line:
                        split_first_line = first_line.split()
                        status = None
                        remote_location = None
                        if len(split_first_line) == 3:
                            status = split_first_line[0].strip()
                            local_folder = split_first_line[1].strip()
                            remote_location = split_first_line[2].strip()
                        elif len(split_first_line) == 2:
                            status = split_first_line[0].strip()
                            local_folder = ""
                            remote_location = split_first_line[1].strip()
                        network = second_line.strip()
                        if status and remote_location:
                            ret_list.append(ShareData(remote_share=remote_location, local_share=local_folder,
                                                      status=status, network=network))
                    first_line = None
                    second_line = None
        elif "--------" in item:
            start_analyzing = True

    ret_list.sort(key=lambda x: x.remote_share, reverse=False)

    click.echo(tabulate([x.windows_tabular_format() for x in ret_list], headers=ShareData.WIN_MOUNTS_LIST_HEADERS,
                        tablefmt=TBLT_TABLE_FORMAT))


@mount.command(help=Texts.HELP_L, short_help=Texts.HELP_L, cls=AliasCmd, alias='ls', options_metavar='[options]')
@common_options()
@click.pass_context
def list(ctx: click.Context):
    username = get_current_user()

    if platform.system() == 'Linux':
        get_mounts_linux_osx(username=username, is_admin=is_admin())
    elif platform.system() == 'Windows':
        get_mounts_windows()
    else:  # OSX
        get_mounts_linux_osx(username=username, is_admin=is_admin(), osx=True)

    print_unmount()
