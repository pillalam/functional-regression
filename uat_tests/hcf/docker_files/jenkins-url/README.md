# Docker file for Jenkins

 This readme provides steps to push a dockerized image to cluster, and also how to access it as a container.
 
### Steps to Dockerize the image

1. copy the files to any folder as Dockerfile & executors.groovy
2. Run docker build .
3. Image is created 

### Follow the below steps for pushing a dockerized image to a HCF Cluster.

1. Log in to the HCF cluster from UI and set "Allow sudo" flag to true under Admin-Quota plans.
2. Now from cmd line, target to the cluster and select org and space.
        $ cf api --skip-ssl-validation <cluster-url>
    $ cf login -u <username> -o <org> -s <space>
3. Push the docker image to the cluster.

   Image-Description:- hdpqa/jenkins-url This dockerized image is to setuo and run Jenkins server.

   Cf command to push the docker-image

```bash
    $ cf push hdpqa/jenkins_url --docker-image/-o hdpqa/jenkins_url
```
4. After the cf push operation, it will end up with a jenkins url.

5. Access the Jenkins server from browser.


## Steps to access the Jenkins image from containers :-

### Create a docker container, using the above image.
```bass
$ docker pull <image-name>
$ docker run -p 8080:8080 -p 50000:50000 -v <"host-vm-path>:/var/jenkins_home <image_name>
    -> In this step we are storing workspace for jenkins in the host machine.
Eg: docker run -p 8080:8080 -p 50000:50000 -v /home/ubuntu:/var/jenkins_home hdpqa/jenkins_url
```
Now from browser, access the application with the url as 'http://<machine-ip>:8080'
