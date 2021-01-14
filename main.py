  
# way to upload audio
# way to save audio
# function to predict the output
import numpy as np
import os
from flask import Flask, request, jsonify, render_template
import pickle
UPLOAD_FOLDER="/Users/hp/Desktop/samsung_prism_code"
app = Flask(__name__, template_folder='/Users/hp/Desktop/samsung_prism_code/API')

@app.route('/',methods=["GET","POST"])
def upload_predict():
	if request.method == "POST":
		audio_file=request.files["audio"]
		if audio_file:
			audio_location=os.path.join(UPLOAD_FOLDER,audio_file.filename)
			# TYPE YOUR MODEL HERE ######
			



			return render_template('idex.html',prediction=1)

	return render_template('idex.html',prediction=0)


app.run(debug=True)