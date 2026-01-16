# 📝 My Journal — A Personal Journaling Web App

A sleek, dark-themed journaling web application built with **Flask** and **SQLite**, designed to help you track your daily mood, thoughts, coding progress, and reflections — all in one place.
link for site (https://levelup-journal.onrender.com/);
---

## ✨ Features

* 📓 Create daily journal entries
* 🟢 Track **Mood**, **Mind**, **Code Progress**, and **Reflections**
* ✨ Smart reflection suggestions based on your mood & thoughts
* 📜 View all past entries in a clean, animated layout
* ✏️ Edit existing entries
* 🗑️ Delete entries with confirmation
* 🔔 Toast notifications with sound feedback
* 🌌 Animated particle background
* 🚀 Version tracking via `version.txt`

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite (via SQLAlchemy)
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Animations:** CSS animations + Particles.js

---

## 📂 Project Structure

```
.
├── app.py
├── journal.db
├── version.txt
├── /templates
│   ├── index.html
│   ├── entries.html
│   └── edit.html
├── /static
│   └── /sounds
│       └── success.mp3
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Doremon-tech-svg/my-journal.git
cd my-journal
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask flask-sqlalchemy
```

---

### 4️⃣ Set Version (Optional)

Create a file called `version.txt`:

```txt
v1.0
```

This version is displayed in the footer of the app.

---

### 5️⃣ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* Each journal entry stores:

  * Mood
  * Mental state
  * Coding progress
  * Personal reflections
  * Entry date
* Entries are saved in a local SQLite database
* Reflection suggestions adapt based on keywords in mood and thoughts
* The “Last Updated” footer reflects your most recent journal entry

---

## 📸 Screenshots

*Add screenshots or a demo GIF here for GitHub preview.*

---

## 🔐 Data & Privacy

* All data is stored **locally** in `journal.db`
* No external APIs or cloud storage
* No user authentication (single-user personal journal)

---

## 📈 Future Improvements

* 🔐 User authentication
* 📅 Calendar view
* 🔍 Search & filters
* ☁️ Cloud sync / backups
* 📊 Mood analytics & charts
* 🌙 Light/Dark theme toggle

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a Pull Request

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💙 Author

Built with focus, reflection, and
