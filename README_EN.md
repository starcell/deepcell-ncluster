# deepcell-ncluster

![Nauta Diagram](docs/nauta.png)

<p align="center">
  <a href="README.md">한국어</a> |
  <span>English</span>
</p>

See the Nauta docs at: https://intelai.github.io/nauta/


The Deepcell ncluster is software package for building Kubernetes cluster. Deepcell ncluster started by forking Intel Nauta. The Nauta software provides a multi-user, distributed computing environment for running deep learning model training experiments. Results of experiments, can be viewed and monitored using a command line interface, web UI and/or TensorBoard*. You can use existing data sets, use your own data, or downloaded data from online sources, and create public or private folders to make collaboration among teams easier.
But Intel has decided to stop further development of Nauta and will no longer be supporting the product. So Starcell started Deepcell ncluster project. Deepcell ncluster intends to develop as a cluster building software that is useful not only for deep learning computing environments, but also for building Kubernetes clusters for general services, especially microservices.
In addition, Deepcell ncluster supports deep learning frameworks using GPUs.

The following are the features currently supported by Deepcell ncluster.

* Tensorflow/CPU : Batch, Jupyter Notebook  
* Tensorflw/GPU : Batch, Jupyter Notebook  
* PyTorch/CPU : Batch, Jupyter Notebook(지원예정)  
* PyTorch/GPU : Batch, Jupyter Notebook(지원예정)  
* Horovod를 이용한 분산 딥러닝  
* TensorBoard  
* Tensorflow Serving  
* OpenVINO OpenVINO Model Server

Currently, GPU support has been added, and other features are the same as Nauta. Documents for functions that are not available in Nauta or changed functions are first written and released. For the Nauta function, please refer to the Nauta documentation for the time being.

To build Nauta installation package and run it smoothly on Google Cloud Platform please follow our [Nauta on Google Cloud Platform - Getting Started](toolbox/providers/gcp/gcp.md). More details on building Nauta artifacts can be found in [How to Build](docs/installation-and-configuration/How_to_Build_Nauta/HBN.md) guide.

To get things up and running quickly please take a look at our [Getting Started](docs/user-guide/actions/getting_started.md) guide.

For more in-depth information please refer to the following documents:

- [Nauta Installation and configuration guide](docs/installation-and-configuration/) 
- [Nauta User Guide](docs/user-guide/README.md)

# License

By contributing to the project software, you agree that your contributions will be licensed under the Apache 2.0 license that is included in the LICENSE file in the root directory of this source tree.
The user materials are licensed under [CC-BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/legalcode).

# Contact

Submit Github issue to ask a question, submit a request or report a bug.
