FROM python:3.9.0

WORKDIR /source

COPY . /source

# RUN sudo usermod -a -G video developer
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install libxkbcommon-x11-0 -y
RUN apt-get install libxcb-xinerama0  
RUN apt-get install -y libasound2-dev
RUN pip3 install --no-cache-dir -r requirements.txt


