#!/bin/bash
for port in 4000 8000; do
  PID=$(lsof -ti tcp:$port)
  if [ -n "$PID" ]; then
    echo "Killing process on port $port (PID $PID)"
    kill -9 $PID
  fi
done
# Запуск frontend
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Запуск backend
cd backend
python3 main.py &
BACKEND_PID=$!
cd ..

# Ожидание завершения обоих процессов
wait $FRONTEND_PID $BACKEND_PID