# 🌌 My Journal

> **A modern, distraction-free journaling web app for developers and thinkers.**
> Reflect on your mood, mind, code, and growth — all in one beautifully designed space.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## ✨ Why My Journal?

Most journaling apps are cluttered, generic, or disconnected from how developers think.
**My Journal** is built for intentional reflection — combining emotional awareness with technical progress.

Whether you’re:

* Debugging life 🧠
* Tracking your coding journey 💻
* Or simply unloading your thoughts 📓

This app stays out of your way and lets you write.

---

## 🚀 Features

* 📝 **Daily Journal Entries** — Simple, fast, and focused
* 🟢 **Mood Tracking** — Capture how you *feel*
* 🧠 **Mind State** — Track mental clarity, stress, or focus
* 💻 **Code Progress** — Log what you worked on
* 📓 **Reflections** — Free-form personal notes
* ✨ **Smart Reflection Suggestions** — Context-aware prompts
* 📜 **View Past Entries** — Clean, animated timeline
* ✏️ **Edit Anytime** — Refine past thoughts
* 🗑️ **Delete Safely** — With confirmation
* 🔔 **Toast Notifications + Sound Feedback**
* 🌌 **Animated Particle Background**
* 🚀 **Version Tracking** via `version.txt`

---

## 🖼️ Preview

> *Minimal UI. Dark theme. Smooth animations.*
> *Add screenshots or a short demo GIF here.*

---

## 🛠️ Tech Stack

| Layer    | Technology                    |
| -------- | ----------------------------- |
| Backend  | Flask (Python)                |
| Database | SQLite + SQLAlchemy           |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Effects  | CSS Animations, Particles.js  |

---

## 📂 Project Structure

```
.
├── app.py              # Flask application
├── journal.db          # SQLite database (local)
├── version.txt         # App version
├── templates/
│   ├── index.html      # Main journal page
│   ├── entries.html    # View all entries
│   └── edit.html       # Edit entry page
├── static/
│   └── sounds/
│       └── success.mp3 # UI feedback sound
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/my-journal.git
cd my-journal
```

---

### 2️⃣ (Recommended) Create a Virtual Environment

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

### 4️⃣ Set App Version

Create a `version.txt` file:

```txt
v1.0
```

Displayed in the footer as the current app version.

---

### 5️⃣ Run the App

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* Each entry stores:

  * Mood
  * Mind state
  * Code progress
  * Reflections
  * Date
* Entries are saved locally using SQLite
* Smart reflection suggestions adapt to keywords
* "Last Updated" reflects your most recent entry

---

## 🔐 Privacy & Data

* 🔒 **100% Local Storage** — No cloud, no tracking
* 🧘 **Private by Design** — Your thoughts stay yours
* 🚫 **No Authentication** — Built for single-user focus

---

## 🛣️ Roadmap

* 🔐 User authentication
* 📅 Calendar-based view
* 🔍 Search & filtering
* 📊 Mood analytics & trends
* ☁️ Optional cloud backup
* 🌗 Light / Dark theme toggle

---

## 🤝 Contributing

Ideas, issues, and pull requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and distribute.

---

## 💙 Author

Built with intention, curiosity, and growth in mind.

> *“Write to understand yourself. Build to understand the world.”*
