# Django Real-Time Chat Application

This is a real-time chat application built using Django and WebSockets. It allows users to create accounts, log in, and participate in real-time conversations with other users.

## Features

- User authentication (sign up, log in, log out)
- Real-time messaging with WebSockets
- Chat rooms
- User profile management

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/django-real-time-chat.git
cd django-real-time-chat
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Usage

1. Navigate to `http://localhost:8000` in your web browser.
2. Sign up for a new account or log in with an existing account.
3. Create or join a chat room.
4. Start chatting in real-time!

## Contributing

We welcome contributions to this project. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.

### Steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request.
