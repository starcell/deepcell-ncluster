FROM tensorflow/tensorflow:2.1.0-gpu-py3-jupyter

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

RUN pip install --no-cache-dir \
        Pillow==5.4.* \
        h5py==2.9.* \
        ipykernel==5.1.* \
        matplotlib==3.0.* \
        mock==2.0.* \
        numpy==1.16.* \
        scipy==1.2.* \
        scikit-learn==0.20.* \
        pandas==0.23.* \
        wheel==0.32.* \
        jupyterlab==2.2.* \
        graphviz==0.14.* \
        pydot==1.4.*

RUN python -m ipykernel.kernelspec
