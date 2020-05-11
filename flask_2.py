from flask import Flask
from flask import jsonify, request, render_template, flash
from wtforms import Form, TextField, TextAreaField, validators, SubmitField
import config
import re
import target1_new as t
import score_cleaning as sc

app = Flask(__name__)

# App config
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

global vul_comment

vul=['disgust','shame','anger','fear']

class ReusableForm(Form):
    comment = TextAreaField('Comment:', validators=[validators.required()])


def check_comment_toxicity(comment):
	'''
	check comment for toxicity
	input: string
	output: value between 0 - 1 indicating toxicity
	'''
	score = sc.toxicity_score(comment)
	return score

def set_toxicity_message(comment):
        res=''
        res =  t.classify_dataset(comment)

        if res=='joy':
            message = 'Attention: Your comment is not toxic.'
        else:
            message = 'Success: Your comment toxic.'

        return message


@app.route('/', methods=['GET', 'POST'])
def hello():
	form = ReusableForm(request.form)

	print(form.errors)
	if request.method == 'POST':
		print("Form:")
		print(form)
		#name = request.form['name']
		comment = request.form['comment']
		#print(f"Name:{name}")
		print(f"Comment:{comment}")

		if form.validate():
			# Save the comment here.
			#flash('Hello ' + name + ' Comment: ' + comment)
			toxic_score = check_comment_toxicity(comment)

			toxicity_message = set_toxicity_message(comment)
                        
			print(f"Toxic Score:{toxic_score}")
			print(f"Toxic message:{toxicity_message}")

			flash(f"{toxicity_message} Toxicity Score: {toxic_score:0.2f}. " +\
				f"Your comment was: {comment}")

		else:
			flash('Error: All the form fields are required. ')

	return render_template('hello.html', form=form)

if __name__ == '__main__':
    app.run()
