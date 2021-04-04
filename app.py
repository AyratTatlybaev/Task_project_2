from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html', departure=data.departures[departure])


@app.route('/tours/<int:id>/')
def render_tours(id):
    return render_template('tour.html', id_tour=data.tours[id])


@app.route('/data')
def render_data_tours():
    return render_template('data.html')


@app.route('/data/departures/<departure>/')
def render_data_departure(departure):
    return render_template('departures.html')


@app.route('/data/tours/<int:id>')
def render_data_tours_id(id):
    return render_template('tours.html')

# Run server
app.run(debug=True)
