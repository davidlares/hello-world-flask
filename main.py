from flask import Flask 
#del modulo flask, traete la clase Flask
app = Flask(__name__) 
# variable app con una instancia de Flask 
# primer param (nombre del modulo)

@app.route('/')
def hello_world():
	return 'Hello World'

if __name__ == '__main__':
	app.run()