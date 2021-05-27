import os

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xls', '.xlsx']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                flash('Not an accepted filetype')
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect(url_for('index'))

    return render_template('index.html')
