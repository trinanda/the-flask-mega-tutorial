from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


# ketika flask sell dijalankan, ini akan menjalankan fungsi ini, dan mendaftarkan item yang di return olehnya kedalam session sell
@app.shell_context_processor
def make_shell_contex():
    return {'db': db, 'User': User, 'Post': Post}
