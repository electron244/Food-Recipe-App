# 🍽️ Recipe App

A simple Django-based Recipe App that allows users to add recipes with a title and description. Users can also delete recipes from the list. 📝

## ✨ Features
➕ Add recipes with a title and description
📝 Update recipes with new details
📦 Store recipes in an SQLite database
🗑️ Delete recipes with a single click
🖥️ Simple and user-friendly interface

## 🔧 Installation

### 1. 📥 Clone the Repository
```sh
git clone https://github.com/electron244/Food-Recipe-App.git
cd Food-Recipe-App
```

### 2. 🏗️ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. 🔄 Apply Migrations
```sh
python manage.py migrate
```

### 4. 🚀 Run the Server
```sh
python manage.py runserver
```

## 🏃‍♂️ Usage
1. Open `http://127.0.0.1:8000/` in your browser.
2. Enter a recipe title and description, then click the **➕ Add Recipe** button.
3. Your recipe will be saved and displayed on the page.
4. Click the **🗑️ Delete** button next to a recipe to remove it.

## 🗄️ Database
The project uses an SQLite database by default, but you can change it in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 📂 Project Structure
```
recipe-app/
│── recipes/
│   ├── migrations/
│   ├── models.py      # Database model for recipes
│   ├── views.py       # Views for handling requests
│   ├── urls.py        # URL routing
│   ├── templates/
│   │   ├── index.html  # Main template file
│── manage.py          # Django management script
│── db.sqlite3         # SQLite database file
│── requirements.txt   # List of dependencies
│── README.md          # Project documentation
```

## 📌 Requirements
- 🐍 Python 3.8+
- 🎯 Django 4.0+

## 🤝 Contributing
Feel free to fork this repository and make improvements. You can submit a pull request with your changes.

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

