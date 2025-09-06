#!/bin/bash

# BYD90 Development Setup Script

echo "🚀 Setting up BYD90 development environment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "✅ Created .env file. Please update it with your configuration."
fi

# Create backend .env file
if [ ! -f backend/.env ]; then
    echo "📝 Creating backend .env file..."
    cp env.example backend/.env
fi

# Frontend environment file
if [ ! -f frontend/.env ]; then
    echo "📝 Creating frontend .env file..."
    cat > frontend/.env << EOL
VITE_API_BASE_URL=http://localhost:8000
EOL
fi

# Build and start services
echo "🏗️ Building Docker containers..."
cd docker && docker-compose build

echo "🚀 Starting services..."
docker-compose up -d db redis

echo "⏳ Waiting for database to be ready..."
sleep 10

echo "📦 Installing backend dependencies..."
cd ../backend && poetry install

echo "🗄️ Running database migrations..."
# You would run Alembic migrations here
echo "Note: Set up Alembic migrations manually"

echo "📦 Installing frontend dependencies..."
cd ../frontend && npm install

echo "✅ Setup complete! You can now start the development servers:"
echo ""
echo "Backend: cd backend && poetry run uvicorn app.main:app --reload"
echo "Frontend: cd frontend && npm run dev"
echo ""
echo "Or use Docker:"
echo "cd docker && docker-compose up"
echo ""
echo "🎉 Happy coding!"
