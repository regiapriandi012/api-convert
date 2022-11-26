# Python Microservice Kubernetes - Example
## API Convert Video to MP3
![image](https://user-images.githubusercontent.com/69528812/204096932-d68ecc3e-a263-4c17-bcee-cff8065093b3.png)
## 

### Used Technology
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
## 
### Configure Kubernetes
- #### Configure Auth DB
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f postgresql/manifest/
  ```
- #### Configure File DB
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f mongodb/manifest/
  ```
- #### Configure Rabbitmq Queue
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f rabbit/manifest/
  ```
- #### Configure Auth App
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f python/src/auth/manifest/
  ```
- #### Configure Gateway App
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f python/src/gateway/manifest/
  ```
- #### Configure Converter App
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f python/src/converter/manifest/
  ```
- #### Configure Notification App
  ```
  $ cd python-microservice-kubernetes
  $ kubectl apply -f python/src/notification/manifest/
  ```
##
### Access The Service
- #### Gateway (App) > IP:30002
- #### Auth DB (Postgresql) -> IP:30003
- #### Rabbitmq Manager (Queue) -> IP:30004
- #### File DB (Mongodb) -> IP:30005
##
### Add Auth User
```
--Create Database User
CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR (255) NOT NULL,
    password VARCHAR (255) NOT NULL
);

--Add Username and Password for User
INSERT INTO user (email, password) VALUES ('you@gmail.com', '123456');
```
##
