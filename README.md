# Docker Compose: Python Backend + Nginx Reverse Proxy

A containerized Python HTTP backend deployed behind an Nginx reverse proxy using Docker Compose.

## Project Overview

This project demonstrates how to deploy a multi-container application using Docker Compose.

The application consists of two services:

- **Backend:** A lightweight Python HTTP server.
- **Nginx:** Reverse proxy that forwards HTTP requests to the Python backend.

Both containers communicate through a custom Docker bridge network.

## Architecture

```text
          Client
            |
            | HTTP :8080
            v
      +-----------+
      |   Nginx   |
      |   :80     |
      +-----------+
            |
            | Docker Network
            | backend:5000
            v
      +-----------+
      |  Python   |
      |  Backend  |
      |   :5000   |
      +-----------+
```

## Technologies

- Docker
- Docker Compose
- Python 3.12
- Nginx (Alpine)
- Docker Bridge Networking
- Docker Healthcheck
- Bind Mounts

## Project Structure

```text
.
├── app/
│   └── app.py
├── nginx/
│   └── default.conf
├── Dockerfile
├── compose.yaml
└── README.md
```

## Features

- Multi-container deployment using Docker Compose.
- Nginx reverse proxy configuration.
- Custom Docker bridge network.
- Backend healthcheck.
- Service dependency management using `depends_on`.
- Automatic container restart policy.
- Nginx configuration mounted using a read-only bind mount.

## Application Endpoints

| Endpoint | Description | Expected Response |
|---|---|---|
| `/` | Backend welcome message | `Hello from Task 11 Backend!` |
| `/health` | Health status check | `OK` |

## Deployment

### 1. Clone the repository

```bash
git clone git@github.com:sur-matevosyan/docker-compose-nginx-python.git
cd docker-compose-nginx-python
```

### 2. Build and start containers

```bash
docker compose up -d --build
```

### 3. Check container status

```bash
docker compose ps
```

### 4. Test the application

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
```

### 5. View logs

```bash
docker compose logs
```

### 6. Stop the application

```bash
docker compose down
```

## Networking

Both services are connected to a custom Docker bridge network named `app-network`.

Nginx communicates with the backend using Docker's internal DNS service discovery:

```text
http://backend:5000
```

The Python backend does not need to publish its port to the host.

## Healthcheck

Docker Compose monitors the backend using an HTTP healthcheck on:

```text
http://localhost:5000/health
```

Nginx starts after the backend reports a healthy status using:

```yaml
depends_on:
  backend:
    condition: service_healthy
```

## Learning Objectives

This project helped practice:

- Containerizing Python applications.
- Configuring Nginx as a reverse proxy.
- Managing multiple services with Docker Compose.
- Configuring Docker networks and internal DNS.
- Implementing container healthchecks.
- Troubleshooting container networking issues.

---

**Author:** Suren Matevosyan  
**GitHub:** [sur-matevosyan](https://github.com/sur-matevosyan)
