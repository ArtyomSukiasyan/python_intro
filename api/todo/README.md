# To-Do App API (Pure Python)

This is a simple To-Do app API built using **pure Python** without any external frameworks like Flask or Django. The API is designed to handle CRUD operations (Create, Read, Update, Delete) for to-do items, and it connects to a MongoDB database using Docker.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
  - [Sample Requests](#sample-requests)
- [License](#license)

## Features

- Add, retrieve, update, and delete to-do items.
- Data persistence using MongoDB.
- Pure Python-based server with manual routing.
- Input validation middleware to ensure data integrity.

## Technologies

- **Python** (Pure Python HTTP Server)
- **MongoDB** (Using Docker for the database)
- **Pymongo** (MongoDB driver for Python)
- **Docker** (For running MongoDB in a container)

## Setup

### Requirements

- Python 3.6+
- Docker (for running MongoDB)
- `pymongo` library for MongoDB interaction

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd todo_app
