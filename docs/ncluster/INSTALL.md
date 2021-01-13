# 딥셀 엔클러스터(Deepcell ncluster) 설치

##  준비사항

설치 작업을 수행할 설치용 시스템(installer system)과 쿠버네티스 클러스터를 구성할 2개 이상의 설치 대상 시스템들이 필요합니다.

   
   
   
## 설치용 시스템 준비

      
설치용 시스템 운영체제:
  * Red Hat Enterprise Linux 7.6
  * CentOS 7.6
  * Ubuntu 16.04, 18.04
  
### 설치용 시스템에 있어야 할 소프트웨어:

   
Red Hat Enterprise Linux 7.6, CentOS 7.6:
  * Python 2.7 and `/usr/bin/python` available
  * Python 3.5
  * sshpass (when password authentication is used)
  * Helm 2.9.1 (the version of a Helm client _must be_ the same as Helm server used by the platform)
   
  
Ubuntu 16.04:
  * Python 2.7 and `/usr/bin/python` available
  * Python 3.5
  * apt packages installed:
    - python3-pip
    - build-essential
    - libffi-dev
    - libssl-dev
    - sshpass
  * Helm 2.9.1 (the version of a Helm client _must be_ the same as Helm server used by the platform)


### 딥셀 엔클러스터 패키지 

빌드가 완성된 패키지를 복사하여 아래와 같은 명령으로 압축을 푼다.

`nauta-1.1.0-ent-20191010050128.tar.gz -C <destination>`



## 설치대상 시스템 준비


베어메탈(bare metal) 시스템으로 클러스터를 구성할 경우 현재 Red Hat Enterprise Linux 7.6 또는 CentOS 7.6을 준비해야 합니다.
마스터와 워커노드로 구성


- Configured access to the master host over SSH.
  - This is configured access from your _Installer Machine to your Target Host (master)._
  
- Full network connectivity between a target hosts is required. In addition, Installer connectivity is only required to the master node.


커널 업데이트

데이터 파일 시스템 준비


### Data directory
마스터에만 필요

The `/data` directory _must_ be created on the master node before installation. This directory contains persistent Kubernetes', as well as explicit Nauta data. Therefore, you should mount a separate disk to this directory. However, the size is dependent on your needs and the number of users. The recommended disk size is 70Gi, as this is a practical solution for a default three-node Nauta environment.   
  
  
### 필요 소프트웨어
  
  
필요 소프트웨어 목록

  - byacc
  - cifs-utils
  - ebtables
  - ethtool
  - gcc
  - gcc-c++
  - git
  - iproute
  - iptables >= 1.4.21
  - libcgroup
  - libcgroup-devel
  - libcgroup-tools
  - libffi-devel
  - libseccomp-devel
  - libtool-ltdl-devel
  - make
  - nfs-utils
  - openssh
  - openssh-clients
  - openssl
  - openssl-devel
  - policycoreutils-python
  - python
  - python-backports
  - python-backports-ssl_match_hostname
  - python-devel
  - python-ipaddress
  - python-setuptools
  - rsync
  - selinux-policy >= 3.13.1-23
  - selinux-policy-base >= 3.13.1-102
  - selinux-policy-targeted >= 3.13.1-102
  - socat
  - systemd-libs
  - util-linux
  - vim
  - wget

필요 소프트웨어 설치
  
yum -y install byacc cifs-utils ebtables ethtool gcc gcc-c++ git iproute
yum -y install libcgroup libcgroup-devel libcgroup-tools libffi-devel
yum -y install libseccomp-devel libtool-ltdl-devel make nfs-utils openssh openssh-clients openssl openssl-devel
yum -y install policycoreutils-python python python-backports
yum -y install python-backports-ssl_match_hostname python-devel python-ipaddress python-setuptools rsync
yum -y install socat systemd-libs util-linux vim wget



### Valid Repositories

설치 대상 시스템에 리포지토리가 정상적으로 설정되어 있으면 설치 작업 중 필요한 소프트웨어를 자동으로 설치 할 수 있다. 그래서 올바른 리포지토리가 등록되어 있는 지 확인하고 등록되지 않았으면 추가 하도록 한다.

#### Repositories List

Use the following command to check your repository list: `yum repolist all`

A list of **required** enabled repositories for RHEL 7.6, is:

- Extra Packages for Enterprise Linux 7 - x86_64
- Red Hat Enterprise Linux 7 Server - x86_64
- Red Hat Enterprise Linux 7 Server (High Availability) - x86_64
- Red Hat Enterprise Linux 7 Server (Optional) - x86_64
- Red Hat Enterprise Linux 7 Server (Supplementary) - x86_64

A list of **required** enabled repositories for Centos 7.6, is:

- CentOS-7 - Base
- CentOS-7 - Extras
- CentOS-7 - Updates
- Extra Packages for Enterprise (epel) 


## 설치 작업
설치용 시스템에서 설처 파일 수정 
  inventory.yaml
  config.yam

ENV_INVENTORY 변수에 inventory.yaml 파일이 설정되어 있어야 한다.

  
ENV_CONFIG 변수에 config.yaml 파일이 설정되어 있어야 한다.


export ENV_INVENTORY=$<absolute path inventory file>
export ENV_CONFIG=$<absolute path config file>


아래 명령을 실행하여 설치 시작
  ./installer.sh install

## 확인
설치 로그에 실패가 없으면 정상적으로 설치 된 것인다.완료 후 확인
  kubectl describe --all-namespaces node
