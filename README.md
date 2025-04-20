# PROG8850 - Final Assignment

## ✅ Project Overview

This final assignment demonstrates an integrated DevOps and Microservices project using:

- **FastAPI** as the Microservice (Microfrontend)
- **MySQL** for student data storage
- **Docker & Docker Compose** for containerization
- **ngrok** to expose the local API
- **Adminer** and **WordPress** as sample additional containers
- **SigNoz** for observability and monitoring of containers

---

## 📦 Folder Structure


---

## 🚀 How to Run

```bash
docker compose up -d --build
This will start all containers including FastAPI on port 8080, MySQL, Adminer, WordPress, and SigNoz.
Microfrontend API
Once running, visit:

Local: http://127.0.0.1:8080

Ngrok: (check your ngrok terminal output)

Test endpoints:
GET /students – shows all student records

GET / – returns: {"message": "Microfrontend is working!"}

MySQL Student Data
USE students;

INSERT INTO students (id, name, email, course) VALUES
(8933095, 'Hemapriya Saravanan', 'hema@example.com', 'Cloud Computing'),
(8986873, 'Padmini', 'padmini@example.com', 'Data Engineering'),
(8981900, 'Ankith', 'ankith@example.com', 'AWS'),
(8986104, 'Yamini', 'yamini@example.com', 'DevOps');
Monitoring
SigNoz is running and connected. It captures container metrics.

Navigate to SigNoz dashboard: http://localhost:3301

Preconfigured for collecting OTEL traces and logs

Final Status
Docker containers: ✅ All started successfully

Student data: ✅ Inserted and visible via /students

Ngrok: ✅ URL exposed and tested

GitHub: ✅ Final push completed
