from flask import Flask, jsonify 
import subprocess 
import os 

FNULL = open(os.devnull, 'w')

app = Flask(__name__) 

stop_ora_cmd = ['sudo', 'docker', 'stop', 'ORACLE']
start_ora_cmd = ['sudo', 'docker', 'start', 'ORACLE']
stop_cal_cmd = ['sudo', 'docker', 'stop', 'CAL']
start_cal_cmd = ['sudo', 'docker', 'start', 'CAL']
stop_amq_cmd = ['sudo', 'docker', 'stop', 'RHAMQ']
start_amq_cmd = ['sudo', 'docker', 'start', 'RHAMQ']
stop_all_cmd = ['sudo', 'docker', 'stop', 'CAL', 'RHAMQ', 'ORACLE']
start_all_cmd = ['sudo', 'docker', 'start', 'CAL', 'RHAMQ', 'ORACLE']

@app.route('/stop_ora')
def stop_ora():
  try:
    retcode = subprocess.call(stop_ora_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop ORACLE."


@app.route('/start_ora')
def start_ora():
  try:
    retcode = subprocess.call(start_ora_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start ORACLE."

@app.route('/stop_cal')
def stop_cal():
  try:
    retcode = subprocess.call(stop_cal_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop CAL."


@app.route('/start_cal')
def start_cal():
  try:
    retcode = subprocess.call(start_cal_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start CAL."

@app.route('/stop_rhamq')
def stop_rhamq():
  try:
    retcode = subprocess.call(stop_amq_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop RHAMQ."


@app.route('/start_rhamq')
def start_rhamq():
  try:
    retcode = subprocess.call(start_amq_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start RHAMQ."

@app.route('/stop_ibmmq')
def stop_ibm():
  try:
    retcode = subprocess.call(stop_ibm_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop IBMMQ."

@app.route('/start_ibmmq')
def start_ibm():
  try:
    retcode = subprocess.call(start_ibm_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start IBMMQ."

@app.route('/stop_all')
def stop_all():
  try:
    retcode = subprocess.call(stop_all_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to stop all application containers."

@app.route('/start_all')
def start_all():
  try:
    retcode = subprocess.call(start_all_cmd, stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to start all application containers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
