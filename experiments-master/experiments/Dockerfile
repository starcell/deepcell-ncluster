FROM nauta-registry-nginx.nauta:5000/nauta/tensorflow/1.12.0py3/base:1.12.0-py3
# workdir set to /mnt - is treated by a jupyter as a main folder with notebooks
WORKDIR /mnt

ENV PYTHONUNBUFFERED 1
# setting PASSWORD env variable to an empty string turns off authetication
ENV PASSWORD ""

COPY folder .

# create dummy file to inform user about /mnt/input not being persistent volume
RUN ["mkdir", "/mnt/input"]
RUN echo "Warning - you are able to save some temporary content directly in the input directory. This content is discarded after the session ends." \
    > /mnt/input/README
# CMD ["jupyter", "notebook", "--ip=localhost", "--allow-root"]
ENTRYPOINT  ["jupyter", "notebook", "--allow-root"]

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV NAUTA_EXPERIMENT_NAME mnist-sing-668-20-03-19-11-07-30

ENV NAUTA_USERNAME npark
