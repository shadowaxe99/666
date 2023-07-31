```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database.db import db
from ai_models.authentication import User
from ai_models.git_operations import clone_repository
from ai_models.pdf_processing import process_pdf
from ai_models.code_processing import process_code
from ai_models.feedback_system import Feedback

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.authenticate(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User.register(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Username already exists')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/clone_git', methods=['GET', 'POST'])
@login_required
def clone_git():
    if request.method == 'POST':
        repository_url = request.form['repository_url']
        clone_repository(repository_url)
    return render_template('clone_git.html')

@app.route('/upload_pdf', methods=['GET', 'POST'])
@login_required
def upload_pdf():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        process_pdf(pdf_file)
    return render_template('upload_pdf.html')

@app.route('/upload_code', methods=['GET', 'POST'])
@login_required
def upload_code():
    if request.method == 'POST':
        code_file = request.files['code_file']
        process_code(code_file)
    return render_template('upload_code.html')

@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        feedback_content = request.form['feedback_content']
        Feedback.submit_feedback(current_user.id, feedback_content)
    return render_template('feedback.html')

if __name__ == "__main__":
    app.run(debug=True)
```