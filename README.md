## Message of the day
<hr >

### Introduction
Message-of-the-day is simple Django application, which displays message (quote) to user.
When once displayed message, it will be the same for next 24 hours.

### Installation
Please follow below steps:
1) git clone `https://github.com/KonradMarzec1991/Message-of-the-day.git`
2) When being in main folder, `docker-compose up --build`

### Usage
There are 6 content-types user can negotiate:
1) JSON
2) Plain text
3) XML
4) YAML
5) MessagePack
6) HTML Form

In order to request given content-type, please use `Accept` header with requested value.
Below some samples, how to do it in Postman:
