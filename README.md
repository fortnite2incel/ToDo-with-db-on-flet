# Flet To-Do Application with Database Integration (`ToDo-with-db-on-flet-main`)
A cross-platform desktop/GUI To-Do Application built with **Python**, **Flet** (Flutter for Python), and an **SQLite** database backend. The application provides an interactive graphical interface to manage tasks while maintaining persistent state across sessions.

---

## 🛠 Technology Stack

* **GUI Framework:** [Flet](https://flet.dev/) (Flutter engine for Python)
* **Programming Language:** Python 3.x
* **Database:** SQLite (`db/todo.db`)
* **Configuration & Query Abstraction:** `config.py` & `db/` helper modules

---

## ✨ Key Features

* **Cross-Platform Graphical UI (`main.py`):** Responsive desktop interface built with Flet controls.
* **Database Persistence (`db/`):** Full integration with an SQLite database to store and update tasks.
* **Database Abstraction (`db/main_db.py`, `db/queries.py`):** Structured SQL query execution and database connections separated from UI logic.
* **Configurable Database Path (`config.py`):** Centralized path routing (`path_db = 'db/todo.db'`) for flexible environment setups.

---

## 📁 Project Structure

```text
ToDo-with-db-on-flet-main/
├── config.py                   # Central configuration (e.g., SQLite DB path definition)
├── main.py                     # Main Flet GUI entry point and event handlers
└── db/                         # Database operations package
    ├── __init__.py
    ├── todo.db                 # SQLite database storage file
    ├── main_db.py              # SQLite connection and database context manager
    └── queries.py              # SQL queries (Create, Read, Update, Delete)
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.10+** installed.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd ToDo-with-db-on-flet-main
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # On Linux/macOS:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install flet
   ```

4. **Run the Application:**
   ```bash
   python main.py
   ```
