#!/bin/bash

# Library Management System Development Startup Script

echo "🚀 Starting Library Management System in development mode..."

# Activate virtual environment
source venv/bin/activate

# Start Django development server
echo "🐍 Starting Django server..."
python manage.py runserver &
DJANGO_PID=$!

# Wait a moment for Django to start
sleep 3

# Start Vue.js development server
echo "⚡ Starting Vue.js frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "✅ Development servers started!"
echo ""
echo "🌐 Access points:"
echo "- Django Admin: http://localhost:8000/admin/"
echo "- API Root: http://localhost:8000/api/"
echo "- Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for user to stop
trap "echo '🛑 Stopping servers...'; kill $DJANGO_PID $FRONTEND_PID; exit" INT
wait
