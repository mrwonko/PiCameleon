FROM balenalib/raspberrypi3-python:3.7-buster

RUN apt update && apt install -y \
    libatlas3-base \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN echo "[global]\nextra-index-url=https://www.piwheels.org/simple" > /etc/pip.conf
RUN pip3 install -r requirements.txt && rm /requirements.txt

COPY picameleon /picameleon
WORKDIR /picameleon
ENTRYPOINT python3 -u main.py configs/$CONFIG_FILE
