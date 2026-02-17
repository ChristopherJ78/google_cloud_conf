# Google Cloud Tech Conf Website

This is a Flask-based website for a 1-day Google Cloud technical conference. It includes a schedule of 8 talks, speaker information, and search functionality.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

## Setup Instructions

1.  **Clone or Download the Project**:
    Ensure you have the project files in a directory (e.g., `google_cloud_conf`).

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4.  **Install Dependencies**:
    ```bash
    pip install flask
    ```

## Running the Application

1.  **Start the Flask Server**:
    ```bash
    python app.py
    ```

2.  **Access the Website**:
    Open your web browser and go to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features

- **Home Page**: Displays the conference date, location, and full schedule.
- **Search**: Filter talks by Title, Speaker Name, or Category via the search bar.
- **Responsive Design**: Works on desktop and mobile devices.
- **Lunch Break**: Automatically inserted into the schedule.

## Project Structure

- `app.py`: Main Flask application file containing route logic and dummy data.
- `templates/index.html`: Jinja2 template for the homepage.
- `static/css/style.css`: Custom CSS styles.
- `static/js/`: Directory for client-side scripts (optional).

## Customization

- **Modify Data**: Edit the `TALKS` list in `app.py` to change speakers, times, or titles.
- **Change Styles**: Update `static/css/style.css` to alter the look and feel.
- **Update Template**: Edit `templates/index.html` to change the HTML structure.
