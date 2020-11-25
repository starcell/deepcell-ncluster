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

from collections import namedtuple
from distutils.version import LooseVersion
import re
import os
from typing import Optional, Dict, Tuple

import yaml

from util.system import execute_system_command, get_os_version
from util.logger import initialize_logger
from util.exceptions import InvalidDependencyError, InvalidOsError
from cli_text_consts import UtilDependenciesCheckerTexts as Texts
from version import VERSION
from util.config import Config

log = initialize_logger(__name__)

UBUNTU_MIN_VERSION = LooseVersion('16')
WINDOWS_MIN_VERSION = LooseVersion('10')
MACOS_MIN_VERSION = LooseVersion('10.13')
REDHAT_MIN_VERSION = LooseVersion('7.5')

DRAFT_MIN_VERSION = LooseVersion('v0.13.0')
KUBECTL_MIN_VERSION = LooseVersion('v1.10')
KUBECTL_SERVER_MIN_VERSION = LooseVersion('v1.10')
HELM_VERSION = LooseVersion('v2.11.0')
GIT_VERSION = LooseVersion('1.8.3.1')

HELM_SERVER_CONNECTION_TIMEOUT = 30
NAMESPACE_PLACEHOLDER = '<namespace>'

DEPENDENCY_VERSIONS_FILE_SUFFIX = '-dependency-versions.yaml'
"""
namedtuple for holding binary dependency specification.
expected_version: expected dependency version
version_command: function that will be executed to obtain version info
version_command_args: arguments that will be passed to called version_command
version_field: name of field from which version will be parsed (e.g. GitVersion)
match_exact_version: if True, only versions that exactly match expected version should be accepted,
                     if False all versions that are greater or equal to the expected version should be accepted
"""
DependencySpec = namedtuple('DependencySpec', [
    'expected_version', 'version_command', 'version_command_args',
    'version_field', 'match_exact_version'
])


def get_dependency_map() -> Dict[str, DependencySpec]:
    return {
        'kubectl':
        DependencySpec(
            expected_version=KUBECTL_MIN_VERSION,
            version_command=execute_system_command,
            version_command_args=['kubectl', 'version', '--client'],
            version_field='GitVersion:',
            match_exact_version=False),
        'kubectl server':
        DependencySpec(
            expected_version=KUBECTL_SERVER_MIN_VERSION,
            version_command=execute_system_command,
            version_command_args=['kubectl', 'version', '--short'],
            version_field='Server Version:',
            match_exact_version=False),
        'helm client':
        DependencySpec(
            expected_version=HELM_VERSION,
            version_command=execute_system_command,
            version_command_args=[
                os.path.join(Config().config_path, 'helm'), 'version',
                '--client'
            ],
            version_field='SemVer:',
            match_exact_version=True),
        'helm server':
        DependencySpec(
            expected_version=HELM_VERSION,
            version_command=execute_system_command,
            version_command_args=[
                os.path.join(Config().config_path, 'helm'), 'version',
                '--server', '--debug', '--tiller-connection-timeout',
                f'{HELM_SERVER_CONNECTION_TIMEOUT}', '--tiller-namespace',
                NAMESPACE_PLACEHOLDER
            ],
            version_field='SemVer:',
            match_exact_version=True),
        'git':
        DependencySpec(
            expected_version=GIT_VERSION,
            version_command=execute_system_command,
            version_command_args=[
                'git', '--version'
            ],
            version_field='git version',
            match_exact_version=False
        ),
    }


SUPPORTED_OS_MAP = {
    'ubuntu': UBUNTU_MIN_VERSION,
    'rhel': REDHAT_MIN_VERSION,
    'macos': MACOS_MIN_VERSION,
    'windows_pro': WINDOWS_MIN_VERSION,
    'windows_enterprise': WINDOWS_MIN_VERSION
}


def _is_version_valid(installed_version: LooseVersion,
                      expected_version: LooseVersion,
                      match_exact_version=False) -> bool:
    return installed_version == expected_version if match_exact_version else installed_version >= expected_version


def _parse_installed_version(version_output: str, version_field='SemVer') -> LooseVersion:
    regex = r"{version_field}(?:\"([\w.-]+)\"| ([\w.-]+))".format(version_field=version_field)
    matches = re.findall(regex, version_output)

    if len(matches) != 1:
        raise ValueError(
            Texts.PARSE_FAIL_ERROR_MSG.format(version_field=version_field, version_output=version_output))

    installed_version = LooseVersion(matches[0][0] or matches[0][1])

    return installed_version


def check_os():
    """ Check if user's OS is supported by nctl. """
    try:
        os_name, os_version = get_os_version()
        if os_name == "":
            raise InvalidOsError(Texts.UNKNOWN_OS_ERROR_MSG)
    except InvalidOsError:
        raise
    except Exception as exe:
        raise InvalidOsError(Texts.GET_OS_VERSION_ERROR_MSG) from exe
    log.info(f"Detected OS: {os_name} {os_version}")
    if os_name not in SUPPORTED_OS_MAP:
        raise InvalidOsError(
            Texts.UNSUPPORTED_OS_ERROR_MSG.format(
                os_name=os_name, os_version=os_version))
    if not _is_version_valid(os_version, SUPPORTED_OS_MAP[os_name]):
        raise InvalidOsError(
            Texts.INVALID_OS_VERSION_ERROR_MSG.format(
                os_name=os_name, os_version=os_version))


