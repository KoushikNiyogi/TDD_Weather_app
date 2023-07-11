from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}
next_id = 1  # Next available ID for new cities

@app.route('/weather/city/<city>', methods=['GET'])
def get_city_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'message': 'City not found'}), 404

@app.route('/weather/city', methods=['POST'])
def post_city():
    global next_id
    city = request.json['city']
    temperature = request.json['temperature']
    weather_data[next_id] = {'city': city, 'temperature': temperature}
    next_id += 1
    return jsonify({'message': 'City added successfully', 'id': next_id - 1}), 201

@app.route('/weather/city/<city>', methods=['PATCH'])
def patch_city(city):
    temperature = request.json['temperature']
    if city in weather_data:
        weather_data[city]['temperature'] = temperature
        return jsonify({'message': 'City updated successfully'})
    else:
        return jsonify({'message': 'City not found'}), 404

@app.route('/weather/city/<city>', methods=['DELETE'])
def delete_city(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': 'City deleted successfully'})
    else:
        return jsonify({'message': 'City not found'}), 404

if __name__ == '__main__':
    app.run()
