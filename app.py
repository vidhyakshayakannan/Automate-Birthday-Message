from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Friend {self.username}>'

@app.route('/')
def index():
    friends = Friend.query.all()
    return render_template('index.html', friends=friends)

@app.route('/add', methods=['POST'])
def add_friend():
    username = request.form['username']
    birthday = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
    new_friend = Friend(username=username, birthday=birthday)
    try:
        db.session.add(new_friend)
        db.session.commit()
        flash('Friend added successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error! Friend could not be added.', 'danger')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_friend(id):
    friend = Friend.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            friend.username = request.form['username']
            friend.birthday = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
            db.session.commit()
            flash('Friend updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error! Friend could not be updated: {str(e)}', 'danger')
            return redirect(url_for('edit_friend', id=id))  # Redirect back to edit page with error
    
    return render_template('edit_friend.html', friend=friend)

@app.route('/send_messages')
def send_messages():
    cl = Client()
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    today = datetime.today().strftime('%Y-%m-%d')
    friends = Friend.query.filter_by(birthday=today).all()
    message = "happy birthday!! wishing you only the best in all that life has to offer"
    for friend in friends:
        cl.direct_send(message, [cl.user_id_from_username(friend.username)])
    flash(f'Sent birthday messages to {len(friends)} friends!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
