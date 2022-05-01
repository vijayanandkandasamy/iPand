# Required Imports
import os
import pyrebase
import json
import pandas as pda
#import pandas as pandas_html_map
import folium
#import plotly.express as px

from flask import render_template, request, redirect, session
from app import app
from flask_dropzone import Dropzone

# Global Variables
uploaded_filename= ""
analysis_title_text= ""

# Start of  Displaying Current Working Directory #
current_working_directory = "Current Working Directory: " + os.getcwd()
print(current_working_directory)
# -- End of  Displaying Current Working Directory #

# Start of Firebase Configuration & Initialization #

with open('../config.json') as firebase_configuration_file:
    firebase_configuration = json.load(firebase_configuration_file)

firebase = pyrebase.initialize_app(firebase_configuration)
auth = firebase.auth()

# -- End of Firebase Configuration & Initialization #

# Start of  Drop Zone - Path & Configuration
basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'user_file_upload'),
    DROPZONE_MAX_FILE_SIZE = 102400,
    DROPZONE_TIMEOUT = 5*60*1000,
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = '.csv')
dropzone = Dropzone(app)
# -- End of  Drop Zone - Path & Configuration

# Start of iPand - Application - Routes & Functions

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
            email_address = request.form['email_address']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email_address, password)
                #user_id = auth.get_account_info(user['idToken'])
                #session['usr'] = user_id
                return render_template('home.html')
            except:
                unsuccessful = 'Please check your credentials'
                return render_template('index.html', error_message=unsuccessful)
    return render_template('index.html')
# -- End of iPand - Application - Routes & Functions

# User - Sign Up - Route & Function

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if (request.method == 'POST'):
            email_address = request.form['email_address']
            password = request.form['password']
            message_successful = 'Account Created Successfully'
            auth.create_user_with_email_and_password(email_address, password)
            return render_template('index.html', success_message=message_successful)
    return render_template('index.html')

# Forgot Password - Route & Function

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
            email = request.form['name']
            auth.send_password_reset_email(email)
            return render_template('index.html')
    return render_template('forgot_password.html')

# iPand - Application - Home - Route & Function

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# iPand - Application - Read Me - Route & Function

@app.route('/read_me', methods=['GET', 'POST'])
def read_me():
    return render_template('read_me.html')

# iPand - Application - Pandemic Forecast Analysis - User Requirement - Interface - Route & Function - Get Request
@app.route('/pandemic_forecast_analysis', methods=['GET'])
def pandemic_forecast_analysis():
    return render_template('pandemic_forecast_analysis.html')

# iPand - Application - Pandemic Forecast Analysis - User Requirement - Interface - Route & Function - Get Request

@app.route('/pandemic_forecast_analysis', methods=['POST'])
def pandemic_forecast_analysis_user_inputs():
    if request.method == 'POST':
        global analysis_title_text
        analysis_title_text = request.form.get("analysis_title_text")
    return render_template('pandemic_dataset_upload.html', analysis_title=analysis_title_text)

# iPand - Application - Pandemic Forecast Analysis - Upload - Interface - Route & Function - Get Request

@app.route('/pandemic_dataset_upload', methods=['GET'])
def pandemic_dataset_upload():
    return render_template('pandemic_dataset_upload.html', analysis_title=analysis_title_text)

# iPand - Application - Pandemic Forecast Analysis - Upload - Route & Function - Post Request

@app.route('/pandemic_dataset_upload', methods=['POST'])
def upload():
    global uploaded_filename
    file = None
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
        uploaded_filename = f.filename
    return render_template('pandemic_dataset_upload.html', analysis_title=analysis_title_text)

# iPand - Application - Pandemic - Dataset - Visualization - Route & Function - Get Request
@app.route('/pandemic_dataset_visualization', methods=['GET'])
def pandemic_dataset_visualization():
    def find_top_confirmed(n = 15):
        pandemic_dataset_reader = pda.read_csv(os.path.join(app.config['UPLOADED_PATH'],uploaded_filename))
        by_country = pandemic_dataset_reader.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
        pandemic_data_frame = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
        return pandemic_data_frame

    pandemic_data_frame=find_top_confirmed()
    pairs=[(country,confirmed) for country,confirmed in zip(pandemic_data_frame.index,pandemic_data_frame['Confirmed'])]

    pandemic_dataset_reader = pda.read_csv(os.path.join(app.config['UPLOADED_PATH'],uploaded_filename))
    pandemic_html_map=pandemic_dataset_reader[['Lat','Long_','Confirmed']]
    pandemic_html_map=pandemic_html_map.dropna()
    m=folium.Map(location=[34.223334,-82.461707],
                tiles='Stamen toner',
                zoom_start=8)
    def circle_maker(x):
        folium.Circle(location=[x[0],x[1]],
                     radius=float(x[2]),
                     color="red",
                     popup='confirmed cases:{}'.format(x[2])).add_to(m)
    pandemic_html_map.apply(lambda x:circle_maker(x),axis=1)
    html_map=m._repr_html_()   
    return render_template('pandemic_dataset_visualization.html', table=pandemic_data_frame, cmap=html_map, pairs=pairs, analysis_title=analysis_title_text)

# iPand - Application - Pandemic - Dataset - Visualization - Route & Function - Get Request

@app.route('/my_reports', methods=['GET', 'POST'])
def my_reports():
    return render_template('my_reports.html')

if __name__ == '__main__':
    app.run(debug=True) 
