we will see how to run the 'PyFlask app' in flask then we will deploy it in kubernates with the help of docker.



First clone my repo : https://github.com/PIYUSH9090/hello-python-kubernates

1) Then you will get set all the folder and path.

```
cd src
```
First run it locally
```
pip install -r requirements.txt
python main.py
```

2) Create an image- deploy in docker container

At your command line or shell, in the hello-python/app directory, build the image with the following command:
```
docker build -t PyFlask .
```

This will make the image file so if want to check that out you use this command:
```
docker image ls
```
You will get image created before a moment.

Running in Docker 

Now if we want to run this in docker 
```
docker run -p 5001:5000 PyFlask
```

After then we have to push this docker image to docker hub with this command, we can push docker with 2 command 

```
docker image tag PyFlask piyush9090/PyFlask:latest
```
it means :- docker image tag <docker image name> <dockerhub username/docker image name:latest>
    
Secound command is 
```
docker push piyush9090/PyFlask:latest
```

Now you will get this image intop your docker hub account. You can pull from there also whenever you want.


3) Running in Kubernetes - minikube

```
kubectl version
```
If you don’t see a reply with a Client and Server version, you’ll need to install and configure it.


Start the minikube with this command
```
minikube start
```

Then also open dashboard with this command
```
minikube dashboard
```

Now you are working with Kubernetes! You can see the node by typing:
```
kubectl get nodes
```

First you need to authenticate your google cloud
```
gcloud auth login
```

 We have to create first project in google cloud gcloud projects create [PROJECT_ID] --name=[PROJECT_NAME]
```
gcloud projects create pyflask --name=pyflask-62
```
If you already have any project in gcloud then Let's initialize the google cloud
```
gcloud init
```
Now if we want to deploy in minikube let's deploy it with yaml file
```
kubectl apply -f deployment.yaml
```

4) If you want to deploy it via gcloud kubernates -Gcloud kubernates

Now let's create the cluster of kubernates gcloud container clusters create [CLUSTER_NAME] --num-nodes=2
```
gcloud container clusters create translator --num-nodes=2 --zone us-east1-b
```

After creating cluster we should give the permission(credentials) for that container cluster
```
gcloud container clusters get-credentials translator --zone us-east1-b --project pyflask-62
```

Then you have added already yaml file so run this command

```
kubectl apply -f deployment.yaml
```
You can see the pods are running if you execute the following command:

Get the pods
```
kubectl get pods
```
It will create the container inside kubernates deployment then it will run successfully, this is how you can deploy in kubernates.





Thankyou ...
