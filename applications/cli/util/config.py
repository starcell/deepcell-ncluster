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
import sys

from util.k8s.k8s_info import get_config_map_data
from util.logger import initialize_logger
from cli_text_consts import UtilConfigTexts as Texts


# environmental variable with a nctl HOME folder
NCTL_CONFIG_ENV_NAME = 'NCTL_CONFIG'
NCTL_CONFIG_DIR_NAME = 'config'

# name of a directory with EXPERIMENT's data
EXPERIMENTS_DIR_NAME = 'experiments'
# name of a directory with data copied from script folder location
FOLDER_DIR_NAME = 'folder'

# registry config file
DOCKER_REGISTRY_CONFIG_FILE = 'docker_registry.yaml'

NAUTA_NAMESPACE = "nauta"
NAUTA_CONFIGURATION_CM = "nauta"

TBLT_TABLE_FORMAT = "orgtbl"

log = initialize_logger(__name__)


class ConfigInitError(Exception):
    def __init__(self, message: str):
        self.message = message


class Config:
    __shared_state: dict = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not hasattr(self, 'config_path'):
            self.config_path = self.get_config_path()

    @staticmethod
    def validate_config_path(path: str) -> bool:
        if os.path.isdir(path):
            directory_content = os.listdir(path)
            expected_content = {'helm'}
            return expected_content.issubset(directory_content)
        return False

    @staticmethod
    def get_config_path() -> str:
        nctl_cli_dir = os.path.dirname(sys.executable)
        binary_config_dir_path = os.path.join(os.path.split(nctl_cli_dir)[0], NCTL_CONFIG_DIR_NAME)
        user_local_config_dir_path = os.path.join(os.path.expanduser('~'), NCTL_CONFIG_DIR_NAME)

        log.debug(f"{NCTL_CONFIG_DIR_NAME} binary executable path:  {binary_config_dir_path}")
        log.debug(f'{NCTL_CONFIG_DIR_NAME} user home path:  {binary_config_dir_path}')

        if os.environ.get(NCTL_CONFIG_ENV_NAME):
            user_path = os.environ[NCTL_CONFIG_ENV_NAME]
            if os.path.exists(user_path):
                return user_path
            else:
                message = Texts.USER_DIR_NOT_FOUND_ERROR_MSG.format(user_path=user_path,
                                                                    config_env_name=NCTL_CONFIG_ENV_NAME)
                raise ConfigInitError(message)
        elif user_local_config_dir_path and os.path.exists(user_local_config_dir_path):
            return user_local_config_dir_path
        elif binary_config_dir_path and os.path.exists(binary_config_dir_path):
            return binary_config_dir_path
        else:
            message = Texts.NCTL_CONFIG_DIR_NOT_FOUND_ERROR_MSG.format(
                config_dir_name=NCTL_CONFIG_DIR_NAME, binary_config_dir_path=binary_config_dir_path,
                config_env_name=NCTL_CONFIG_ENV_NAME, user_local_config_dir_path=user_local_config_dir_path
            )
            raise ConfigInitError(message)


class NAUTAConfigMap:
    """
    Class for accessing values stored in NAUTA config map on Kubernetes cluster.
    It is implemented using borg pattern (http://code.activestate.com/recipes/66531/),
    so each instance of this class will have shared state, ensuring configuration consistency.
    """
    # images keys' names must be compliant with 'export_images' in tools/nauta-config.yml
    IMAGE_TILLER_FIELD = 'image.tiller'
    EXTERNAL_IP_FIELD = 'external_ip'
    IMAGE_TENSORBOARD_SERVICE_FIELD = 'image.tensorboard_service'
    REGISTRY_FIELD = 'registry'
    PLATFORM_VERSION = 'platform.version'
    PY3_IMAGE_NAME = 'image.tensorflow_1.12_py3'
    DC_IMAGE_NAME = 'image.deepcell'
    GPU_NVIDIA_IMAGE_NAME = 'image.gpu-nvidia'
    PY3_HOROVOD_IMAGE_CONFIG_KEY = 'image.horovod'
    MINIMAL_NODE_MEMORY_AMOUNT = 'minimal.node.memory.amount'
    MINIMAL_NODE_CPU_NUMBER = 'minimal.node.cpu.number'
    PY3_PYTORCH_IMAGE_CONFIG_KEY = 'image.pytorch'
    OPENVINOMS_IMAGE_CONFIG_KEY = 'image.openvino-ms'

    __shared_state: dict = {}

    def __init__(self, config_map_request_timeout: int = None):
        self.__dict__ = self.__shared_state
        if not self.__dict__:
            config_map_data = get_config_map_data(name=NAUTA_CONFIGURATION_CM, namespace=NAUTA_NAMESPACE,
                                                  request_timeout=config_map_request_timeout)
            self.registry = config_map_data[self.REGISTRY_FIELD]
            self.image_tiller = '{}/{}'.format(config_map_data[self.REGISTRY_FIELD],
                                               config_map_data[self.IMAGE_TILLER_FIELD])
            self.external_ip = config_map_data[self.EXTERNAL_IP_FIELD]
            self.image_tensorboard_service = '{}/{}'.format(config_map_data[self.REGISTRY_FIELD],
                                                            config_map_data[self.IMAGE_TENSORBOARD_SERVICE_FIELD])
            self.platform_version = config_map_data.get(self.PLATFORM_VERSION)
            self.py3_image_name = config_map_data.get(self.PY3_IMAGE_NAME)
            self.dc_image_name = config_map_data.get(self.DC_IMAGE_NAME)
            self.gpu_nvidia_image_name = config_map_data.get(self.GPU_NVIDIA_IMAGE_NAME)
            self.py3_horovod_image_name = config_map_data.get(NAUTAConfigMap.PY3_HOROVOD_IMAGE_CONFIG_KEY)
            self.minimal_node_memory_amount = config_map_data.get(NAUTAConfigMap.MINIMAL_NODE_MEMORY_AMOUNT)
            self.minimal_node_cpu_number = config_map_data.get(NAUTAConfigMap.MINIMAL_NODE_CPU_NUMBER)
            self.py3_pytorch_image_name = config_map_data.get(NAUTAConfigMap.PY3_PYTORCH_IMAGE_CONFIG_KEY)
            self.openvinoms_image_name = config_map_data.get(NAUTAConfigMap.OPENVINOMS_IMAGE_CONFIG_KEY)
