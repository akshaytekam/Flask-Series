from flask import Flask, render_template

app = Flask(__name__)


@app.route("/expressions")
def expressions():

    name = "Data To Info"
    course_name = "Data Science"

    inr1 = 1000
    inr2 = 2000

    person1 = "Akshay"
    person2 = "Salman"

    kwargs = {
        "name" : name,
        'course_name' : "Data Science",
        'inr1' : 1000,
        'inr2' : 2000,
        'person1' : "Akshay",
        'person2' : "Salman",
    }

    return render_template(
        'expressions.html', **kwargs
        )
