import copytext
from flask import Flask

app = Flask(__name__)


@app.route('/')
def make_emeddable():
	context = {
		'COPY': copytext.Copy('copy_sheet/events.xlsx')
	}
	for row in sheet:
		events
	return render_template('timeline.html', **context)
	