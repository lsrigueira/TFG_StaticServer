FROM ubuntu:18.04

WORKDIR /code
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y 
RUN apt-get install python3-pip -y
RUN apt-get install nano -y
RUN apt-get install net-tools -y
RUN apt-get install byobu -y
RUN pip3 install pymongo




RUN mkdir ./src
ADD ./src ./src