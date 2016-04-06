FROM meenakshim/mysqlimage
MAINTAINER "meenakshim@hpe.com"

ENV DOCKYARD_SRC=django-fileupload2
ENV DOCKYARD_SRVHOME=/srv
ENV DOCKYARD_SRVPROJ=/srv/django-fileupload2

COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt

WORKDIR $DOCKYARD_SRVPROJ

EXPOSE 8080
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
