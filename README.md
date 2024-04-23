# Chatbot Project

This Django-based chatbot project integrates a simple chat interface with a backend that processes messages using a Rasa chatbot. It demonstrates the use of Django for web development and AJAX for asynchronous web requests.

## Features

- Chat interface built with HTML, CSS, and JavaScript.
- Backend processing with Django.
- Integration with Rasa for natural language understanding.
- Use of `.env` for secure configuration management.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.0.3
- Rasa
- PostgreSQL (or any database of your choice, adjust settings accordingly)

### Installation

1. Clone the repository:
   
  git clone https://github.com/Ayikoandrew/chatbot.git
  
3. Navigate to the project directory:
   
   cd chatbot
   
5. Install required Python packages:
   
   pip install -r requirements.txt
   
7. Create a `.env` file in the project root directory and add your configuration:
   
   SECRET_KEY=your_secret_key_here
   
   DATABASE_NAME=your_database_name
   
   DATABASE_USER=your_database_user
   
   DATABASE_PASSWORD=your_database_password
   
   DEBUG=True

8. Apply migrations to create the database schema:
   
   python manage.py migrate
9. Start the Django development server:
   
### Usage

- Access the chat interface at `http://localhost:8000/chatbot/`.
- Interact with the chatbot through the web interface.

## Configuration

- **Django settings**: Configured in `mychatbot/settings.py`, sensitive settings are loaded from environment variables defined in the `.env` file.
- **Database**: Configure your database settings in the `.env` file and ensure `settings.py` is set up to read these values.
- **Static and media files**: Managed by Django's static files app.

## Security

- Use a strong `SECRET_KEY` in production and never commit your `.env` file to version control.
- Set `DEBUG` to `False` in production.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
