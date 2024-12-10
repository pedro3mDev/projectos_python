from login import app 

@app.route("/")
def index():
    return "Teste"