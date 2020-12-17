## Message of the day
<hr >

### Introduction
Message-of-the-day is simple Django REST application, which displays message (quote) to user.
When once displayed, it will be the same for next 24 hours.

### Installation
Please follow below steps:
1) `git clone https://github.com/KonradMarzec1991/Message-of-the-day.git`
2) `docker-compose up --build` (in main folder)

### Usage
There are 6 content-types user can negotiate:
1) JSON
2) Plain text
3) XML
4) YAML
5) MessagePack
6) HTML Form

In order to request given content-type, please use `Accept` header with requested value.
Below some samples (screenshots), how to do it in Postman:

1) JSON
![json](https://user-images.githubusercontent.com/33575891/102020428-78aef080-3d79-11eb-960c-35f1952963d5.png)

2) XML
![xml](https://user-images.githubusercontent.com/33575891/102020440-8f554780-3d79-11eb-8bad-0ed17a7c90e8.png)

3) YAML
![yaml](https://user-images.githubusercontent.com/33575891/102020461-b14eca00-3d79-11eb-9593-ee2629a86ff7.png)

4) When used not served content-type, message with status code 406 will be displayed
![406](https://user-images.githubusercontent.com/33575891/102020468-bca1f580-3d79-11eb-81f3-1f9835c8438f.png)
