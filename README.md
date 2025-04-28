# MasterChef AI Bot - Django Recipe Assistant

![ai output](https://github.com/user-attachments/assets/0c5de8fa-cabb-491e-b0ce-de44fbc8091c)

## Project Overview
MasterChef AI Bot is an intelligent recipe assistant powered by Django and AI APIs that:
- Generates recipes based on user queries
- Provides step-by-step cooking instructions
- Offers quick meal solutions
- Adapts recipes based on available ingredients/time constraints

## Key Features

### AI-Powered Recipe Generation
- Natural language processing for recipe requests
- Context-aware recipe suggestions
- Time-sensitive meal planning (e.g., "5-minute pizza")
- Ingredient substitution recommendations

### Interactive Interface
- Clean, user-friendly chat interface
- Thought process visualization (as shown in screenshots)
- Quick query submission
- Responsive design for all devices

### Smart Cooking Assistance
- Step-by-step breakdowns
- Cooking time estimations
- Equipment recommendations
- Dietary adaptation suggestions

## Demo Screenshots

### Home Page
![home page](https://github.com/user-attachments/assets/e805bb74-ff6c-4fef-bde7-a4a6575ac478)

### Recipe Query
![asking recipe](https://github.com/user-attachments/assets/35ea7253-b829-4f69-a22a-3ff8da025521)

### AI Thought Process
![ai output](https://github.com/user-attachments/assets/f27b6885-274a-47e6-be04-b4452166113a)

## Technology Stack

### Core Components
- **Backend**: Django 4.2
- **AI Integration**: OpenAI API (or similar LLM service)
- **Database**: PostgreSQL
- **Authentication**: Django Allauth

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 5
- AJAX for dynamic updates
- Responsive design

### APIs
- External recipe APIs (optional)
- Nutrition data APIs (future)
- Image generation APIs (future)

## Installation Guide

### Prerequisites
- Python 3.10+
- Django 4.2+
- OpenAI API key
- PostgreSQL

### Setup Instructions
1. Clone repository:
   ```bash
   git clone "repository url"
   cd masterchef-ai
   ```

2. Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key and database credentials
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

7. Access at `http://localhost:8000`

## API Documentation

### Core Endpoints
```
POST /api/recipes/generate/
Params: {query: "5 minute pizza", constraints: "vegetarian"}
Returns: Generated recipe with steps

GET /api/recipes/history/
Returns: User's recipe query history
```

### Authentication Endpoints
```
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
```

## Usage Examples

1. **Quick Meal Request**:
   ```
   "Give me a 15-minute pasta recipe"
   ```

2. **Ingredient-Based Query**:
   ```
   "What can I make with chicken, tomatoes, and rice?"
   ```

3. **Dietary-Specific Request**:
   ```
   "Vegan dessert recipe under 30 minutes"
   ```

4. **Technique Inquiry**:
   ```
   "How to properly knead pizza dough?"
   ```

## Future Enhancements
- Voice command integration
- Meal planning calendar
- Grocery list generator
- Cooking timer integration
- User recipe saving system
- Image generation for recipes

