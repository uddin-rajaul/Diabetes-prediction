# Diabetes Prediction Web Application

This is a Django-based web application for predicting diabetes risk using a trained machine learning model.

## Project Structure

- `prediction/` : Main Directory containing settings and urls.
- `predictModel/`: Django app containing the prediction logic and views.
  - `models.py`: Contains models for data processing (not used in this project).
  - `views.py`: Contains views for rendering templates and handling requests.
  - `templates/`: Directory for HTML templates.
    - `index.html`: Template for input form.
    - `result.html`: Template for displaying prediction result.
- `static/`: Directory for static files (CSS, JavaScript, images).
- `trained_model.sav`: Trained machine learning model saved using pickle.
- `scaler.sav`: Scaler used for preprocessing input data.
- `manage.py`: Django management script.

## Dependencies

- Python 3.x
- Django
- scikit-learn

## Setup

1.  Clone the repository:

    ```bash
    git clone https://github.com/yourusername/diabetes-prediction-app.git
    cd diabetes-prediction-app

    ```

2.  Install dependencies using pip:

    ```bash
    pip install django scikit-learn

    ```

3.  Install Dependencies from requirements.txt
    To run the Diabetes Prediction Web Application, you can install the required Python packages using pip and the requirements.txt file included in the project repository. First, set up a virtual environment (recommended) and activate it:

    ```bash # Create a virtual environment
    python -m venv venv

        # Activate the virtual environment (Windows)
        venv\Scripts\activate

        # Activate the virtual environment (macOS/Linux)
        source venv/bin/activate
    ```

4.  Next, install the required dependencies using pip and the requirements.txt file:

    ```bash
    pip install -r requirements.txt
    ```

5.  Run the Django development server:

    ```bash
    python manage.py runserver

    ```

6.  Open a web browser and go to http://localhost:8000/ to access the application.
