# Lamp App

This Readme file is for docker file Dockerfile lamp. It is based on Ubuntu15.04 , and it sets up jdk, curl, git , Apache and mysql
This Readme file is for dockerizing lamp application. It is based on tutum/lamp image, which setups mysql, lamp server.

## Steps
1. copy the file to any folder as Dockerfile
2. Run docker build .
3. Image is created 
4. run docker run -it $imageid
5. Use that container in app 

OR

1. Push to image to docker hub
2. use that image to build container in app of HCF Cluster

## Steps to work with docker containers:

### Create a docker container, using the above image.
```bass
$ docker pull <image-name>
$ docker run -d -p 80:80 -p 3306:3306 <image_name>
    -> In this step we are linking mysql port to host port.
Eg: docker run -p 80:80 -p 3306:3306 hdpqa/lamp_app
```

Now from browser, access the application with the url as 'http://<machine-ip>:80'
