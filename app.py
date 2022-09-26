from flask import Flask, render_template

app = Flask(__name__, static_url_path='/cdn')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/terms/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms/tos')
def tos():
    return render_template('tos.html')


@app.route('/invited')
def invited():
    return render_template('invited.html')


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.73', port=8000)
