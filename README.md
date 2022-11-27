![](https://github.com/regiapriandi012/python-microservice-kubernetes/actions/workflows/google.yml/badge.svg)
# Python Microservice Kubernetes - Example
Microservice architecture design built using Python, Rabbitmq, Postgresql, Mongodb to build a video to Mp3 conversion API.
## API Convert Video to MP3
![image](https://user-images.githubusercontent.com/69528812/204116100-1238cb24-cf90-4538-bdcb-cb0cdd60a71a.png)
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
### Configure Queue on Rabbitmq
  - #### Access manager on IP:30004
    ```
    Username: guest (default)
    Password: guest (default)
    ```
  - #### Add Queues
    <img width="960" alt="image" src="https://user-images.githubusercontent.com/69528812/204124113-060ba3ec-4aac-443b-b4b3-75359ce520dd.png">
##
### Testing
  - #### Login
    ```
    $ curl -X POST 192.168.56.2:30002/login -u regiapriandi012@gmail.com:12345
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJlZ2lhcHJpYW5kaTAxMkBnbWFpbC5jb20iLCJleHAiOjE2Njk2MTUxMjEsImlhdCI6MTY2OTUyODcyMSwiYWRtaW4iOnRydWV9.YpNpfTBJLI7u3v6lwDZphGPBnjc83t7m9DkUnTXifpU
    ```
  - #### Upload Video
    ```
    $ curl -X POST -F 'file=@./video.mp4' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJlZ2lhcHJpYW5kaTAxMkBnbWFpbC5jb20iLCJleHAiOjE2Njk2MTUxMTIsImlhdCI6MTY2OTUyODcxMiwiYWRtaW4iOnRydWV9.TgMr3Uwk5pnZNrCMWYZfsdkBrTfx2IMnYbET_iwJu-g' 192.168.56.2:30002/upload
    ```
  - #### Get Mp3 file ID
    <img width="288" alt="image" src="https://user-images.githubusercontent.com/69528812/204123781-d51f5cbf-6f9a-4de0-bafb-dc5367be754e.png">
  - #### Download Mp3
    ```
    curl --output video.mp3 -X GET -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJlZ2lhcHJpYW5kaTAxMkBnbWFpbC5jb20iLCJleHAiOjE2Njk2MTUxMTIsImlhdCI6MTY2OTUyODcxMiwiYWRtaW4iOnRydWV9.TgMr3Uwk5pnZNrCMWYZfsdkBrTfx2IMnYbET_iwJu-g' "192.168.56.2:30002/download?fid=63830df2667a14a04a9d99b9"
    ```
  - #### Show Mp3 downloaded
    ```
    $ ls | grep .mp3
    video.mp3
    ```
