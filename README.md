# 🎬 Metflix — Netflix-Inspired Movie Web Application

**Metflix** is a Netflix-inspired movie browsing and watchlist web application built using **Django**. The project provides a simple platform where users can explore movies, view detailed information, create an account, and maintain their personal watchlist.

The application is developed as a Django learning project with a focus on **Django models, authentication, templates, forms, media files, Tailwind CSS, and database relationships**.

---

## 🚀 Features

### 🎥 Movie Browsing

* Browse available movies from the database.
* Display movie posters and movie information.
* View individual movie details.
* Movies can be associated with multiple genres.
* Movie ratings, release dates, descriptions, and trailer links are supported.

### 🔎 Movie Details

Each movie can contain:

* Movie name
* Poster
* Genres
* Rating
* Release date
* Description
* Trailer link
* Date added

The movie detail page allows users to explore complete information about a selected movie.

### 📌 Watchlist

Authenticated users can maintain their own personal watchlist.

Users can:

* Add movies to their watchlist.
* View their saved movies.
* Remove movies from their watchlist.
* Prevent duplicate movie entries in the same user's watchlist.

The watchlist is connected to the Django authentication system, so every user has an independent collection of saved movies.

### 🔐 User Authentication

The application uses Django's built-in authentication system.

Available functionality includes:

* User registration
* Login
* Logout
* Protected movie detail pages
* Protected watchlist functionality

Users are automatically logged in after successful registration.

### 🎭 Genre Management

Movies and genres use a **Many-to-Many relationship**, allowing a movie to belong to multiple genres.

For example:

```text
Movie
 ├── Action
 ├── Adventure
 └── Sci-Fi
```

### 🖼️ Media & Posters

Movie poster images are stored using Django's `ImageField` and uploaded to the `media/posters/` directory.

### 🎨 Tailwind CSS

The project uses **Django Tailwind** for styling and frontend development.

The project also includes `django-browser-reload` for a smoother development workflow.

---

## 🛠️ Tech Stack

| Technology               | Purpose                    |
| ------------------------ | -------------------------- |
| 🐍 Python                | Backend programming        |
| 🌐 Django                | Web framework              |
| 🗄️ SQLite               | Database                   |
| 🎨 Tailwind CSS          | Frontend styling           |
| 🖼️ Pillow               | Image processing           |
| 🔐 Django Authentication | User authentication        |
| 🐳 Docker                | Containerization           |
| 📝 HTML                  | Templates                  |
| ⚡ Django Templates       | Dynamic frontend rendering |

The project's dependencies include Django 6, Django Tailwind, Pillow and Django Browser Reload.

---

## 🏗️ Project Structure

```text
myDjango/
│
├── myApp/
│   ├── migrations/
│   ├── templates/
│   │   └── myApp/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── myDjango/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── registration/
│   ├── website/
│   └── layout.html
│
├── static/
├── media/
│   └── posters/
│
├── theme/
├── db.sqlite3
├── Dockerfile
├── manage.py
└── requirements.txt
```

The repository currently contains separate application, project, template, static/media, theme and Docker-related components.

---

## 🗄️ Database Models

Metflix currently uses three main application models.

### `Genre`

Stores movie genres.

```text
Genre
 ├── id
 └── name
```

The genre name is unique.

### `Movies`

Stores movie information.

```text
Movies
 ├── name
 ├── image
 ├── date_added
 ├── genres
 ├── rating
 ├── release_date
 ├── description
 └── trailer_link
```

A movie can have multiple genres through a Many-to-Many relationship.

### `WatchList`

Connects users with movies.

```text
User ──────── WatchList ──────── Movie
```

Each watchlist entry stores:

* User
* Movie
* Date added

The project also prevents the same user from adding the same movie multiple times.

---

## 🔄 Application Flow

```text
                ┌──────────────┐
                │    User      │
                └──────┬───────┘
                       │
              ┌────────▼────────┐
              │ Authentication  │
              └────────┬────────┘
                       │
                ┌──────▼──────┐
                │    Movies    │
                └──────┬──────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      Details       Genres       Watchlist
                                   │
                                   ▼
                              Saved Movies
```

The Django URL configuration routes users between the homepage, movie pages, authentication pages and watchlist functionality.

---

## 🔗 Main Routes

| Route                           | Function          |
| ------------------------------- | ----------------- |
| `/`                             | Main website      |
| `/myApp/`                       | Movie section     |
| `/myApp/movie/<id>/`            | Movie details     |
| `/myApp/watchlist/`             | User watchlist    |
| `/myApp/watchlist/add/<id>/`    | Add movie         |
| `/myApp/watchlist/remove/<id>/` | Remove movie      |
| `/myApp/register/`              | User registration |
| `/accounts/login/`              | Login             |
| `/accounts/logout/`             | Logout            |
| `/admin/`                       | Django admin      |

Movie details and watchlist operations are protected using Django's `login_required` decorator.

---

## 📋 Forms

The project uses Django Model Forms for handling application data.

### Movie Form

The `MovieForm` is based on the `Movies` model and provides fields for:

* Movie name
* Date added
* Genres

Genres are displayed using checkbox inputs.

### User Registration Form

The registration form extends Django's built-in `UserCreationForm` and adds an email field.

It handles:

* Username
* Email
* Password
* Password confirmation

---

## 🐳 Docker Support

The project includes a `Dockerfile` for running Metflix inside a Docker container.

The container:

1. Uses Python 3.14.6.
2. Sets `/metflix` as the working directory.
3. Copies the project files.
4. Installs dependencies from `requirements.txt`.
5. Exposes port `8000`.
6. Starts the Django development server.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pandeyaditya0022ee/Django.git
```

### 2. Navigate to the Project

```bash
cd Django/myDjango
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t metflix .
```

Run the container:

```bash
docker run -p 8000:8000 metflix
```

Then open:

```text
http://localhost:8000/
```

---

## 📚 What I Learned From This Project

This project helped in understanding practical Django concepts such as:

* Django project and app structure
* MVT architecture
* Django Models
* Django ORM
* One-to-Many / Many-to-Many relationships
* Django Forms
* Model Forms
* User Authentication
* Login-protected views
* URL routing
* Django Templates
* Static and Media files
* Image uploads with Pillow
* Tailwind CSS integration
* SQLite database
* Dockerizing a Django application

---

## 🔮 Future Improvements

Some features that can be added in future versions:

* 🔍 Movie search
* 🎭 Genre-based filtering
* ⭐ User ratings and reviews
* ❤️ Favorites
* 🎬 Embedded trailer playback
* 📱 Fully responsive UI
* 👤 User profiles
* 🎞️ Continue Watching
* 🕒 Recently Viewed Movies
* 📊 Personalized movie recommendations
* 🔌 REST API using Django REST Framework
* ☁️ Production deployment with PostgreSQL

---

## 👨‍💻 Author

**Aditya Pandey**

GitHub: [@pandeyaditya0022ee](https://github.com/pandeyaditya0022ee)

---

## ⭐ Project

If you find this project useful for learning Django, feel free to explore the repository and experiment with the code.

**Metflix — A Django-powered Netflix-inspired movie application.** 🍿
