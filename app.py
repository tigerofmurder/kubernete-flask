import sys
from flask import Flask,render_template, request,Response
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/run", methods=['POST', 'GET'])
def runcode():
	from flask import jsonify

	if request.method == "POST":
		codeareadata = request.form['codearea']
		try:#save original standart output reference
			original_stdout = sys.stdout
			sys.stdout = open('file.txt', 'w') #change the standard output to the file we created
			#execute code
			exec(codeareadata)  #example =>   print("hello world")
			sys.stdout.close()
			sys.stdout = original_stdout  #reset the standard output to its original value
			# finally read output from file and save in output variable
			output = open('file.txt', 'r').read()
		except Exception as e:
		# to return error in the code
			sys.stdout = original_stdout
			output = e
	#finally return and render index page and send codedata and output to show on page
	return render_template( 'index.html', code = codeareadata , output = output)
'''if __name__ == "__main__":
	app.debug = True
	app.run()
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080, debug=True)
    #app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
    