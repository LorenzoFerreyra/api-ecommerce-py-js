# E-Commerce Application

This is a full-stack e-commerce application built with **FastAPI** (backend), **React** (frontend), and **Docker** for containerization. The application is divided into microservices, each handling a specific domain (e.g., User, Product, Category, Order).

## Table of Contents

1. [Features](#features)
2. [Technologies](#technologies)
3. [Project Structure](#project-structure)
4. [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Running with Docker](#running-with-docker)
5. [API Documentation](#api-documentation)
6. [Acknowledgments](#acknowledgments)

---

## Features

-   **User Management**:
    -   Login, and authenticate.
-   **Product Management**:
    -   Browse products, view details, and manage inventory.
-   **Category Management**:
    -   Associate products with categories.
-   **Order Management**:
    -   Place orders and view order history.
-   **API Gateway**:
    -   Single entry point for all microservices.
-   **Frontend**:
    -   Built with React, Vite, and TailwindCSS.

---

## Technologies

-   **Backend**:
    -   FastAPI (Python)
    -   SQLModel (ORM)
    -   MySQL (Database)
-   **Frontend**:
    -   React (JavaScript)
    -   Vite (Build Tool)
    -   TailwindCSS (Styling)
-   **DevOps**:
    -   Docker (Containerization)
    -   Docker Compose (Orchestration)

---

## Project Structure

```
py-ecommerce/
├── api/            # API Gateway service
├── services/
    ├── user/           # User management service
    ├── product/        # Product management service
    ├── category/       # Category management service
    ├── order/          # Order management service
├── frontend/               # React frontend
├── docker-compose.yml      # Docker Compose configuration
```

---

## Setup

### Prerequisites

-   Docker and Docker Compose installed.
-   Node.js and npm installed (for frontend development).

---

### Running with Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ecommerce-app.git
    cd py-ecommerce
    ```

2. Build and start the containers:

    ```bash
    docker-compose up --build
    ```

3. Access the application:
    - Frontend: `http://localhost:5173`
    - API Gateway: `http://localhost:8000`

---

## API Documentation

The API Gateway exposes the following endpoints:

| Endpoint                  | Method | Description               |
| ------------------------- | ------ | ------------------------- |
| `/users/login`            | POST   | Login and get a JWT token |
| `/users/{id}`             | GET    | Get current user details  |
| `/products/`              | GET    | Get all products          |
| `/products/{id}`          | GET    | Get product details       |
| `/products/category/{id}` | GET    | Get products by category  |
| `/products/`              | POST   | Create a product          |
| `/products/stock`         | PATCH  | Update stock              |
| `/products/`              | PATCH  | Update category           |
| `/products/category/{id}` | PATCH  | Delete category           |
| `/categories/`            | GET    | Get all categories        |
| `/categories/{id}`        | GET    | Get category details      |
| `/categories/`            | POST   | Create category           |
| `/categories/{id}`        | PUT    | Update category           |
| `/categories/{id}`        | DELETE | Delete category           |
| `/orders/{id}`            | GET    | Get order details         |
| `/orders/user/{id}`       | GET    | Get user orders list      |
| `/orders/`                | POST   | Create a new order        |

For detailed API documentation, visit the Swagger UI at `http://localhost:8000/docs`.

---

## Acknowledgments

-   [FastAPI](https://fastapi.tiangolo.com/) for the backend framework.
-   [React](https://reactjs.org/) for the frontend library.
-   [Docker](https://www.docker.com/) for containerization.
