# Wordpress App

This Readme file is for docker file Dockerfile_wordpress.
It is based on Ubuntu15.04 , and it sets up jdk, curl, git , wordpress and nginx

## Steps
1. copy the file to any folder as Dockerfile
2. Run docker build .
3. Image is created 
4. run docker run -it $imageid
5. Use that container in app 

OR

1. Push to image to docker hub
2. use that image to build container in app of HCF Cluster 