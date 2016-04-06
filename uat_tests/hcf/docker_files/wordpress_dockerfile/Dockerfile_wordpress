# Dockerfile to build ubuntu and install various services and wordpress
FROM ubuntu:15.04
MAINTAINER Ravikumar Venkatesan <ravikumar_venkatesan@yahoo.com>
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y openjdk-7-jdk
RUN apt-get install -y nginx
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y wordpress
EXPOSE 80 443
VOLUME /wordpress
