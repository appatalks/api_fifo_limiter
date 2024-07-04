> [!WARNING]
> WORK IN PROGRESS; В РОБОТІ

- [ ] SSL

#### Install

1. Create a ```MySQL``` **User** and **Database** on external ```MySQL 8``` or better.
   ```mysql
   CREATE DATABASE IF NOT EXISTS api_gateway_fifo;
   CREATE USER IF NOT EXISTS 'api_gateway'@'%' IDENTIFIED BY 'your_mysql_password';
   GRANT ALL PRIVILEGES ON api_gateway_fifo.* TO 'api_gateway'@'%';
   FLUSH PRIVILEGES;
   ```

2. Clone Repository
   ```bash
   git clone https://github.com/your-repo/api_fifo_limiter.git
   cd api_fifo_limiter/docker
   ```

3. Adjust ```DB_HOST``` and ```DB_PASSWORD``` accordingly in the following files:
   - fifo_init.py
   - api_fifo_server.py
   - docker-compose.yml

#### Usage:

1. Start Server
   ```bash
   docker-compose up --build
   ```

2. Direct API to Server Endpoint
   ```bash
   curl -X POST http://localhost:8000/api/save -H "Content-Type: application/json" -d '{"data": "example data"}'
   {"status":"success"}
   ```

3. Retrieve from MySQL and Delete Data;
   ```bash
   curl -X GET http://localhost:8000/api/deliver
   {"data":"example data"}
   ```

