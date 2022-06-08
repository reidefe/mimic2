FROM tensorflow/tensorflow:1.8.0-gpu-py3

RUN mkdir /root/text-to-speech
COPY . /root/mimic2
WORKDIR /root/mimic2
RUN pip install  --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]