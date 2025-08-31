Local Disaster Relief API

A RESTful API built with Django + Django REST Framework + SimpleJWT to manage disaster relief efforts.
It allows users to register, log in, create incidents, list relief items, and request support.

⚡ Authentication Flow

We use JWT (JSON Web Tokens) for authentication.

Register → Create a new user.

Login → Get access & refresh tokens.

Use Access Token → Authenticate API requests.

Refresh Token → Get new access token when expired.

📌 Important: Every protected request must include:

Authorization: Bearer <your-access-token>

🚀 API Endpoints & Testing Guide
1. Register a New User

POST /api/register/

Request body:

{
  "username": "test_user",
  "email": "user@example.com",
  "password": "password123"
  "password2": "password123"
}


Response:

{
  "id": 1,
  "username": "test_user",
  "email": "user@example.com"
}

2. Login (Obtain JWT Tokens)

POST /api/token/

Request body:

{
  "username": "test_user",
  "password": "password123"
}


Response:

{
  "refresh": "long-refresh-token",
  "access": "short-access-token"
}

3. Refresh Access Token

POST /api/token/refresh/

Request body:

{
  "refresh": "long-refresh-token"
}


Response:

{
  "access": "new-access-token"
}

4. List Relief Items (Protected)

GET /api/relief/items/

Headers:

Authorization: Bearer <access-token>


Response (example):

[
  {
    "id": 1,
    "name": "Blanket",
    "description": "Warm blanket for displaced families",
    "quantity": 100
  },
  {
    "id": 2,
    "name": "Rice",
    "description": "50kg bags of rice",
    "quantity": 20
  }
]

5. Create a Relief Item (Admin Only)

POST /api/relief/items/

Headers:

Authorization: Bearer <access-token>


Request body:

{
  "name": "Water Bottles",
  "description": "Clean drinking water",
  "quantity": 200
}


Response:

{
  "id": 3,
  "name": "Water Bottles",
  "description": "Clean drinking water",
  "quantity": 200
}

6. Request a Relief Item (User)

POST /api/relief/requests/

Headers:

Authorization: Bearer <access-token>


Request body:

{
  "item": 1,
  "quantity": 2
}


Response:

{
  "id": 5,
  "item": "Blanket",
  "quantity": 2,
  "status": "Pending",
  "requested_by": "john_doe"
}

7. Report an Incident (User)

POST /api/incidents/

Headers:

Authorization: Bearer <access-token>


Request body:

{
  "title": "Flood in Kano",
  "description": "Heavy rainfall has displaced families.",
  "location": "Kano"
}


Response:

{
  "id": 2,
  "title": "Flood in Kano",
  "description": "Heavy rainfall has displaced families.",
  "location": "Kano",
  "reported_by": "john_doe"
}

✅ Testing Checklist

Register a new user → /api/register/

Login and get tokens → /api/token/

Use access token to:

List relief items → /api/relief/items/

Create a relief request → /api/relief/requests/

Report an incident → /api/incidents/

Refresh token if expired → /api/token/refresh/