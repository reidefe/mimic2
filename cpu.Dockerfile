FROM tensorflow/tensorflow:1.8.0-py3

RUN mkdir /root/mimic2
COPY . /root/mimic2
WORKDIR /root/mimic2
RUN apt-get update
RUN apt-get install -y python3-tk
RUN pip install  --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]