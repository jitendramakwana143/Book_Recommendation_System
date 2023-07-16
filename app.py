from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def i():
    return render_template('i.html')


if __name__ == '__main__':
    app.run(debug=True)
