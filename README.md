# My Django URL Shortener Project

Welcome to the My Django URL Shortener project! This repository contains the code for a URL shortening service built with Django.

## Getting Started Locally

Follow these steps to set up the project locally:

### Prerequisites

- Python
- Django (you can install it via pip install django)
- Git (for cloning the repository)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Varun-Kolanu/22075043_KOLANU_VARUN.git

2. Navigate to the project directory:

   ```bash
   cd 22075043_KOLANU_VARUN

3. Activate the virtual environment (optional but recommended
 - On Windows:

   ```bash
   .\venv\Scripts\activate    

- On MacOs or Linux:

   ```bash
   source venv/Scripts/activate   

5. Install required dependencies:
   ```bash
   pip install -r requirements.txt

6. Create a .env taking reference of .env.example and replace your database credentials
7. Apply database migrations
   ```bash
   python manage.py migrate

8. Start the development server
   ```bash
   python manage.py runserver

9. Open http://localhost:8000/ to open the local development server of the url shortener


### Production Link

You can access production link [here](https://url-shortener-k8ut.onrender.com/)


### Endpoints:

1. "/" - Home page
2. "/url_list/" - Short Urls List
   
