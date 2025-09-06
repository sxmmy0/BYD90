# BYD90 - Beyond Ninety

> AI-powered athlete performance platform connecting athletes with coaches and providing personalized training recommendations.

![BYD90 Logo](https://via.placeholder.com/200x80/0ea5e9/ffffff?text=BYD90)

## 🌟 Features

- **AI-Powered Recommendations** - Personalized training suggestions based on sport, position, and performance data
- **Coach-Athlete Connection** - Platform for coaches to connect and train athletes
- **Position-Specific Training** - Tailored workouts and drills for specific sports positions
- **Performance Analytics** - Detailed tracking and insights into athletic progress
- **Community Features** - Connect with other athletes and share your journey
- **Customizable Avatars** - Personalized avatars with sports gear and achievements
- **Multi-Sport Support** - Support for football, basketball, soccer, tennis, and more

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **FastAPI** - Modern, fast web framework
- **PostgreSQL** - Primary database
- **Redis** - Caching and session storage
- **SQLAlchemy** - ORM for database operations
- **JWT Authentication** - Secure user authentication
- **AI Integration** - OpenAI API for recommendations

### Frontend (React + TypeScript)
- **React 18** - Modern React with hooks
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool and dev server
- **Tailwind CSS + Sass** - Styling framework
- **Zustand** - State management
- **React Query** - Server state management
- **Framer Motion** - Animations and transitions

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** (recommended)
- **Node.js 18+** (for local development)
- **Python 3.11+** (for local development)
- **Poetry** (Python package manager)

### Option 1: Docker Setup (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd BYD90

# Run the setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Start all services
cd docker
docker-compose up
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database Admin**: http://localhost:5050 (admin@byd90.com / admin123)

### Option 2: Local Development

#### Backend Setup

```bash
cd backend

# Install dependencies
poetry install

# Copy environment file
cp ../env.example .env

# Start PostgreSQL and Redis (via Docker)
cd ../docker
docker-compose up -d db redis

# Run database migrations (setup Alembic first)
cd ../backend
poetry run alembic upgrade head

# Start the development server
poetry run uvicorn app.main:app --reload
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## 📁 Project Structure

```
BYD90/
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── api/             # API routes
│   │   ├── core/            # Core functionality
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic
│   │   └── main.py          # FastAPI app
│   ├── tests/               # Backend tests
│   └── pyproject.toml       # Python dependencies
├── frontend/                # React frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # API services
│   │   ├── store/           # State management
│   │   ├── styles/          # CSS/Sass styles
│   │   └── types/           # TypeScript types
│   └── package.json         # Frontend dependencies
├── docker/                  # Docker configuration
├── docs/                    # Documentation
└── scripts/                 # Development scripts
```

## 🎯 User Types

### Athletes
- Create personalized profiles with sport and position
- Receive AI-powered training recommendations
- Track performance metrics and progress
- Connect with certified coaches
- Join sport-specific communities
- Customize avatars and earn achievements

### Coaches
- Create professional coaching profiles
- Connect with and train athletes
- Provide feedback on training progress
- Access athlete performance data
- Manage training programs
- Build coaching reputation through reviews

## 🔧 Development

### Environment Variables

Copy `env.example` to `.env` and configure:

```env
# Database
POSTGRES_SERVER=localhost
POSTGRES_USER=byd90_user
POSTGRES_PASSWORD=byd90_password
POSTGRES_DB=byd90_db

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT
SECRET_KEY=your-secret-key

# AI APIs
OPENAI_API_KEY=your-openai-key
```

### Database Schema

The application uses the following main models:
- **Users** - Base user authentication and profile
- **Athletes** - Athlete-specific data and metrics
- **Coaches** - Coach profiles and certifications
- **Recommendations** - AI-generated training suggestions
- **Communities** - Social groups and discussions
- **Avatars** - Customizable user avatars

### API Endpoints

Key API endpoints include:

- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Current user info
- `GET /api/v1/recommendations` - Get AI recommendations
- `GET /api/v1/communities` - List communities
- `POST /api/v1/athletes/profile` - Update athlete profile

Full API documentation is available at `/docs` when running the backend.

## 🧪 Testing

### Backend Tests
```bash
cd backend
poetry run pytest
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## 🚀 Deployment

### Production Build

```bash
# Build frontend
cd frontend
npm run build

# Build backend Docker image
cd ../backend
docker build -t byd90-backend .

# Deploy using Docker Compose
cd ../docker
docker-compose -f docker-compose.prod.yml up -d
```

### Environment Setup

For production, ensure you have:
- PostgreSQL database
- Redis instance
- Secure JWT secret key
- Valid SSL certificates
- OpenAI API key (for AI features)
- Configured email service (for notifications)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript/Python best practices
- Write tests for new features
- Update documentation as needed
- Use conventional commit messages
- Ensure code passes linting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastAPI** - Modern Python web framework
- **React** - UI library
- **Tailwind CSS** - Utility-first CSS framework
- **OpenAI** - AI recommendation engine
- **Lucide React** - Beautiful icon set

## 📞 Support

For support and questions:
- 📧 Email: support@byd90.com
- 💬 Discord: [BYD90 Community](https://discord.gg/byd90)
- 📖 Documentation: [docs.byd90.com](https://docs.byd90.com)

---

**BYD90** - Beyond Ninety. Beyond Limits. 🚀
