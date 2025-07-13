# 🚀 WebApp Template (React + FastAPI + PostgreSQL)

A fullstack web application starter template with user authentication and modern development stack.

---

## 🧱 Tech Stack

- **Frontend**: ReactJS + TypeScript  
- **Backend**: FastAPI  
- **Database**: PostgreSQL  
- **Reverse Proxy**: Nginx  
- **DevOps**: Docker + shell scripts

---

## ⚡ Quick Start (Development)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create `.env` files

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

Be sure to fill in necessary variables like `DATABASE_URL`, `SECRET_KEY`, and `VITE_API_URL`.

---

## 🔐 SSL Setup (for Nginx)

Place your SSL certificates in the `nginx/ssl/` directory:

```text
nginx/ssl/key.pem     # private key
nginx/ssl/cert.pem    # public certificate
```

---

## 🐍 Backend Setup

### 3. Create a Python virtual environment and install dependencies

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚛️ Frontend Setup

### 4. Install Node dependencies

```bash
cd frontend
npm install
```

---

## 🧪 Run in Development Mode

```bash
./start_dev.sh
```

- Runs frontend, backend, and database using local `.env` files.
- Hot reload enabled.

---

## 🐳 Deploy with Docker (Production)

```bash
./deploy_prod.sh
```

- Builds and starts everything in Docker containers.
- Application will be available via HTTPS through Nginx reverse proxy.

---

## 📁 Project Structure

```
.
├── backend/         # FastAPI application
├── frontend/        # React application
├── nginx/           # Nginx config and SSL certs
├── docker-compose.yml
├── start_dev.sh
└── deploy_prod.sh
```

---

## 🧾 License

MIT — free to use and modify, just keep attribution.