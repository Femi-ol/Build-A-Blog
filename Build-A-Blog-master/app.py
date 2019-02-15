from flask import Flask, url_for, request, render_template

app = Flask(__name__)
wsgi_app = app.wsgi_app

# theTitle = " " 
# thePost = " "

allPosts = []
buildContent = ""

@app.route('/')
def hello():

	url = url_for('createBlog')
	link = '<a href="' + url + '">Create a blog post</a>'

	# # scroll through dictionary and print out posts.
	# for inPost in allPosts:
	# 	buildContent += "'<h2>" + inPost['pTitle'] + "</h2>"
	# 	buildContent += "<div>" + inPost['pPost'] + "</div> <br /><br /><br />"


	return link;






@app.route('/createBlog', methods=['GET', 'POST'])
def createBlog():
	if request.method == 'GET':
	 	# Send page with form for blog post
		return render_template("writePost.html")

	elif request.method == 'POST':
	 	
	 	# accept entry into form above
	 	# create a variable to store images
	 	
	 	theTitle = request.form['myTitle']
	 	thePost = request.form['myPost']

	 	# use dictionary to store multiple posts
	 	new_post = {

		'pTitle': request.form['myTitle'],
		'pPost': request.form['myPost']
		}

	 	allPosts.append(new_post)

	 	# Give poster confirmation page
	 	return render_template('confirm.html')

	else:
	 	return "Very bad request"


@app.route('/readBlog', methods=['GET'])
def readBlog():

	buildContent = ""

	# scroll through dictionary and print out posts.
	for inPost in allPosts:
		buildContent += "'<h2>'" + inPost['pTitle'] + "'</h2>'"
		buildContent += "<div>" + inPost['pPost'] + "</div> <br /><br /><br />"
		
	return render_template('blogPost.html', buildContent = buildContent)



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)