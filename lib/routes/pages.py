import markdown

from flask import Markup, render_template
from flask.ext.login import login_required

from lib.server import app


def __load_markdown(filepath):
    with open(filepath) as f:
        return Markup(markdown.markdown(f.read()))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/readme')
def readme():
    section_markdown = (
        '0-intro',
        '1-location',
        '2-preparing',
        '3-tournament',
        '4-bounty',
        '5-prizes',
        '6-rules',
        '7-advanced',
        '8-starting',
        '9-api',
        '10-testing',
    )
    sections = [
        (section, __load_markdown('static/md/readme/%s.md' % section))
        for section in section_markdown
    ]
    return render_template('readme.html', sections=sections)


@app.route('/code-of-conduct')
def code_of_conduct():
    return render_template('code_of_conduct.html')


@app.route('/app/')
@app.route('/app/<path:path>')
@login_required
def play(path=None):
    # serve play.html for anything that starts with "play/"
    # frontend will show the correct route
    return render_template('app.html')
