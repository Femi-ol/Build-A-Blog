from flask import Flask, url_for, request, render_template

app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/')
def hello():

	url = url_for('createBlog')
	link = '<a href="' + url + '">Create a blog</a>'
	return link;


@app.route('/createBlog', methods=['GET', 'POST'])
def createBlog():
	if request.method == 'GET':
	 	# Send page with form for blog post
		return render_template("writePost.html")
	elif request.method == 'POST':
	 	# accept entry into form above
	 	
	 	theTitle = request.form['myTitle']
	 	thePost = request.form['myPost']
	 	# thePost = request.form['myPost']
	 	theImage = 'You'
	 	return "Hi"
	# 	theImage = request.form['myImage']


	 	return """
			<html>
				<head>
					<title>
						Hello World!
					</title>
				</head>
				<body>
				<div>
					""" + theTile + """
					</div>
				<div>
					""" + thePost + """
					</div>
				<div>
					""" + theImage + """
					</div>
				</body>
			</html>"""
	else:
	 	return "Very bad request"


@app.route('/readBlog')
def readBlog():
 	return "This is the  blog page"


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)