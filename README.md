# Expense Tracker API

A REST API for tracking personal expenses, built with FastAPI. This is a web API version of my earlier CLI expense tracker project, rebuilt to learn FastAPI fundamentals.

## Features

- Add new expenses with amount, category, description, and transaction date
- List all expenses, with optional filtering by category
- Delete an expense by ID
- Get a summary of total expenses and breakdown by category

## Installation

1. Clone this repository
    https://github.com/raudhatuls/expense-tracker-api.git
    cd expense-tracker-api
 
2. Create and activate a virtual environment
    python -m venv venv
    venv\Scripts\Activate.ps1 # Windows PowerShell
    
3. Install dependencies
    pip install -r requirements.txt
    
4. Run the server
    uvicorn main:app --reload  
    
5. Open the interactive docs at `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Endpoint                  | Description                              |
|--------|----------------------------|-------------------------------------------|
| POST   | `/add_expense/`            | Add a new expense                        |
| GET    | `/list_expense/`           | List all expenses (optional `?item_category=` filter) |
| DELETE | `/delete_expense/{id}`     | Delete an expense by ID                  |
| GET    | `/summary/`                | Get total and per-category breakdown     |

## Example

**Add an expense:**
```json
POST /add_expense/
{
  "amount": 50000,
  "category": "food",
  "description": "lunch",
  "transaction_date": "2026-09-23"
}
```

**Response:**
```json
{
  "amount": 50000,
  "category": "Food",
  "description": "lunch",
  "transaction_date": "2026-09-23",
  "id": 1,
  "created_at": "2026-09-23"
}
```

## What I learned

- Building a REST API with FastAPI: routing, path parameters, query parameters
- Pydantic models for request validation
- Choosing appropriate HTTP methods (GET/POST/DELETE) and status codes (404 vs 500)
- Consistent error handling across endpoints
- Normalizing data at the point of input rather than at the point of output
- Debugging real issues independently (Pydantic type annotation errors, incorrect HTTP methods in testing, case-sensitivity in filtering)

## Built with

- Python
- FastAPI
- Pydantic