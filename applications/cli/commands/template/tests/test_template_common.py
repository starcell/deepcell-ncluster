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

import os
from unittest import mock
from unittest.mock import patch, mock_open

import pytest
import requests.exceptions
import yaml

import util.config
from util.exceptions import ExceptionWithMessage
from commands.template.common import extract_chart_description, Template, get_remote_templates, get_local_templates, \
    prepare_list_of_templates, get_repository_address
from cli_text_consts import TemplateListCmdTexts as Texts

CHART_NAME = "test"
CHART_DESCRIPTION = "test description"
CHART_VERSION = "1.0.1"


CORRECT_CHART_FILE = f"name: {CHART_NAME}\nversion: {CHART_VERSION}\ndescription: {CHART_DESCRIPTION}\nfake_key: key"

INCORRECT_CHART_FILE = "aname: test\n"

REPOSITORY_ADDRESS = "http://test-repo.zoo"
ACCESS_TOKEN = "access-token"

CORRECT_CONF_FILE = f"model-zoo-address: {REPOSITORY_ADDRESS}\naccess-token: {ACCESS_TOKEN}"
INCORRECT_CONF_FILE = f"access-token: {ACCESS_TOKEN}"

REMOTE_TEMPLATE_NAME = "Remote template"
LOCAL_TEMPLATE_NAME = "Local template"
LOCAL_CHART_VERSION = "1.0.2"

TEMPLATE_CHART_YAML = '''
name: test_template
apiVersion: v1
description: Test template
version: 0.1.0
'''

REMOTE_TEMPLATE = Template(name=REMOTE_TEMPLATE_NAME, description=CHART_DESCRIPTION, remote_version=CHART_VERSION)
LOCAL_TEMPLATE_1 = Template(name=REMOTE_TEMPLATE_NAME, description=CHART_DESCRIPTION, local_version=LOCAL_CHART_VERSION)
LOCAL_TEMPLATE_2 = Template(name=LOCAL_TEMPLATE_NAME, description=CHART_DESCRIPTION, local_version=LOCAL_CHART_VERSION)

EXCEPTION_MESSAGE = "exception message"


def assert_template(template: Template, name: str = CHART_NAME, description: str = CHART_DESCRIPTION,
                    local_version: str = None,
                    remote_version: str = None):
    assert template.name == name
    assert template.description == description
    assert template.local_version == local_version
    assert template.remote_version == remote_version


def test_extract_chart_description_local_success():

    chart = extract_chart_description(CORRECT_CHART_FILE, local=True)

    assert_template(chart, local_version="1.0.1")


def test_extract_chart_description_remote_success():

    chart = extract_chart_description(CORRECT_CHART_FILE, local=False)

    assert_template(chart, remote_version="1.0.1")


def test_extract_chart_description_failure():

    chart = extract_chart_description(INCORRECT_CHART_FILE, local=True)

    assert chart is None


def test_get_remote_templates_success(mocker):
    get_manifest_mock = mocker.patch("commands.template.common.requests.get").return_value
    get_manifest_mock.json.return_value = {'templates': [{'name': CHART_NAME, 'version': '1.0.1',
                                                          'url': f'{CHART_NAME}.tar.gz',
                                                          'description': CHART_DESCRIPTION}]}

    result = get_remote_templates(REPOSITORY_ADDRESS)

    assert len(result) == 1
    assert_template(result[CHART_NAME], name=CHART_NAME,  remote_version="1.0.1", description=CHART_DESCRIPTION)


def test_get_remote_templates_error(mocker):
    get_manifest_mock = mocker.patch("commands.template.common.requests.get")
    mock_response = mock.Mock()
    mock_response.status_code = 503
    get_manifest_mock.side_effect = requests.exceptions.HTTPError(response=mock_response)
    get_manifest_mock.json.return_value = {'templates': [{'name': CHART_NAME, 'version': '1.0.1',
                                                          'description': CHART_DESCRIPTION}]}

    with pytest.raises(ExceptionWithMessage):
        get_remote_templates(REPOSITORY_ADDRESS)


