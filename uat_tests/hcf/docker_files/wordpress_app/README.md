# Wordpress App

This Readme file is for dockerizing wordpress app. It is based on tutum/wordpress image, which setups mysql, wordpress server.

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
Eg: docker run -p 80:80 -p 3306:3306 hdpqa/wordpress_app
```

Now from browser, access the application with the url as 'http://<machine-ip>:80'
The current working deployment is :
http://52.26.116.213/    (login details:admin/test123)
