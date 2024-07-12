from flask import Flask, render_template, request
import joblib

app = Flask(__name__,static_url_path="/static")
model=joblib.load("Diabetes_model.sav")


@app.route('/')
def homepage():
    return render_template('index.html')
    
@app.route('/form')
def form():
    return render_template('alamak.html')

@app.route('/send', methods=['post'])
def process():
    BMI = int(request.form['Weight']) / pow(int(request.form['Height'])/100,2)
    data=[[
        request.form['HighBP'],
        request.form['HighChol'],
        request.form['CholCheck'],
        BMI,
        request.form['Smoker'],
        request.form['Stroke'],
        request.form['HeartDiseaseorAttack'],
        request.form['PhysActivity'],
        request.form['Fruits'],
        request.form['Veggies'],
        request.form['HvyAlcoholConsump'],
        request.form['GenHlth'],
        request.form['MenHlth'],
        request.form['PhysHlth'],
        request.form['Diffwalk'],
        request.form['Sex'],
        request.form['Age'],
    ]]
    result= model.predict(data)[0]


    if result == 0:
            result = "/static/assets/healthy.png"
    elif result == 1:
            result = "/static/assets/pre_diabetes.png"
    elif result == 2:
            result = "/static/assets/diabetes.png"
    return render_template ('result.html' , result=result)

if __name__=="__main__":
     app.run(debug   =True)
