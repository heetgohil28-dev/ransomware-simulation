FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip3 install cryptography
RUN mkdir -p /simulation/files
COPY ransomware.py /simulation/ransomware.py
COPY listener.py /simulation/listener.py
COPY files/ /simulation/files/
WORKDIR /simulation
CMD ["python3", "ransomware.py"]
