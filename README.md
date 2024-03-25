# microservices-basics
This is an educational project, aimed to develop a system based on microservice architecture

Runner result:
```json
Posting message: msg1
Response: Success
200
Posting message: msg2
Response: Success
200
Posting message: msg3
Response: Success
200
Posting message: msg4
Response: Success
200
Posting message: msg5
Response: Success
200
Posting message: msg6
Response: Success
200
Posting message: msg7
Response: Success
200
Posting message: msg8
Response: Success
200
Posting message: msg9
Response: Success
200
Posting message: msg10
Response: Success
200
msg5
msg8
msg9
msg3
msg1
msg4
msg6
msg7
msg2
msg10

msg1
msg4
msg5
msg6
msg8msg2
msg3
msg7
msg9
msg10
```

Messages result:

First service:
```json
Received msg2
Received msg3
Received msg7
Received msg9
Received msg10
['msg2', 'msg3', 'msg7', 'msg9', 'msg10']
127.0.0.1 - - [25/Mar/2024 21:53:56] "GET /api/v1.0/msg HTTP/1.1" 200 -
```

Second service:
```json
Received msg1
Received msg4
Received msg5
Received msg6
Received msg8
['msg1', 'msg4', 'msg5', 'msg6', 'msg8']
127.0.0.1 - - [25/Mar/2024 21:53:56] "GET /api/v1.0/msg HTTP/1.1" 200 -
```

Logging services:

```json
 * Running on http://127.0.0.1:6003
received POST
127.0.0.1 - - [25/Mar/2024 21:53:55] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:55] "POST /api/v1.0/log HTTP/1.1" 200 -


 * Running on http://127.0.0.1:6001
Press CTRL+C to quit
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received GET
127.0.0.1 - - [25/Mar/2024 21:53:56] "GET /api/v1.0/log HTTP/1.1" 200 -

 * Running on http://127.0.0.1:6002
Press CTRL+C to quit
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
received POST
127.0.0.1 - - [25/Mar/2024 21:53:56] "POST /api/v1.0/log HTTP/1.1" 200 -
```