# Production-Grade Reading Platform API

 **production-ready, event-driven FastAPI backend** for tracking reading activity, built with **authentication, async processing, caching, migrations, observability, and testing**.

This project evolves a simple reading tracker into a **scalable, multi-user backend service**, following real-world backend architecture practices.

# Features

# Authentication & Authorization
- JWT-based authentication
- Secure password hashing (bcrypt + passlib)
- Protected routes using dependency-based guards
- Per-user data isolation (users can only access their own books)

# Async FastAPI Backend
- Fully asynchronous FastAPI application
- Async SQLAlchemy ORM
- Async-ready background job architecture

# Database & Migrations
- Relational schema with:
  - Users
  - Books
  - Reading Sessions
- SQLAlchemy ORM
- Alembic migrations (initial + schema evolution ready)
- SQLite for local development (PostgreSQL-ready)

# Analytics & Derived Data
- `/stats` endpoint providing:
  - Total books
  - Completed books
  - Reading streak
  - Average pages per day
  - Most-read author

# Caching Strategy
- Cache abstraction layer
- Redis support (production)
- In-memory async fallback (local development / Python 3.13 compatibility)
- Automatic cache invalidation on writes

# Observability
- Structured logging
- Centralized error handling
- Clean exception hierarchy
- SQL query visibility during development

# Testing (Design-Ready)
- Pytest + async test support
- Auth flow tests
- Protected route tests
- Cache behavior tests
- ≥80% coverage target





