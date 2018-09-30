from flask import Flask, jsonify, request, Response
app = Flask(__name__)

test_page = b"""
<!doctype html>
<html>
<head>
<title>hello world</title>
</head>
<body>
<h1 id="greeting">hello, world</h1>
<script>
document.getElementById("greeting").innerHTML = "hello, csp"
</script>
</body>
</html>
"""
test_csp_policy = "default-src 'self'; report-uri http://localhost:5000/csp-report" 

root_message = {'csp reports go to': '/csp-report',
                'to test csp go to': '/test-csp-report'}

csp_report_data = {"ip_address":"",
                   "user_agent": "",
                   "csp-report": ""}


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(root_message)

@app.route('/csp-report', methods=['POST'])
def process_csp_report():
    #print(request.user_agent)
    #print(request.data)
    #print(request.remote_addr)
    csp_report_data['ip_address'] = request.remote_addr
    csp_report_data['user_agent'] = request.user_agent
    csp_report_data['csp-report'] = request.data
    print(csp_report_data)
    return jsonify({"status": "ok"})
    

@app.route('/test-csp-report', methods=['GET'])
def test_csp_report():
    resp = Response(test_page)
    resp.headers['Content-Security-Policy-Report-Only'] = test_csp_policy
    return resp

if __name__ == '__main__':
    app.run()
