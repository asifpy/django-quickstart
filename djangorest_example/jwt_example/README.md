JWT Example
===========

1. Get JWT token
----------------

POST username and password to obtain JWT token for below endpoint.

**REQUEST**

`http post http://localhost:8000/djangorest/jwt/obtain_token/ username=admin password=admin`


**RESPONSE**

```
HTTP/1.0 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Date: Mon, 26 Dec 2016 13:44:10 GMT
Server: WSGIServer/0.2 CPython/3.4.1
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODI3NjAxNTAsInVzZXJuYW1lIjoic2EiLCJlbWFpbCI6InNhQG1lLm9yZyIsInVzZXJfaWQiOjF9.HRP554n01HuGFfq_ZgOAU_8EbDLFNgl5_crC1fQSKk0"
}
```

2. Authorization using obtained JWT
-----------------------------------

**REQUEST**

`http http://localhost:8000/djangorest/jwt/employees/ 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0ODI3NjAxNTAsInVzZXJuYW1lIjoic2EiLCJlbWFpbCI6InNhQG1lLm9yZyIsInVzZXJfaWQiOjF9.HRP554n01HuGFfq_ZgOAU_8EbDLFNgl5_crC1fQSKk0'`

**RESPONSE**

```
HTTP/1.0 200 OK
Allow: GET, POST, OPTIONS
Content-Type: application/json
Date: Mon, 26 Dec 2016 14:03:27 GMT
Server: WSGIServer/0.2 CPython/3.4.1
Vary: Accept
X-Frame-Options: SAMEORIGIN

[
    {
        "company": 1,
        "email": "john@me.org",
        "name": "John updated"
    },
    {
        "company": 1,
        "email": "sds@me.org",
        "name": "New"
    },
    {
        "company": 1,
        "email": "sds@me.org",
        "name": "n1222"
    },
]
```
