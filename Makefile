# BYD90 - Beyond Ninety Makefile
# AI-powered athlete performance platform

.PHONY: help setup install clean dev test lint format build deploy docker-* db-*

# Default target
help: ## Show this help message
	@echo "BYD90 - Beyond Ninety Development Commands"
	@echo "=========================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# =============================================================================
# Setup and Installation
# =============================================================================

setup: ## Initial project setup
	@echo "🚀 Setting up BYD90 development environment..."
	@chmod +x scripts/setup.sh
	@./scripts/setup.sh

install: install-backend install-frontend ## Install all dependencies

install-backend: ## Install backend dependencies
	@echo "📦 Installing backend dependencies..."
	@cd backend && poetry install

install-frontend: ## Install frontend dependencies
	@echo "📦 Installing frontend dependencies..."
	@cd frontend && npm install

update: update-backend update-frontend ## Update all dependencies

update-backend: ## Update backend dependencies
	@echo "🔄 Updating backend dependencies..."
	@cd backend && poetry update

update-frontend: ## Update frontend dependencies
	@echo "🔄 Updating frontend dependencies..."
	@cd frontend && npm update

# =============================================================================
# Development Commands
# =============================================================================

dev: ## Start development servers (both backend and frontend)
	@echo "🚀 Starting development servers..."
	@make -j2 dev-backend dev-frontend

dev-backend: ## Start backend development server
	@echo "🐍 Starting FastAPI backend..."
	@cd backend && poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend: ## Start frontend development server
	@echo "⚛️ Starting React frontend..."
	@cd frontend && npm run dev

dev-backend-debug: ## Start backend with debug mode
	@echo "🐛 Starting FastAPI backend in debug mode..."
	@cd backend && poetry run python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn app.main:app --reload

# =============================================================================
# Docker Commands
# =============================================================================

docker-build: ## Build all Docker images
	@echo "🏗️ Building Docker images..."
	@cd docker && docker-compose build

docker-up: ## Start all services with Docker
	@echo "🐳 Starting all services with Docker..."
	@cd docker && docker-compose up

docker-up-d: ## Start all services with Docker (detached)
	@echo "🐳 Starting all services with Docker (detached)..."
	@cd docker && docker-compose up -d

docker-down: ## Stop all Docker services
	@echo "⏹️ Stopping Docker services..."
	@cd docker && docker-compose down

docker-restart: ## Restart all Docker services
	@echo "🔄 Restarting Docker services..."
	@cd docker && docker-compose restart

docker-logs: ## Show Docker logs
	@echo "📋 Showing Docker logs..."
	@cd docker && docker-compose logs -f

docker-clean: ## Clean Docker containers, networks, and volumes
	@echo "🧹 Cleaning Docker resources..."
	@cd docker && docker-compose down -v --remove-orphans
	@docker system prune -f

# =============================================================================
# Database Commands
# =============================================================================

db-up: ## Start database services only
	@echo "🗄️ Starting database services..."
	@cd docker && docker-compose up -d db redis

db-migrate: ## Run database migrations
	@echo "🔄 Running database migrations..."
	@cd backend && poetry run alembic upgrade head

db-migration: ## Create a new database migration
	@echo "📝 Creating new database migration..."
	@read -p "Migration message: " msg; \
	cd backend && poetry run alembic revision --autogenerate -m "$$msg"

db-reset: ## Reset database (WARNING: This will delete all data)
	@echo "⚠️ Resetting database..."
	@cd docker && docker-compose down db
	@docker volume rm docker_postgres_data 2>/dev/null || true
	@cd docker && docker-compose up -d db
	@sleep 5
	@make db-migrate

db-shell: ## Connect to database shell
	@echo "🐘 Connecting to PostgreSQL..."
	@cd docker && docker-compose exec db psql -U byd90_user -d byd90_db

db-backup: ## Backup database
	@echo "💾 Creating database backup..."
	@mkdir -p backups
	@cd docker && docker-compose exec db pg_dump -U byd90_user byd90_db > ../backups/backup_$(shell date +%Y%m%d_%H%M%S).sql

# =============================================================================
# Testing Commands
# =============================================================================

test: test-backend test-frontend ## Run all tests

test-backend: ## Run backend tests
	@echo "🧪 Running backend tests..."
	@cd backend && poetry run pytest -v

test-frontend: ## Run frontend tests
	@echo "🧪 Running frontend tests..."
	@cd frontend && npm run test

test-coverage: ## Run tests with coverage
	@echo "📊 Running tests with coverage..."
	@cd backend && poetry run pytest --cov=app --cov-report=html
	@cd frontend && npm run test:coverage

test-watch: ## Run tests in watch mode
	@echo "👀 Running tests in watch mode..."
	@make -j2 test-backend-watch test-frontend-watch

test-backend-watch: ## Run backend tests in watch mode
	@cd backend && poetry run pytest-watch

test-frontend-watch: ## Run frontend tests in watch mode
	@cd frontend && npm run test:watch

# =============================================================================
# Code Quality Commands
# =============================================================================

lint: lint-backend lint-frontend ## Run all linters

lint-backend: ## Run backend linting
	@echo "🔍 Running backend linting..."
	@cd backend && poetry run flake8 app/
	@cd backend && poetry run mypy app/

lint-frontend: ## Run frontend linting
	@echo "🔍 Running frontend linting..."
	@cd frontend && npm run lint

format: format-backend format-frontend ## Format all code

format-backend: ## Format backend code
	@echo "✨ Formatting backend code..."
	@cd backend && poetry run black app/
	@cd backend && poetry run isort app/

format-frontend: ## Format frontend code
	@echo "✨ Formatting frontend code..."
	@cd frontend && npm run lint:fix
	@cd frontend && npx prettier --write src/

