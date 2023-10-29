import joblib


class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)
    

# beneficiary_example = {
#     "has_premium_tech_support": "Yes",
#     "contract_type": "Two Year",
#     "internet_type": "Cable",
#     "has_unlimited_data": "Yes",
#     "num_dependents": 0,
#     "num_referrals": 3
# }
# model_inputs = list(beneficiary_example.values())

# print(model_inputs)                  # [30, 'female', 20, 1, 'yes', 'southwest']
# print(Model().predict(model_inputs)) # 17353.51581464062