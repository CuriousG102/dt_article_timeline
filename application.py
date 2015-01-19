import copytext
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def make_emeddable():
	context = {
		'COPY': copytext.Copy('copy_sheet/events.xlsx')
	}
	return render_template('timeline.html', **context)

if __name__ == '__main__':
	app.run()
