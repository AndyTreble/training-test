from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
  return 'Hello World awesome!'
if __name__ == '__main__':
  app.run(host='0.0.0.0', 

@app.route('/goodbye')
def hello():
  return 'goodbye World awesome!'
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)