# DJango Docker App

## Follow the below steps for pushing a dockerized image to a HCF Cluster.

1. Log in to the HCF cluster from UI and set "Allow sudo" flag to true under Admin->Quota plans.
2. Now from cmd line, target to the cluster and select org and space.
	$ cf api --skip-ssl-validation <cluster-url>
    $ cf login -u <username> -o <org> -s <space>
3. Push the docker image to the cluster.

   Image-Description:- hdpqa/django-fileupload2 This dockerized image is a django based application, to upload and view text files
   
   Cf command to push the docker-image
   
```bash
    $ cf push djangofileupload --docker-image/-o hdpqa/django-fileupload2
```
4. After the cf push operation, it will end up with an application url.
        
5. Access the application url from browser. Browse,upload and view the files.


## Steps to access the django docker images from containers :-

### List of Docker Images:-
     
1. hdpqa/test-fibonacci

    Image-Description: This dockerized image is based on bottle WSGI Framework, and used to generate fibonacci sequence.

2. hdpqa/test-deployment

    Image-Description: This dockerized image is based on bottle WSGI framework, and display's deployment version.

3. hdpqa/django-fileupload2
4. hdpqa/django_emp

    Image-Description:- This dockerized image is a django based application, to add employee profile details.
5. hdpqa/django_calc

Image-Description:- This dockerized image is a django based application, used to calculate avg, execution time of a script.

### Create a docker container, using any of the above images.
```bass
$ docker pull <image-name>
$ docker run --name <container-name> -p 8080:8080 <docker-imagename>
Eg: docker run --name container1 -p 8080:8080 hdpqa/django_calc
```
Now from browser, access the application with the url as 'http://<machine-ip>:8080'
