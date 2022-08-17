from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from palette import get_colors


app = Flask(__name__)


Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        color = get_colors(f)
        return render_template('palette.html', color=color)


if __name__ == "__main__":
    app.run(debug=True)
