FROM continuumio/anaconda3:2020.02

RUN conda install nb_conda

# Create the environment:
COPY env_tf1.yml /root/
RUN conda env create -f /root/env_tf1.yml

COPY env_tf2.yml /root/
RUN conda env create -f /root/env_tf2.yml

COPY jupyter_notebook_config.py /root/.jupyter/
COPY notebooks /notebooks

COPY run_jupyter.sh /
RUN chmod +x /run_jupyter.sh

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"

CMD ["/run_jupyter.sh", "--allow-root"]

RUN pip install -U pip==19.0.* setuptools==40.6.*

RUN python -m ipykernel.kernelspec
