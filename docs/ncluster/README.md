# 딥셀 엔클러스터에서 변경된 내용

# 템플릿 자원 요구량 수정
텝플리에 정의된 디폴트 CPU, Memory 요구량을 수정(작게하여 자원이 많지 않은 경우에도 실행되도록)였습니다.

# 템플릿 추가
다음과 같은 템플릿을 추가
* jupyter-deepcell : anaconda 지원, tensorflow 2.1 지원  
* jupyter-gpu : nvidia gpu 지원, tesnsorflow 2.1 지원
  - [GPU 사용 준비](docs/ncluster/GPU-nvidia.md) 참고

# 사용 방법(명령어 예)
~~~
nctl exp i -t jupyter-deepcell
nctl exp i -t jupyter-gpu
~~~