from flask import Flask, jsonify, request 
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

action_commands = ['stop_ora_cmd', 
                   'start_ora_cmd',
                   'stop_cal_cmd',
                   'start_cal_cmd',
                   'stop_amq_cmd',
                   'start_amq_cmd',
                   'stop_all_cmd',
                   'start_all_cmd']

def invoke(action):
  if action not in action_commands:
    return jsonify({"ERROR":"Incorrect endpoint or path"})

  try:
    retcode = subprocess.call(eval(action), stdout=FNULL, stderr=subprocess.STDOUT) 
    if retcode == 0:
      result = '{status: success}' 
    else:
      result = '{status: failed}' 

    return jsonify(result)
  except subprocess.CalledProcessError as e:
    return "An error occurred while trying to execute", action
   
@app.route('/isl/v1/service/', methods=['POST'])
def run_post_task():
  input_json = request.get_json()
  action = input_json['cmd']
  action = action + '_cmd' 

  if action not in action_commands:
    return jsonify({"ERROR":"Incorrect endpoint or path"})

  return invoke(action)

@app.route('/isl/v1/service/<string:action>', methods=['GET'])
def run_get_task(action):
  action = action + '_cmd' 
  return invoke(action)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
