from webob import Request

from router import Router
from utils import controller


@controller
def hello(req):
    if req.method == 'POST':
        return 'Hello {}!'.format(req.params['name'])
    elif req.method == 'GET':
        return '''<form method="POST">
            Your name: <input type="text" name="name">
            <input type="submit">
            </form>'''


hello_world = Router()
hello_world.add_route('/', controller=hello)

request = Request.blank('/')
# resp = request.get_response(hello_world)
# print(resp)

request.method = 'POST'
request.body = b'name=Gerardo'
resp = request.get_response(hello_world)
print(resp)
