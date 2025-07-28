# Simple Color Changing Dashboard

A simple Dash application that features a button that changes color when clicked.

## Features

- Interactive button that changes to a random color on each click
- Click counter display
- Modern, responsive design
- Ready for deployment on Render

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:8050`

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app.server`
   - **Environment**: Python 3

4. Deploy!

## Project Structure

```
dash/
├── app.py          # Main Dash application
├── wsgi.py         # WSGI entry point for deployment
├── requirements.txt # Python dependencies
└── README.md       # This file
``` 