from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "dojo"

@app.route('/')
def index():
	if 'num_refreshed' in session.keys():
		session['num_refreshed'] +=1
	else:
		session['num_refreshed'] = 1
	return render_template('index.html')



@app.route('/process', methods=['POST'])
def keeping_track():
	return redirect('/')


app.run(debug=True)