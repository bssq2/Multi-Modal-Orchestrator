FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

LABEL maintainer="Samson Boicu <github.com/bssq2>"
ENV DEBIAN_FRONTEND=noninteractive

# System deps
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt /tmp/req.txt
RUN pip3 install --upgrade pip && pip3 install -r /tmp/req.txt

WORKDIR /app
COPY src /app/src
EXPOSE 8080
CMD ["python3", "src/api/api_server.py"]