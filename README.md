# Stripe Payments API Integration
This project aims to demonstrate the integration of Stripe Payments API into a web application built with Django and React.

## Setup
 Clone the repository current repository:
```sh
git@github.com:lucassavioli/django-stripe-api.git
```
Navigate to the project directory:
```sh
cd django-stripe-api
```
Create a virtual environment:
```sh
python3 -m venv venv
```
## Install dependencies
#### Backend (Django)
Install the depedencies of the backend using the requirements.txt.
```sh
pip install -r requirements.txt
```
#### Frontend (React)
```sh
cd frontend && npm install
```
## Set up Stripe API keys:
First you need to obtain your Stripe API keys from the Stripe Dashboard. After that, set your API keys in a .env file.

## Starting Django and React
Run migrations, and start the backend server:
```sh
python manage.py migrate
python manage.py runserver
```
Navigate to the frontend directory and run
```sh
cd frontend
npm run dev
```