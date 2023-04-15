from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def conditinal():

    course = 'data science'

    return render_template(
        'conditional.html', course=course
        )

@app.route("/loops")
def loops():

    movies = [
        'iron man',
        'bahubali',
        'RRR',
        'mr. bean'
    ]

    return render_template(
        'loops.html', movies=movies
        )
