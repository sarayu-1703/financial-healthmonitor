# Financial Health Monitor

AI-powered Financial Health Monitoring system built using FastAPI, React, Vite, Agno multi-agent workflows, Neon PostgreSQL, and Gemini API.

This application analyzes financial transaction and budget data and generates intelligent financial health insights using multiple AI agents working together in a workflow-based architecture.

# Features

Multi-agent financial analysis system

Budget monitoring and overspending detection

Expense concentration analysis

Spending trend analysis

Conditional workflow branching

Session-based conversational memory

Neon PostgreSQL-backed persistence

FastAPI backend APIs

React frontend dashboard interface

Financial health scoring (Green / Amber / Red)

# Tech Stack

## Backend

Python

FastAPI

Agno

Neon PostgreSQL

SQLAlchemy

Pydantic

## Frontend

React

Vite

CSS

## AI Integration

Gemini API

# Multi-Agent Architecture

| Agent | Responsibility |
|---|---|
| Budget Agent | Detects overspending against budget |
| Trend Agent | Analyzes spending patterns |
| Concentration Agent | Identifies risky spending concentration |
| Recommendation Agent | Generates financial recommendations |
| Coordinator Agent | Combines outputs into final report |

# Workflow Overview

1. User asks a financial health question

2. Workflow retrieves transaction and budget data

3. Multiple AI agents analyze the data independently

4. Conditional workflow logic determines financial risk status

5. Final report is generated

6. Session history is stored in Neon PostgreSQL

# Project Structure

```bash
financial-health-monitor/
│
├── backend/
│   ├── agents/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── config.py
│   └── main.py
│
├── data/
│   ├── generate_data.py
│   ├── seed.sql
│   └── transactions.sql
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

# Backend Explanation

The backend is built using FastAPI.

`main.py` initializes the FastAPI server

`config.py` manages environment variables and API configuration

`agents/` contains all AI agents used in the workflow

`routes/` contains API endpoints

`schemas/` contains structured request and response models

`services/` contains business logic and workflow processing

`tools/` contains reusable helper utilities

# Frontend Explanation

The frontend is built using React and Vite.

`src/` contains the main frontend code, pages, components, and API integration logic

`public/` contains static assets

`package.json` manages frontend dependencies and scripts

`vite.config.js` contains Vite configuration

# Database

The application uses Neon serverless PostgreSQL as the cloud database.

The database stores:

financial transactions

budgets

financial reports

session history

# AI Integration

Gemini API is used for:

financial reasoning

report generation

multi-agent analysis

recommendation generation

# Conditional Workflow Execution

The application supports conditional workflow branching.

## Green Report

Healthy spending behavior

Budget within limits

Remediation workflow skipped

## Amber / Red Report

Overspending detected

Risk concentration identified

Remediation workflow triggered automatically

# Running the Backend

```bash
uvicorn main:app --reload
```

Backend API:

```bash
http://localhost:8000
```

Swagger Documentation:

```bash
http://localhost:8000/docs
```

# Running the Frontend

```bash
npm install
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

# Example Queries

```text
How is my financial health for February?
```

```text
How is my financial health for April?
```

# Demo Video

https://youtu.be/iaKTYuQBkfs?si=OkqFWrmIJ0UK1Xtc

# Assignment Requirements Covered

Multi-agent workflow implementation

Conditional workflow execution

Green report generation

Amber/Red report generation

Backend API integration

Structured financial analysis

Session persistence

End-to-end working demo

README documentation

Demo video included

# Author

Sarayu Nalagatlla
