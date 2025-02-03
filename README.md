# News Aggregator

A Flask-based web application that aggregates and displays news articles from a MongoDB database.

## Project Description

This web application serves as a news aggregator platform that:
- Displays news articles in a clean, organized format
- Stores articles in MongoDB Atlas
- Supports easy addition of mock data for testing
- Provides a simple and intuitive user interface

## Project Structure

```
news_aggregator/
├── .env                    # Environment variables (not in git)
├── .env.example           # Example environment variables template
├── .gitignore             # Git ignore rules
├── app.py                 # Main Flask application
├── insert_mock_data.py    # Script to insert test data
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment configuration
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
│   └── index.html       # Main page template
└── .venv/               # Virtual environment (not in git)
```

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd news_aggregator
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Copy `.env.example` to `.env`
- Update `.env` with your MongoDB credentials

5. Insert mock data (optional):
```bash
python insert_mock_data.py
```

6. Run the application:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Environment Variables

The following environment variables are required:
- `MONGODB_USERNAME`: MongoDB Atlas username
- `MONGODB_PASSWORD`: MongoDB Atlas password
- `MONGODB_CLUSTER`: MongoDB cluster address
- `MONGODB_DATABASE`: Database name
- `MONGODB_COLLECTION`: Collection name
- `MONGODB_OPTIONS`: MongoDB connection options

## Dependencies

Main dependencies include:
- Flask: Web framework
- PyMongo: MongoDB driver
- python-dotenv: Environment variable management

For a complete list, see `requirements.txt`

## Development

To add mock data to the database, run:
```bash
python insert_mock_data.py
```

The application runs in debug mode by default, which provides detailed error messages and auto-reloading when code changes are detected.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

[Your chosen license]