def check_dependency(dependency_name: str,
                     dependency_spec: DependencySpec,
                     namespace: str = None,
                     saved_versions: Dict[str, LooseVersion] = None
                     ) -> Tuple[bool, LooseVersion]:
    """
    Check if dependency defined by given DependencySpec is valid
    :param dependency_name: name of dependency to check
    :param dependency_spec: specification of dependency to check
    :param namespace: k8s namespace where server component of checked dependency is located
    :param saved_versions: dict containing saved versions from previous dependency check. If provided, saved version
    will be used instead of running command to check version of dependency
    :return: a tuple of validation status and installed version
    """
    if namespace:
        for i, arg in enumerate(dependency_spec.version_command_args):
            dependency_spec.version_command_args[i] = arg.replace(
                NAMESPACE_PLACEHOLDER, namespace)

    if saved_versions and saved_versions.get(dependency_name):
        log.debug(
            f'Reading {dependency_name} version from saved verify result.')
        return _is_version_valid(
            saved_versions[dependency_name], dependency_spec.expected_version,
            dependency_spec.match_exact_version), saved_versions[
                dependency_name]

    try:
        output, exit_code, log_output = dependency_spec.version_command(dependency_spec.version_command_args)
        if exit_code != 0:
            raise RuntimeError
    except RuntimeError as e:
        raise RuntimeError(
            Texts.VERSION_CMD_FAIL_MSG.format(
                version_cmd=dependency_spec.version_command,
                version_cmd_args=dependency_spec.version_command_args,
                output=log_output)) from e

    if dependency_spec.version_field:
        installed_version = _parse_installed_version(
            output, version_field=dependency_spec.version_field)
    else:
        installed_version = LooseVersion(output.strip())

    return _is_version_valid(
        installed_version=installed_version,
        expected_version=dependency_spec.expected_version,
        match_exact_version=dependency_spec.match_exact_version
    ), installed_version


def check_all_binary_dependencies(namespace: str):
    """
    Check versions for all dependencies of carbon CLI. In case of version validation failure,
     an InvalidDependencyError is raised. This function is intended to be called before most of CLI commands.
     Behaviour of this function is similar to verify CLI command.
    :param namespace: k8s namespace where server components of checked dependencies are located
    """
    saved_versions = load_dependency_versions()
    dependency_versions = {}

    for dependency_name, dependency_spec in get_dependency_map().items():
        try:
            supported_versions_sign = '==' if dependency_spec.match_exact_version else '>='
            valid, installed_version = check_dependency(
                dependency_name=dependency_name,
                dependency_spec=dependency_spec,
                namespace=namespace,
                saved_versions=saved_versions)
            dependency_versions[dependency_name] = installed_version
            log.info(
                f'Checking version of {dependency_name}. '
                f'Installed version: ({installed_version}). '
                f'Supported version {supported_versions_sign} {dependency_spec.expected_version}.'
            )
            if not valid:
                raise InvalidDependencyError(
                    Texts.INVALID_DEPENDENCY_ERROR_MSG.format(
                        dependency_name=dependency_name,
                        installed_version=installed_version,
                        expected_version=dependency_spec.expected_version))
        except FileNotFoundError as e:
            error_msg = Texts.DEPENDENCY_NOT_INSTALLED_ERROR_MSG.format(
                dependency_name=dependency_name)
            log.exception(error_msg)
            raise InvalidDependencyError(error_msg) from e
        except (RuntimeError, ValueError, TypeError) as e:
            error_msg = Texts.VERSION_GET_FAIL_MSG.format(
                dependency_name=dependency_name)
            log.exception(error_msg)
            raise InvalidDependencyError(error_msg) from e
    else:
        # This block is entered if all dependencies were validated successfully
        # Save dependency versions in a file, if there were no saved versions
        if not saved_versions:
            save_dependency_versions(dependency_versions)


def get_dependency_versions_file_path() -> str:
    nctl_version = VERSION
    nctl_config_directory = Config().config_path
    dependency_versions_file_path = os.path.join(
        nctl_config_directory,
        f'{nctl_version}{DEPENDENCY_VERSIONS_FILE_SUFFIX}')
    return dependency_versions_file_path


def save_dependency_versions(dependency_versions: Dict[str, LooseVersion]):
    """
    Saves a YAML file containing versions of nctl dependencies under $(NCTL_CONFIG)/$(nctl_version) path.
    :param dependency_versions: a dictionary containing dependency names as keys and their versions as values
    """
    dependency_versions_file_path = get_dependency_versions_file_path()
    log.info(f'Saving dependency versions to {dependency_versions_file_path}')
    dependency_versions_obj = {k: str(v) for k, v in dependency_versions.items()}
    with open(
            dependency_versions_file_path, 'w',
            encoding='utf-8') as dependency_versions_file:
        yaml.safe_dump(dependency_versions_obj, dependency_versions_file)


def load_dependency_versions() -> Optional[Dict[str, LooseVersion]]:
    """
    Loads saved dependency version for current nctl version. Returns None if dependency version file is not present.
    """
    dependency_versions_file_path = get_dependency_versions_file_path()
    log.info(
        f'Loading dependency versions from {dependency_versions_file_path}')
    if os.path.exists(dependency_versions_file_path):
        with open(
                dependency_versions_file_path, 'r',
                encoding='utf-8') as dependency_versions_file:
            log.info(
                f'Loaded dependency versions from {dependency_versions_file_path}'
            )
            dependency_versions = yaml.safe_load(dependency_versions_file)
            dependency_versions_obj = {k: LooseVersion(v) for k, v in dependency_versions.items()}
            return dependency_versions_obj
    else:
        log.info(
            f'{dependency_versions_file_path} dependency versions file not found'
        )
        return None
