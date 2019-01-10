from app import app, db, cli
from app.models import User, Post


# (venv) $ pip install python-dotenv
# FLASK_APP=microblog.py


#ketika flask sell dijalankan, ini akan menjalankan fungsi ini, dan mendaftarkan item yang di return olehnya kedalam session sell
@app.shell_context_processor
def make_shell_contex():
    return {'db': db, 'User': User, 'Post': Post}
