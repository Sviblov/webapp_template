#Template for webapp

Technology stack: 
Frontend: ReactJS+Typescript
Backend: FastAPI
DB: Postgres
reverse-proxy: nginx

Fast start:

1) Clone repository
2) create .env files by copying .env.example
3) upload ssl certificate to /ngingx/ssl/key.pem and /nginx/ssl/cert.pem

backend:
3) create python virtual environment virtualenv venv
4) pip install -r backend/requirements.txt

frontend:
5) in folder frontend run: npm install


to start dev: 
./start_dev.sh

to put everything in docker: 
./deploy_prod.sh