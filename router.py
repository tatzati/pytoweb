import re

from webob import Request
from webob import exc
from six import string_types

from utils import load_controller, template_to_regex


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, template, controller, **vars):
        if isinstance(controller, string_types):
            controller = load_controller(controller)
        self.routes.append((re.compile(template_to_regex(template)),
                            controller,
                            vars))

    def __call__(self, environ, start_response):
        req = Request(environ)
        for regex, controller, vars in self.routes:
            match = regex.match(req.path_info)
            if match:
                req.urlvars = match.groupdict()
                req.urlvars.update(vars)
                return controller(environ, start_response)
        return exc.HTTPNotFound()(environ, start_response)
