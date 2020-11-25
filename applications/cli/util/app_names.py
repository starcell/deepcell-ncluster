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

from enum import Enum


#  list of nauta app names - it contains labels under which nauta apps are visible on a cluster
class NAUTAAppNames(Enum):
    ELASTICSEARCH = "elasticsearch"
    DOCKER_REGISTRY = "docker-registry"
    WEB_GUI = "gui"
    TENSORBOARD = "tensorboard"
    TENSORBOARD_SERVICE = "tensorboard-service"
    INGRESS = "ingress"
    JUPYTER = "jupyter"
    DEEPCELL = "deepcell"
    GPU_NVIDIA = "gpu-nvidia"
    GIT_REPO_MANAGER = "gitea"
    GIT_REPO_MANAGER_SSH = "gitea-ssh"
