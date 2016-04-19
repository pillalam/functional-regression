# Dockerfile to build ubuntu and install various services and wordpress

FROM tutum/wordpress:latest
RUN rm -fr /app && git clone --depth=1 https://github.com/WordPress/WordPress.git /app
EXPOSE 80 3306
CMD ["/run.sh"]

