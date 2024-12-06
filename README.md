# Telegram Mini App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Telegram Mini App built with React (Frontend) and Flask (Backend).

## Project Structure

```
frontend/    # React TypeScript application
├── src/     # Source code
├── public/  # Static files
└── ...      # Configuration files

backend/     # Flask Python application
├── app.py   # Main application file
└── ...      # Python backend files
```

## Features

- TypeScript + React frontend
- Flask Python backend
- Docker support
- Telegram Web App SDK integration
- Tailwind CSS styling
- CI/CD with GitHub Actions

## Prerequisites

- Node.js 18+
- Python 3.9+
- Docker and Docker Compose (optional)

## Environment Variables

Copy `.env.example` to `.env` and update the values:

### Frontend
```env
REACT_APP_BACKEND_URL=http://localhost:5000
REACT_APP_TELEGRAM_BOT_USERNAME=your_bot_username
```

### Backend
```env
BOT_TOKEN=your_bot_token
ALLOWED_ORIGINS=http://localhost:3000
```

## Development

### Using Docker Compose
```bash
# Start all services
docker-compose up

# Rebuild and start
docker-compose up --build
```

### Manual Setup

Frontend:
```bash
cd frontend
npm install
npm start
```

Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python app.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
