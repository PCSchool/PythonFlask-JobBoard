From flask import Flask, render_template

app = flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render render_template('index.html')