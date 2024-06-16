# Automate Birthday Message

This is a Flask-based web application that helps you manage and send birthday messages to friends via Instagram. This project demonstrates basic CRUD operations with SQLAlchemy for managing friends and integrates with the Instagram API (via instagrapi) to send birthday messages.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add friends with their username and birthday.
- View the list of friends with their birthdays.
- Send birthday messages to friends via Instagram.
- Basic error handling for adding friends and sending messages.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/friend-birthday-reminder.git
   cd friend-birthday-reminder
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   ```

   Replace `your_secret_key_here`, `your_instagram_username`, and `your_instagram_password` with appropriate values.

4. **Initialize the database:**

   Run the following commands to set up the database schema:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the application:**

   ```bash
   flask run
   ```

   Open your web browser and go to `http://localhost:5000` to view the application.

## Usage

- **Add a Friend:**
  - Navigate to the homepage.
  - Fill out the "Add Friend" form with the friend's Instagram username and birthday.
  - Click on "Add Friend" to add them to your friend list.

- **Send Birthday Messages:**
  - Click on the "Send Birthday Messages" button to send birthday messages to friends whose birthday matches the current date.

## Environment Variables

- `FLASK_APP`: The entry point of your Flask application (e.g., `app.py`).
- `FLASK_ENV`: The environment in which Flask is running (`development` or `production`).
- `SECRET_KEY`: A secret key used by Flask to secure sessions and other things.
- `INSTAGRAM_USERNAME`: Your Instagram username.
- `INSTAGRAM_PASSWORD`: Your Instagram password.

Make sure to keep your `.env` file secure and do not expose it publicly (e.g., by adding it to `.gitignore`).

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or issues, feel free to open a pull request or report an issue in the GitHub repository.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