check: ## Run all code quality checks
	@echo "✅ Running all code quality checks..."
	@make lint
	@make test

# =============================================================================
# Build Commands
# =============================================================================

build: build-backend build-frontend ## Build all applications

build-backend: ## Build backend for production
	@echo "🏗️ Building backend..."
	@cd backend && poetry build

build-frontend: ## Build frontend for production
	@echo "🏗️ Building frontend..."
	@cd frontend && npm run build

build-docker: ## Build production Docker images
	@echo "🐳 Building production Docker images..."
	@docker build -f docker/Dockerfile.backend -t byd90-backend:latest backend/
	@docker build -f docker/Dockerfile.frontend -t byd90-frontend:latest frontend/

# =============================================================================
# Deployment Commands
# =============================================================================

deploy-staging: ## Deploy to staging environment
	@echo "🚀 Deploying to staging..."
	@echo "Staging deployment not yet configured"

deploy-production: ## Deploy to production environment
	@echo "🚀 Deploying to production..."
	@echo "Production deployment not yet configured"

# =============================================================================
# Development Utilities
# =============================================================================

logs: ## Show application logs
	@echo "📋 Showing application logs..."
	@cd docker && docker-compose logs -f backend frontend

logs-backend: ## Show backend logs only
	@cd docker && docker-compose logs -f backend

logs-frontend: ## Show frontend logs only
	@cd docker && docker-compose logs -f frontend

shell-backend: ## Open backend shell
	@echo "🐍 Opening backend shell..."
	@cd backend && poetry shell

shell-db: ## Open database shell
	@make db-shell

# =============================================================================
# AI/ML Commands
# =============================================================================

ai-setup: ## Setup AI/ML dependencies
	@echo "🤖 Setting up AI/ML dependencies..."
	@cd backend && poetry add openai scikit-learn pandas numpy

ai-test: ## Test AI recommendations
	@echo "🧠 Testing AI recommendations..."
	@cd backend && poetry run python -c "from app.services.ai_service import test_recommendations; test_recommendations()"

# =============================================================================
# Security Commands
# =============================================================================

security-check: ## Run security checks
	@echo "🔒 Running security checks..."
	@cd backend && poetry run safety check
	@cd frontend && npm audit

security-fix: ## Fix security vulnerabilities
	@echo "🔧 Fixing security vulnerabilities..."
	@cd frontend && npm audit fix

# =============================================================================
# Cleanup Commands
# =============================================================================

clean: clean-backend clean-frontend clean-docker ## Clean all build artifacts and caches

clean-backend: ## Clean backend artifacts
	@echo "🧹 Cleaning backend artifacts..."
	@cd backend && rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage htmlcov/
	@find backend -type d -name __pycache__ -exec rm -rf {} +
	@find backend -type f -name "*.pyc" -delete

clean-frontend: ## Clean frontend artifacts
	@echo "🧹 Cleaning frontend artifacts..."
	@cd frontend && rm -rf dist/ build/ node_modules/.cache/
	@cd frontend && npm run clean 2>/dev/null || true

clean-docker: ## Clean Docker artifacts
	@echo "🧹 Cleaning Docker artifacts..."
	@docker system prune -f
	@docker volume prune -f

clean-all: clean docker-clean ## Clean everything including Docker volumes
	@echo "🧹 Cleaning everything..."

# =============================================================================
# Environment Management
# =============================================================================

env-copy: ## Copy environment template files
	@echo "📝 Copying environment files..."
	@cp env.example .env 2>/dev/null || true
	@cp env.example backend/.env 2>/dev/null || true
	@echo "VITE_API_BASE_URL=http://localhost:8000" > frontend/.env

env-check: ## Check environment variables
	@echo "🔍 Checking environment variables..."
	@cd backend && poetry run python -c "from app.core.config import settings; print('✅ Backend config loaded successfully')"

# =============================================================================
# Documentation Commands
# =============================================================================

docs: ## Generate documentation
	@echo "📚 Generating documentation..."
	@echo "Documentation generation not yet configured"

docs-serve: ## Serve documentation locally
	@echo "📖 Serving documentation..."
	@echo "Documentation server not yet configured"

# =============================================================================
# Performance Commands
# =============================================================================

perf-test: ## Run performance tests
	@echo "⚡ Running performance tests..."
	@echo "Performance tests not yet configured"

load-test: ## Run load tests
	@echo "📈 Running load tests..."
	@echo "Load tests not yet configured"

# =============================================================================
# Monitoring Commands
# =============================================================================

health-check: ## Check application health
	@echo "🏥 Checking application health..."
	@curl -s http://localhost:8000/health || echo "❌ Backend not responding"
	@curl -s http://localhost:3000 > /dev/null && echo "✅ Frontend responding" || echo "❌ Frontend not responding"

status: ## Show service status
	@echo "📊 Service Status:"
	@echo "=================="
	@cd docker && docker-compose ps

# =============================================================================
# Quick Commands
# =============================================================================

quick-start: env-copy docker-up ## Quick start for new developers
	@echo "🚀 BYD90 is starting up!"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

restart: docker-down docker-up ## Quick restart of all services

# =============================================================================
# Version Management
# =============================================================================

version: ## Show current version
	@echo "📋 BYD90 Version Information:"
	@echo "============================"
	@echo "Backend:"
	@cd backend && poetry version
	@echo "Frontend:"
	@cd frontend && node -pe "require('./package.json').version"

bump-version: ## Bump version (specify VERSION=patch|minor|major)
	@echo "📈 Bumping version..."
	@cd backend && poetry version $(VERSION)
	@cd frontend && npm version $(VERSION)

# Default target when no argument is provided
.DEFAULT_GOAL := help
