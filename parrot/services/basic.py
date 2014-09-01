from flask import g, request, jsonify
from parrot import app


@app.route('/')
def home():
    return 'test'


############### Below are the APIs for jobs and files #####################
@app.route('/files', methods=['GET'])
def files():
    '''This handler return the list of files in Constellation'''
    # fetch json data from Constellation URL
    # Wrap it into custom json object.
    resp = {"count": 10, "files": [{"path": "/folder1/1.mp4", "size": 2048},
            {"path": "/folder2/2.mp4", "size": 108274}]}
    return jsonify(resp)


@app.route('/nodes', methods=['GET'])
def nodes():
    '''This method returns the node list of the specified file\
    and its counts'''
    file_path = request.args.get('path', None)
    if not file_path:
        return 'Wrong file path'
    resp = {"count": 5, "nodes": [{"host": "ccnode1", "ip": "10.10.10.2",
            "fragment": "/abc/1/2/3/4"}, {"host": "ccnode2",
            "ip": "10.10.10.3", "fragment": "/abc/1/2/3/4"}]}
    return jsonify(resp)


@app.route('/images', methods=['GET'])
def images():
    '''This method returns the image list.'''
    resp = {"count": 3, "images": [{"name": "debian", "tag": "jessie",
            "repository": "atsg127.lss.emc.com"}]}
    return jsonify(resp)


@app.route('/jobs', methods=['GET'])
@app.route('/jobs/<job_id>', methods=['GET'])
def jobs(job_id=None):
    resp = None
    if not job_id:
        # fetch job list.
        resp = {"count": 3, "jobs": [{"id": "0000000001",
                "path": "/folder1/1.mp4",
                "image": "atsg127.lss.emc.com/debian:jessie"}]}
    else:
        # get job status according to `job_id`.
        resp = {"id": "0000000001", "path": "/folder1/1.mp4",
                "image": "atsg127.lss.emc.com/debian:jessie",
                "tasks": [{"node": "ccnode1",
                "status": "Waiting/Stopped/Running/Finished"},
                {"node": "ccnode2",
                "status": "Waiting/Stopped/Running/Finished"}],
                "result": 10}
    return jsonify(resp)


@app.route('/jobs/<job_id>/result', methods=['GET', 'POST'])
def job_result(job_id=None):
    resp = {"node": "node1", "result": 10}
    method = request.method
    if method == 'GET':
        return method
    elif method == 'POST':
        return method
    return jsonify(resp)


@app.route('/jobs', methods=['POST'])
def submit_job():
    '''request body: {"path": "/folder1/1.mp4",
    "image": "atsg127.lss.emc.com/debian:jessie"}'''
    resp = {"id": "0000000001"}
    return jsonify(resp)


############## Below are the APIs for building Analytical Images#########
@app.route('/call')
def call():
    from subprocess import call
    r = call(['ls', '-l'])
    return r
