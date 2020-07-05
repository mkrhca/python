from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import subprocess 
import os 

FNULL = open(os.devnull, 'w')

app = Flask(__name__) 
api = Api(app) 

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

class Service_Get(Resource):
  def get(self, action):
    action = action + '_cmd' 
    return invoke(action)

class Service_Put(Resource):
  def post(self):
    input_json = request.get_json()
    action = input_json['cmd']
    action = action + '_cmd' 

    if action not in action_commands:
      return jsonify({"ERROR":"Incorrect endpoint or path"})

    return invoke(action)

api.add_resource(Service_Get, '/isl/v1/service/<string:action>')
api.add_resource(Service_Put, '/isl/v1/service/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
