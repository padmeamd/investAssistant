from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get-file-content', methods=['GET'])
def get_file_content():
    file_path = 'data/sample.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({'content': content})
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
