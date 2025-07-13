#!/bin/bash
git pull
# Остановить и удалить старые контейнеры, если они есть
docker stop mpnn-backend mpnn-frontend mpnn-nginx 2>/dev/null || true
docker rm mpnn-backend mpnn-frontend mpnn-nginx 2>/dev/null || true

# Создать сеть, если не существует
docker network inspect easympnn-net >/dev/null 2>&1 || docker network create easympnn-net

# Backend
cd backend
docker build -t mpnn-backend .
docker run -d --name mpnn-backend --network easympnn-net --env-file .env mpnn-backend
cd ..

# Frontend
cd frontend
docker build -t mpnn-frontend .
docker run -d --name mpnn-frontend --network easympnn-net mpnn-frontend
cd ..

# Nginx
cd nginx
docker build -t mpnn-nginx .
docker run -d --name mpnn-nginx --network easympnn-net  -p 443:443 mpnn-nginx
cd ..