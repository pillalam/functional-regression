# Steps to work with docker containers:

### Create a docker container, using the existing public image.
```bass
$ docker pull tutum/wordpress
$ docker run -d -p 80:80 -p 3306:3306 <docker-image>
    -> In this step we are linking mysql port to host port.
Eg: docker run -p 80:80 -p 3306:3306 tutum/wordpress
```

Now from browser, access the application with the url as 'http://<machine-ip>:80'

The current working deployment is :
http://52.26.116.213/    (login details:admin/test123)
