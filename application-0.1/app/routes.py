from app import app


@app.route('/')
@app.route('/index')
def index():
    return "First Project Test Page."
