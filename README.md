# Text pre-processing implemented with docker container
Simple approach to fetch certain info from the text, provided to it and integration with the docker.

#### Steps to be followed -
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
#### Reference - https://medium.com/nerd-for-tech/deploy-your-flask-rest-api-on-docker-909f5cfa8b0b
