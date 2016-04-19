# Dockerfile to build ubuntu and install lamp server

FROM tutum/lamp:latest
RUN rm -fr /app && git clone https://github.com/fermayo/hello-world-lamp.git /app
EXPOSE 80 3306
CMD ["/run.sh"]

