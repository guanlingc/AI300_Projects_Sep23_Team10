# AI300_Projects_Sep23-Team10
Project for AI300

Name: Chan Guan Ling

Using Catboost Model to predict customer churn

requirements.txt provides the environment needed to run this pipeline
use "src/app.py" for flask app

Files found in this repo
1) Model contains the .pkl files for the trained models
2) Research Notebook contains the .ipynb used for development and model training
3) src contains the main pipeline 

Final Chosen Model

model = CatBoostClassifier(learning_rate=0.1, depth=2, random_seed=5)

Final AUC = 0.8140085186938003

--- URL is no longer avaliable to save cost ---
URL for deployed web app

18.141.231.69 

or
 
ec2-18-141-231-69.ap-southeast-1.compute.amazonaws.com
--- URL is no longer avaliable to save cost ---

