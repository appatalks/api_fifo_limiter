## FIFO API Gateway Server

> [!NOTE]
> #### This project is independently maintained and is not supported by GitHub.

### Overview
A simple FIFO API Gateway for managing API calls, storing them in MySQL, and processing in order.

### Prerequisites
- ```Python 3.x```, ```Flask```, ```MySQL```, ```pip```

### Setup
1. Clone Repository:
   ```bash
   git clone https://github.com/your-repo/api_fifo_limiter.git
   cd api_fifo_limiter
   ```

2. Install Dependencies:
   ```bash
   pip install flask mysql-connector-python
   ```
   
3. Initialize MySQL Database:
   ```bash
   python fifo_init.py
   ```

### Usage

- Start Server
  ```bash
  python api_fifo_server.py
  ```
- Direct API to Server Endpoint
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "example data"}'
  ```
- Retrieve from MySQL and Delete Data;
  ```bash
  curl -k -X GET https://127.0.0.1:5000/api/deliver
  ```

(Remeber to use Valid Certificates, otherwise accept self-signed as valid with ```curl -k``` flag)

### Example: GitHub API Integration

- Save GitHub API Call:
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"headers\": {\"Accept\": \"application/vnd.github+json\", \"Authorization\": \"Bearer 
  <TOKEN>\", \"X-GitHub-Api-Version\": \"2022-11-28\"}, \"url\": \"https://git.example.com/api/v3/user\"}"}'
  {"status": "success"}
  ```

- Retrieve GitHub API Call:
  ```bash
  bash api_fifo_delivery.sh
  { "login": "octocat", "id": 10, ... }
  ```

### Example: OpenAI API Integration

- Save OpenAI API Call
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"openai_token\": \"<OPENAI_API_KEY>\", \"data\": {\"model\": \"gpt-4\", \"messages\": 
  [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"Hello!\"}]}}"}'
  {"status":"success"}
  ```

  - Retrieve GitHub API Call:
  ```bash
  bash api_fifo_delivery_gpt.sh 
  { "id": "c***", "object": "chat.completion", "created": 1***, "model": "gpt-4-0613", "choices": [ { "index": 0, "message": { "role": "assistant", 
  "content": "Hello! How can I assist you today?" } ... }
  ```

