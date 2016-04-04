# Dockerfile to build ubuntu 
FROM ubuntu:15.04
MAINTAINER Ravikumar Venkatesan <ravikumar_venkatesan@yahoo.com>
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y openjdk-7-jdk
RUN apt-get install -y apache2
RUN apt-get install -y git
RUN apt-get install -y wget
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -q -y install mysql-server mysql-client
EXPOSE 80 
VOLUME /mysql
