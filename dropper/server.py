from flask import Flask, send_file

app = Flask(__name__)

@app.route('/get/image')
def get_file():
    file_path = '/path/to/encoded/image'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
