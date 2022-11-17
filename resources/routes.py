from .heartrateAPI import HeartRateAPI, HeartAPI
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(HeartRateAPI, '/api/heart')
    api.add_resource(HeartAPI, '/api/heart/<int:id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')