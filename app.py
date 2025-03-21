from flask import Flask, render_template

app = Flask(__name__)

# Single route for the entire page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)