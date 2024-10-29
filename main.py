from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from controller.login_controller import LoginDao
from model.login_model import LoginDto

app = Flask(__name__)


# user login=======================
@app.route('/api/v1/user/login', methods=['POST', 'GET'])
def user_verify_auth():
    resp = {"cd": "000", "sms": "Success!"}
    payload = dict(request.json)
    dto = LoginDto()
    dto.UName = payload['uname']
    dto.UPass = payload['upass']
    dao = LoginDao()
    if (dao.verify_auth(dto)):
        resp = {"cd": "000", "sms": "Success!"}
    else:
        resp = {"cd": "888", "sms": "Failed!"}
    return resp


@app.route('/api/v1/user/confirm', methods=['POST', 'GET'])
def user_confirm_code():
    resp = {"cd": "000", "sms": "Success!"}
    payload = dict(request.json)
    dto = LoginDto()
    dto.UName = payload['uname']
    dto.UPass = payload['upass']
    dto.ConfirmCode = payload['confirm_code']
    dao = LoginDao()
    if (dao.confirm_code(dto)):
        resp = {"cd": "000", "sms": "Success!"}
    else:
        resp = {"cd": "888", "sms": "Failed!"}
    return resp


SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Flask API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if (__name__ == "__main__"):
    app.run(port='9091', debug=True)
