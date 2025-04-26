from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Model
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(100), nullable=False)
    mind = db.Column(db.String(300), nullable=False)
    code = db.Column(db.String(300), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<JournalEntry {self.id}>"

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_entry():
    mood = request.form.get('mood')
    mind = request.form.get('mind')
    code = request.form.get('code')
    body = request.form.get('body')
    date = datetime.now().strftime('%m/%d/%Y')

    if not all([mood, mind, code, body]):
        return jsonify({"message": "All fields are required!"}), 400

    new_entry = JournalEntry(mood=mood, mind=mind, code=code, body=body, date=date)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Entry saved successfully!"})

@app.route("/entries")
def show_entries():
    entries = JournalEntry.query.order_by(JournalEntry.id.desc()).all()
    return render_template("entries.html", entries=entries)

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('show_entries'))

@app.route('/edit/<int:entry_id>', methods=['GET'])
def edit_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    return render_template('edit.html', entry=entry)

@app.route('/update/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    entry.mood = request.form['mood']
    entry.mind = request.form['mind']
    entry.code = request.form['code']
    entry.body = request.form['body']
    entry.date = request.form['date']
    db.session.commit()
    return redirect(url_for('edit_entry', entry_id=entry_id, updated='true'))

if __name__ == "__main__":
    app.run(debug=True)
