from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/process1', methods=['POST'])
def process1_pass():
    """
    Summary: runs process 1 on pc
    
    Returns:
        str: list of prime numbers
    """
    data1 = request.get_json()
    res = jsonify(process1(data["data"]))
    data1_return = process1(res)
    return data1_return

    
@app.route('/process2', methods=['POST'])
def process2_pass():
    """
    Summary: runs process 2 on pc
    
    Returns:
        str: list of prime numbers
    """
    data2 = request.get_json()
    res = jsonify(process2(data["data"]))
    data2_return = process2(res)
    return data2_return

if __name__ == "__main__":
    app.run()
