from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        required_fields = ['total_sqft', 'location', 'bhk', 'bath']
        if not all(field in request.form for field in required_fields):
            return jsonify({'error': 'Invalid input. Ensure all required fields are present.'}), 400

        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Perform data validation checks
        if total_sqft <= 0 or bhk <= 0 or bath <= 0:
            return jsonify({'error': 'Invalid input. Ensure all values are positive.'}), 400

        if location not in util.get_location_names():
            return jsonify({'error': 'Invalid location.'}), 400

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except KeyError:
        return jsonify({'error': 'Invalid input. Ensure all required fields are present.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
   

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()