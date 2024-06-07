from single_sign_on import SSOToken


class MyService:

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle(self, request, sso_token):
        if self.sso_registry.is_valid(sso_token):
        # if True:
            return Response("Hello {0}!".format(request.name))
        else:
            return Response("Please sign in")


class Request:
    def __init__(self, name):
        self.name = name


class Response:
    def __init__(self, text):
        self.text = text
