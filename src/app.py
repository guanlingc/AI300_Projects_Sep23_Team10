from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)

        premium_tech_support = form_input['premium_tech_support']
        contract_type = form_input['contract_type']
        internet_type = form_input['internet_type']
        has_unlimited_data = form_input['has_unlimited_data']
        num_dependents = int(form_input['num_dependents'])
        num_referrals = int(form_input['num_referrals'])

        model_inputs = [premium_tech_support, contract_type, internet_type, has_unlimited_data, num_dependents, num_referrals]
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
