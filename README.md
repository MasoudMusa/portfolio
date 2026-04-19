# Personal Portfolio - Django

A premium, high-performance personal portfolio website built with **Django** and **Tailwind CSS**. This project features a sophisticated stone-and-beige aesthetic, optimized for showcasing technical expertise in software development, backend engineering, and algorithmic trading systems.

## 🚀 Features

- **Modern UI/UX**: Clean, minimal design using a curated "Geist" font and stone color palette.
- **Dynamic Projects Showcase**: Categorized portfolio with interactive filtering (All, Trading Systems, Web Apps, Internal Tools).
- **Service Pillars**: Dedicated sections for Core Competencies, Technical Skills, and Project Consultations.
- **Responsive Navigation**: Smooth scroll-based navigation with a backdrop blur effect.
- **Interactive Elements**:
  - Custom range sliders and hover-reveal effects for project cards.
  - Floating Action Button (FAB) for quick contact.
  - Fade-in animations for smooth transitions.
- **Fully Integrated Backend**: Powered by Django with a modular `core` app structure, ready for further expansion (e.g., dynamic project management through Admin).

## 🛠️ Tech Stack

- **Framework**: Django 6.0+
- **Frontend**: Tailwind CSS (CDN-based), HTML5, JavaScript
- **Icons**: Iconify (Solar & MDI sets)
- **Environment**: Python Virtual Environment (venv)
- **Database**: SQLite (Default)

## 📁 Project Structure

```text
Portfolio/
├── core/                   # Django App for main logic
│   ├── templates/core/     # HTML templates (index.html)
│   ├── views.py            # Home view controller
│   └── ...
├── portfolio_project/      # Project settings and URLs
├── venv/                   # Python Virtual Environment
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## ⚙️ Getting Started

### 1. Prerequisites
- Python 3.9+ installed on your system.

### 2. Activate Virtual Environment
On Windows:
```powershell
.\venv\Scripts\activate
```

### 3. Install Dependencies
(Dependencies are already installed in the provided `venv`, but you can reinstall them via:)
```powershell
pip install django
```

### 4. Run Migrations
Initialize the local database:
```powershell
python manage.py migrate
```

### 5. Start the Server
Launch the development server:
```powershell
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to view the site.

## 📝 Configuration

- **Root Page**: The root URL is mapped to `core.views.home` which renders `core/templates/core/index.html`.
- **Styling**: Tailwind CSS is loaded via CDN for rapid development and flexibility.

## 🤝 Contact

**Masoud**
- **Email**: mwendamwabehah@gmail.com
- **GitHub**: [github.com/MasoudMusa](https://github.com/MasoudMusa)
- **LinkedIn**: [linkedin.com/in/MwendaMusa](https://linkedin.com/MwendaMusa)

---
*Created with ❤️ for portfolio transformation.*
