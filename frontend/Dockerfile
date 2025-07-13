FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps && npm install --save-dev @types/node
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html