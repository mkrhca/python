from flask import Flask 
from flask import request 
import subprocess 

app = Flask(__name__) 

stop_cal_cmd = "sudo docker stop CAL"
start_cal_cmd = "sudo docker start CAL"
stop_amq_cmd = "sudo docker stop RHAMQ"
start_amq_cmd = "sudo docker start RHAMQ"
stop_ibm_cmd = "sudo docker stop IBMMQ"
start_ibm_cmd = "sudo docker start IBMMQ"

@app.route('/stop_cal')
def stop_cal():
  try:
    result = subprocess.check_output([stop_cal_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop CAL."


@app.route('/start_cal')
def start_cal():
  try:
    result = subprocess.check_output([start_cal_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start CAL."


@app.route('/stop_rhamq')
def stop_rhamq():
  try:
    result = subprocess.check_output([stop_amq_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop RHAMQ."


@app.route('/start_rhamq')
def start_rhamq():
  try:
    result = subprocess.check_output([start_amq_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start RHAMQ."

@app.route('/stop_ibmmq')
def stop_ibm():
  try:
    result = subprocess.check_output([stop_ibm_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop IBMMQ."


@app.route('/start_ibmmq')
def start_ibm():
  try:
    result = subprocess.check_output([start_ibm_cmd], shell=True) 
    return result
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start IBMMQ."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
