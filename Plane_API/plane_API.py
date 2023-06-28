from flask import Flask, jsonify, request
from data.flight_data import flights
from utils.util import search_flight, get_index

#create our app from the Flask library
app = Flask(__name__)
# ------------------------------

#entry point of api returns string
@app.route('/')
def hello():
    return {'hello': 'Universe'}

#get all out flights
@app.route('/flights')
def get_flights():
    return flights
#http://127.0.0.1:5000/flights

#get all flights by id
#<> is a naming convention for how to find it at a later date
@app.route('/flight_by_id/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)
#http://127.0.0.1:5000/flights/555

#add new flights
@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    print(flight)
    flights.append(flight)
    print(flights)
    return flight

#updating a flight
@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])

#deleting a flight
@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200


# ------------------------------
#I wonder how this works youtube later
if __name__ == '__main__':
    #start the app in debug mode when the above is true
    app.run(debug=True)