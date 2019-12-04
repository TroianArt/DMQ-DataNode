# Data node

## Key features
   * Create/delete queues
   * Store message in queue
   * Return message from queue
   * Return statistics

## API documentation

* ### Create queue
	***
	#### Endpoint:
	`http://{data-node-url}:{data-node-port}/queues`
	#### Protocol:
	`POST`
	#### Body:
	```json
	{
	    "name": "{queue-name}"
	}
	```

	#### Request example:
	```sh
	curl -v -X POST https://127.0.0.1:5000/queues \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d '{
	        "name": "queue1"
	    }'
	```

	#### Response example:

	`HTTP/ 1.1 201 Created`

	```json
	{
	    "id": "1234",
	    "name": "queue1"
	}
	```

* ### Delete queue
	***
	#### Endpoint:
	`http://{data-node-url}:{data-node-port}/queues/{queue-id}/`
	#### Protocol:
	`DELETE`
	#### Body:
	```json
	```

	#### Request example:
	```sh
	curl -v -X DELETE https://127.0.0.1:5000/queues/0001/
	```

	#### Response example:
	`HTTP/ 1.1 200 OK`

* ### Store message
	***
	#### Endpoint:
	`http://{data-node-url}:{data-node-port}/queues/{queue-id}/message/`
	#### Protocol:
	`POST`
	#### Body:
	```json
	{
	    "key": "{message key}",
	    "value": "{message body}"
	}
	```

	#### Request example:
	```sh
	curl -v -X POST https://127.0.0.1:5000/queues/0001/message/ \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d '{
	        "key": "foo",
	        "value": {
	            "spam": "eggs"
	        }
	    }'
	```

	#### Response example:
	`HTTP/ 1.1 201 Created`

* ## Get message

	#### Endpoint:
	``` http://{data-node-url}:{data-node-port}/queues/{queue-id}/message/ ```
	#### Protocol:
	` GET `
	#### Body:
	```json
	```

	#### Request example:

	```sh
	curl -v -X GET https://127.0.0.1:5000/queues/0001/message/ \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d ''
	```

	#### Response example:
	```json
	{
	    "key": "foo",
	    "value": {
	        "spam": "eggs"
	    }
	}
	```

* ## Get statistics
	#### Endpoint:
	` http://{data-node-url}:{data-node-port}/statistics/ `
	#### Protocol:
	` GET `
	#### Body:
	```json
	```

	#### Request example:

	```sh
	curl -v -X GET https://127.0.0.1:5000/statistics/ \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d ''
	```

	#### Response example:
	```json
	{
		"cpu_load_percent": 10,
	    "queues": [
	        {
	            "id": "0001",
	            "name": "queue1",
	            "size": 3
	        },
	        {
	            "id": "0002",
	            "name": "queue2",
	            "size": 4
	        }
	    ]
	}
	```