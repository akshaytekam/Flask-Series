from flask import Flask, render_template

app = Flask(__name__)

class Employee:
    def __init__(self, salary, name, address, designation):
        self.salary = salary
        self.name = name
        self.address = address
        self.designation = designation

@app.route("/")
def first_page():

    # List
    movies = [
        'iron man',
        'bahubali',
        'RRR',
        'mr. bean'
    ]

    # Dict
    cars = {
        'model': '007',
        'brand': 'tesla',
        'year': '2023',
    }

    # class object
    people = Employee('salary', 'name', 'address','designation')

    kwargs = {
        'movies': movies,
        'cars': cars,
        'people': people,
    }

    return render_template(
        'data_structures.html', **kwargs
        )
