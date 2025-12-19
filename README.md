# Kareen - Controversial Blog For Unconventional Minds

A full-featured Flask-based blogging platform designed for sharing controversial and unconventional ideas. Built with modern web technologies to provide a secure, user-friendly experience for writers and readers alike.

## Features

- **User Authentication**: Secure registration, login, and logout functionality
- **Password Management**: Password reset via email verification
- **Blog Posts**: Create, read, update, and delete blog posts
- **User Profiles**: Custom profile pictures and account management
- **Pagination**: Efficient browsing through posts with pagination
- **Responsive Design**: Mobile-friendly interface using Bootstrap
- **Error Handling**: Custom error pages for better user experience
- **Email Integration**: SMTP-based email functionality for password resets

## Tech Stack

- **Backend**: Flask 2.1
- **Database**: SQLite with SQLAlchemy
- **Authentication**: Flask-Login with bcrypt password hashing
- **Forms**: Flask-WTF with WTForms
- **Email**: Flask-Mail with Gmail SMTP
- **Image Handling**: Pillow for profile picture processing
- **Deployment**: Gunicorn WSGI server
- **Frontend**: Jinja2 templates with Bootstrap CSS

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd blog_app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```
   SECRET_KEY=your_secret_key_here
   EMAIL_USERNAME=your_gmail_username
   APP_PASSWORD=your_gmail_app_password
   ```

   > **Note**: For Gmail, you'll need to generate an App Password. Visit your Google Account settings > Security > App passwords.

5. **Initialize the database**:
   ```bash
   python -c "from flaskblog import create_app; app = create_app(); app.app_context().push(); from flaskblog import db; db.create_all()"
   ```

## Usage

### Development

Run the application in development mode:
```bash
python wsgi.py
```

Or using Flask CLI:
```bash
export FLASK_APP=wsgi.py
flask run
```

The application will be available at `http://localhost:5000`

### Production

For production deployment (e.g., Heroku):

1. Ensure your `Procfile` is configured:
   ```
   web: gunicorn wsgi:app
   ```

2. Set environment variables in your deployment platform

3. Deploy using your preferred method

## Project Structure

```
blog_app/
├── flaskblog/
│   ├── __init__.py          # Application factory
│   ├── config.py            # Configuration settings
│   ├── models.py            # Database models (User, Post)
│   ├── error/               # Error handlers
│   ├── main/                # Home and about routes
│   ├── posts/               # Post CRUD operations
│   ├── users/               # User authentication and profiles
│   └── static/              # CSS, images, etc.
├── templates/               # Jinja2 templates
├── Procfile                 # Heroku deployment
├── requirements.txt         # Python dependencies
├── wsgi.py                  # WSGI entry point
└── README.md
```

## API Endpoints

- `GET /` - Home page with paginated posts
- `GET /about` - About page
- `GET /register` - User registration
- `GET /login` - User login
- `GET /logout` - User logout
- `GET /account` - User profile management
- `GET /post/new` - Create new post
- `GET /post/<id>` - View specific post
- `GET /post/<id>/update` - Update post
- `POST /post/<id>/delete` - Delete post
- `GET /reset_password` - Request password reset
- `GET /reset_password/<token>` - Reset password with token

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built following Flask tutorials and best practices
- Bootstrap for responsive design
- Flask ecosystem for robust web development
