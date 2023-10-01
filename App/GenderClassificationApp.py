from flask import Flask, render_template, request, url_for


from HelperFunctions import GenderClassificationSystem

app = Flask(__name__)


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("Home.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename
		img.save(img_path)
		
		img_dict = GenderClassificationSystem(img_path)
		
        	


	return render_template("Home.html", img_dict = img_dict)


if __name__ == '__main__':
    app.run(debug=True)