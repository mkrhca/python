from flask import Flask, jsonify 
import subprocess 
import os 

FNULL = open(os.devnull, 'w')

app = Flask(__name__) 

@app.route('/isl/v1/service/<string:action>', methods=['GET'])
def run_task(action):
  stop_ora_cmd = ['sudo', 'docker', 'stop', 'ORACLE']
  start_ora_cmd = ['sudo', 'docker', 'start', 'ORACLE']
  stop_cal_cmd = ['sudo', 'docker', 'stop', 'CAL']
  start_cal_cmd = ['sudo', 'docker', 'start', 'CAL']
  stop_amq_cmd = ['sudo', 'docker', 'stop', 'RHAMQ']
  start_amq_cmd = ['sudo', 'docker', 'start', 'RHAMQ']
  stop_all_cmd = ['sudo', 'docker', 'stop', 'CAL', 'RHAMQ', 'ORACLE']
  start_all_cmd = ['sudo', 'docker', 'start', 'CAL', 'RHAMQ', 'ORACLE']
  
  action = action + '_cmd' 
  try:
    retcode = subprocess.call(eval(action), stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to execute", action

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
