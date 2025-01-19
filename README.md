# url_shortner

## Description

This is a Django-based URL shortener system that allows you to shorten URLs, specify expiration times, and track usage analytics.



## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Subhinpreet03/url_shortner.git
# Or use SSH:
git clone git@github.com:Subhinpreet03/url_shortner.git
cd url_shortner
```

### 2. Setting up Virtual Environment
```bash
python3 -m venv .venv  # Replace '.venv' with the name of your virtual environment if desired
```
### Activate the virtual environment:

- #### On macOS/Linux:
```bash
source .venv/bin/activate
```

- #### On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages  specified in the requirements.txt file:
```bash
pip install -r requirements.txt
```
Further you can use uv package to install quickly which is fast as compared to just pip
But firstly, you need to install uv
```bash
pip install uv
uv pip install -r requirements.txt
```

### 4. Setting up Database
- Create an .env file to add the Database credentials before running the migrations\
Sample .env:\
```bash
DATABASE_NAME = sample_name\
DATABASE_HOST = localhost\
DATABASE_USER = sample_user\
DATABASE_PASSWORD =sample_password\
DATABASE_PORT = 3306\
```
- #### Run the Migrations command\
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/.