def test_get_local_templates_success(mocker, monkeypatch):
    def mockreturn(path):
        return '/abc'

    monkeypatch.setattr(os.path, 'expanduser', mockreturn)

    mocker.patch("os.walk").return_value = [("template_name", "dirnames", "filenames")]
    mocker.patch("os.path.split").return_value = CHART_NAME
    mocker.patch("os.path.isfile").return_value = True
    patch.object(util.config.Config, "get_config_path", return_value="")

    with patch("builtins.open", mock_open(read_data=CORRECT_CHART_FILE)), \
         patch.object(util.config.Config, "get_config_path", return_value="config_path"): # noqa
        dict = get_local_templates()

        assert len(dict) == 1
        assert dict[CHART_NAME].name == CHART_NAME


def test_prepare_list_of_templates(mocker):
    get_repository_address_mock = mocker.patch("commands.template.common.get_repository_address")
    get_repository_address_mock.return_value = "location"
    get_remote_templates_mock = mocker.patch("commands.template.common.get_remote_templates")
    get_remote_templates_mock.return_value = {REMOTE_TEMPLATE_NAME: REMOTE_TEMPLATE}
    get_local_templates = mocker.patch("commands.template.common.get_local_templates")
    get_local_templates.return_value = {REMOTE_TEMPLATE_NAME: LOCAL_TEMPLATE_1, LOCAL_TEMPLATE_NAME: LOCAL_TEMPLATE_2}

    list, error_messages = prepare_list_of_templates()

    assert len(list) == 2

    assert REMOTE_TEMPLATE.representation() in list
    assert LOCAL_TEMPLATE_2.representation() in list

    assert get_repository_address_mock.call_count == 1


def test_prepare_list_of_templates_only_remote(mocker):
    get_repository_address_mock = mocker.patch("commands.template.common.get_repository_address")
    get_repository_address_mock.return_value = "location"
    get_remote_templates_mock = mocker.patch("commands.template.common.get_remote_templates")
    get_remote_templates_mock.return_value = {REMOTE_TEMPLATE_NAME: REMOTE_TEMPLATE}
    get_local_templates = mocker.patch("commands.template.common.get_local_templates")

    list, error_messages = prepare_list_of_templates()

    assert len(list) == 1

    assert REMOTE_TEMPLATE.representation() in list
    assert LOCAL_TEMPLATE_2.representation() not in list

    assert get_local_templates.call_count == 1
    assert get_remote_templates_mock.call_count == 1
    assert get_repository_address_mock.call_count == 1


def test_prepare_list_of_templates_only_local(mocker):
    get_repository_address_mock = mocker.patch("commands.template.common.get_repository_address")
    get_repository_address_mock.return_value = "location"
    get_remote_templates_mock = mocker.patch("commands.template.common.get_remote_templates")
    get_remote_templates_mock.return_value = {}
    get_local_templates = mocker.patch("commands.template.common.get_local_templates")
    get_local_templates.return_value = {LOCAL_TEMPLATE_NAME: LOCAL_TEMPLATE_1, REMOTE_TEMPLATE_NAME: LOCAL_TEMPLATE_2}

    list, error_messages = prepare_list_of_templates()

    assert len(list) == 2

    assert LOCAL_TEMPLATE_1.representation() in list
    assert LOCAL_TEMPLATE_2.representation() in list

    assert get_remote_templates_mock.call_count == 1
    assert get_local_templates.call_count == 1
    assert get_repository_address_mock.call_count == 1


def test_prepare_list_of_templates_remote_failure(mocker):
    get_repository_address_mock = mocker.patch("commands.template.common.get_repository_address")
    get_repository_address_mock.return_value = "location"
    get_remote_templates_mock = mocker.patch("commands.template.common.get_remote_templates")
    get_remote_templates_mock.side_effect = ExceptionWithMessage(EXCEPTION_MESSAGE)
    get_local_templates = mocker.patch("commands.template.common.get_local_templates")
    get_local_templates.return_value = {LOCAL_TEMPLATE_NAME: LOCAL_TEMPLATE_1, REMOTE_TEMPLATE_NAME: LOCAL_TEMPLATE_2}

    list, error_messages = prepare_list_of_templates()

    assert len(list) == 2
    assert len(error_messages) == 1

    assert LOCAL_TEMPLATE_1.representation() in list
    assert LOCAL_TEMPLATE_2.representation() in list
    assert EXCEPTION_MESSAGE == error_messages[0]

    assert get_remote_templates_mock.call_count == 1
    assert get_local_templates.call_count == 1
    assert get_repository_address_mock.call_count == 1


