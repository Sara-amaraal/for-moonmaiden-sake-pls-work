# Endpoint Manual

## {ENDPOINT NAME} (ex: get_test)
- path: `{PATH}` (ex: api/REQ5/get_test/)
- parameters:
    * parameter1: parameter1 description
    * parameter2: parameter2 description
NOTE: the endpoint might not have parameters. If it doesn't, the section above is not needed.
- method: {METHOD} (ex: GET/POST/PUT)
- user auth: {True/False}

### Request format (This only exists if the endpoint requires a payload)
```
{JSON WITH PAYLOAD}
```

Ex:
```
{
    "id": <int: test_id>
}
```

### Response format
```
{JSON WITH RESPONSE EXAMPLE}
```

Ex:
```
{
    "status": 200, 
    "questions": [
        {
            "id": <int: question1_id>,
            "body": <str: question1_body>,
            "opts": [
                {
                    "id": <int: opt1_id>,
                    "body": <str: opt1_body>
                },
                {
                    "id": <int: opt2_id>,
                    "body": <str: opt2_body>},
                {...},
                {...},
                {...},
                {...}
            ] 
        },
        {
            "id": <int: question2_id>,
            "body": <str: question2_body>
            "opts" : [...]
        }
        {...},
        {...},
        ...
    ]
}
```

### Status Code
Status codes and their meanings. See example.

Ex:
- 400 -> wrong method
- 500 -> invalid credentials (dif in 'log' param)
- 401 -> test not found
- 200 -> success

---
## {ENDPOINT NAME} (Now on repeat for all endpoints on the requirement)
- path: `{PATH}`
.
.
.