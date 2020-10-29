import falcon


class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello World"


app = falcon.API()
app.add_route("/", MainResource())
