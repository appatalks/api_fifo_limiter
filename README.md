# api_fifo_limiter
FIFO API Gateway


#### API Call to the API Gateway.

```bash
curl -X POST http://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "example data"}'
```

#### Retrieve and Delete Data (FIFO)

```bash
curl -X GET http://127.0.0.1:5000/api/deliver
```
----

#### Example call to GitHub API Endpoint

```bash
$ curl -X POST http://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"headers\": {\"Accept\": \"application/vnd.github+json\", \"Authorization\": \"Bearer <TOKEN>\", \"X-GitHub-Api-Version\": \"2022-11-28\"}, \"url\": \"https://git.example.com/api/v3/user\"}"}'

{
  "status": "success"
}
```

#### Retrieve the GitHub API call and delivery via script.

Call ```api_fifo_delivery.sh``` at ```1 CALL``` per run.

```bash
$ bash api_fifo_delivery.sh 

{ "login": "octocat", {more data}  }
```