def test_prepare_list_of_templates_local_failure(mocker):
    get_repository_address_mock = mocker.patch("commands.template.common.get_repository_address")
    get_repository_address_mock.return_value = "location"
    get_remote_templates_mock = mocker.patch("commands.template.common.get_remote_templates")
    get_remote_templates_mock.return_value = {REMOTE_TEMPLATE_NAME: REMOTE_TEMPLATE}
    get_local_templates = mocker.patch("commands.template.common.get_local_templates")
    get_local_templates.side_effect = ExceptionWithMessage(EXCEPTION_MESSAGE)

    list, error_messages = prepare_list_of_templates()

    assert len(list) == 1
    assert len(error_messages) == 1

    assert REMOTE_TEMPLATE.representation() in list
    assert LOCAL_TEMPLATE_2.representation() not in list
    assert Texts.ERROR_DURING_LOADING_LOCAL_TEMPLATES == error_messages[0]

    assert get_local_templates.call_count == 1
    assert get_remote_templates_mock.call_count == 1
    assert get_repository_address_mock.call_count == 1


def test_get_repository_address_success(mocker):
    mocker.patch("util.config.Config.get_config_path", return_value="")
    mocker.patch("os.path.isfile").return_value = True

    with patch("builtins.open", mock_open(read_data=CORRECT_CONF_FILE)):
        repository_location = get_repository_address()

    assert repository_location == REPOSITORY_ADDRESS


def test_get_repository_address_lack_of_conf_file(mocker):
    mocker.patch("util.config.Config.get_config_path", return_value="")
    mocker.patch("os.path.isfile").return_value = False

    repository_location = get_repository_address()

    assert not repository_location


def test_get_repository_address_incorrect_file(mocker):
    mocker.patch("util.config.Config.get_config_path", return_value="")
    mocker.patch("os.path.isfile").return_value = True

    with patch("builtins.open", mock_open(read_data=INCORRECT_CONF_FILE)):
        repository_location = get_repository_address()

    assert not repository_location


def test_update_chart_yaml(tmpdir):
    fake_chart_yaml_file = tmpdir.mkdir('template-dir').join('Chart.yaml')
    fake_chart_yaml_file.write(TEMPLATE_CHART_YAML)
    test_template = Template(name='test-template', description='Test template', local_version='1.0.0')
    test_template.update_chart_yaml(chart_yaml_path=fake_chart_yaml_file.strpath)

    with open(fake_chart_yaml_file.strpath, mode='r', encoding='utf-8') as chart_yaml_file:
        modified_chart_yaml = yaml.safe_load(chart_yaml_file)

    assert modified_chart_yaml['name'] == test_template.name
    assert modified_chart_yaml['description'] == test_template.description
    assert modified_chart_yaml['version'] == test_template.local_version


def test_render_from_existing_template(mocker, tmpdir):
    dlsctl_config_dir = tmpdir.mkdir('config')
    mocker.patch("util.config.Config.get_config_path", return_value=dlsctl_config_dir.strpath)

    packs_dir = dlsctl_config_dir.mkdir("packs")

    src_template_name = 'src-template'
    src_template_dir = packs_dir.mkdir(src_template_name)
    src_chart_yaml_file = src_template_dir.mkdir('charts').join('Chart.yaml')
    src_chart_yaml_file.write(TEMPLATE_CHART_YAML)

    test_template = Template(name='test-template', description='Test template', local_version='1.0.0')
    dest_template_dir = packs_dir.join(test_template.name)
    dest_chart_yaml_file = dest_template_dir.join('charts').join('Chart.yaml')

    mocker.patch.object(test_template, 'update_chart_yaml')
    test_template.render_from_existing_template(src_template_name=src_template_name)

    assert dest_template_dir.check()
    assert dest_chart_yaml_file.check()
