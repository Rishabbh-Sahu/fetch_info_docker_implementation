# Text pre-processing implemented with docker container
A simplest illustration of deploying any model (or a rule based engine in this scenario) using docker container. The main focus of this repo is to leverage Docker images to run the solutions anywhere you want. Here, a text pre-processing method is been used, to filter only alphanumeric characters within the input text and deployed in dockeer container. 

#### Steps 
 - Build the docker image
 ```buildoutcfg
docker build -t flask-rest-api .
```
 - You can check and verify the docker image using images params.
```buildoutcfg
docker images
```
 - Run the docker image
```buildoutcfg
docker run -d -p 5000:5000 flask-rest-api
```
 - To see that the container is in fact running:
```buildoutcfg
docker ps -a
```
 - To show all the logs for the container 
```buildoutcfg
docker logs <CONTAINER ID OR CONTAINER NAME>
```
#### Reference
https://medium.com/nerd-for-tech/deploy-your-flask-rest-api-on-docker-909f5cfa8b0b
