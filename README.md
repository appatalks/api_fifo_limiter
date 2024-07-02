# api_fifo_limiter
FIFO API Gateway - for when You can't control your developers


#### Example API Call to the API Gateway.

```bash
$ curl -X POST http://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"headers\": {\"Accept\": \"application/vnd.github+json\", \"Authorization\": \"Bearer <TOKEN>\", \"X-GitHub-Api-Version\": \"2022-11-28\"}, \"url\": \"https://git.example.com/api/v3/user\"}"}'

{
  "status": "success"
}
```

#### Call the record and delivery.

Call ```api_fifo_delivery.sh``` at ```1 CALL``` per run.

```bash
$ bash api_fifo_delivery.sh 

{ "login": "octocat", {more data}  }
```
