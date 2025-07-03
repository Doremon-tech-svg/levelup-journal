import os
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Load version safely
try:
    with open('version.txt', 'r') as f:
        VERSION = f.read().strip()
except FileNotFoundError:
    VERSION = "dev"

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database
db = SQLAlchemy(app)

# DB Model
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(100), nullable=False)
    mind = db.Column(db.String(300), nullable=False)
    code = db.Column(db.String(300), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Keeping string format for compatibility

    def __repr__(self):
        return f"<JournalEntry {self.id}>"

# Create DB tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    now = datetime.now().strftime("%B %d, %Y")
    return render_template('index.html', version=VERSION, now=now)

@app.route('/submit', methods=['POST'])
def submit_entry():
    mood = request.form.get('mood', '').strip()
    mind = request.form.get('mind', '').strip()
    code = request.form.get('code', '').strip()
    body = request.form.get('body', '').strip()
    date = datetime.now().strftime('%m/%d/%Y')

    if not all([mood, mind, code, body]):
        return jsonify({"message": "All fields are required!"}), 400

    new_entry = JournalEntry(mood=mood, mind=mind, code=code, body=body, date=date)
    db.session.add(new_entry)

    try:
        db.session.commit()
        logger.info("New journal entry added.")
        return jsonify({"message": "Entry saved successfully!"})
    except Exception as e:
        db.session.rollback()
        logger.error("Error saving entry: %s", str(e))
        return jsonify({"message": "Error saving entry."}), 500

@app.route("/entries")
def show_entries():
    entries = JournalEntry.query.order_by(JournalEntry.id.desc()).all()
    return render_template("entries.html", entries=entries)

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    try:
        db.session.commit()
        logger.info("Deleted entry %s", entry_id)
    except Exception as e:
        db.session.rollback()
        logger.error("Error deleting entry: %s", str(e))
    return redirect(url_for('show_entries'))

@app.route('/edit/<int:entry_id>', methods=['GET'])
def edit_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    return render_template('edit.html', entry=entry)

@app.route('/update/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    mood = request.form.get('mood', '').strip()
    mind = request.form.get('mind', '').strip()
    code = request.form.get('code', '').strip()
    body = request.form.get('body', '').strip()
    date = request.form.get('date', '').strip()

    if not all([mood, mind, code, body, date]):
        logger.warning("Missing fields during update.")
        return redirect(url_for('edit_entry', entry_id=entry_id))

    entry.mood = mood
    entry.mind = mind
    entry.code = code
    entry.body = body
    entry.date = date

    try:
        db.session.commit()
        logger.info("Updated entry %s", entry_id)
    except Exception as e:
        db.session.rollback()
        logger.error("Error updating entry: %s", str(e))

    return redirect(url_for('edit_entry', entry_id=entry_id, updated='true'))

if __name__ == "__main__":
    app.run(debug=True)
