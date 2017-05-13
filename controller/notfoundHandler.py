import webapp2
from webapp2_extras import jinja2

class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        msg = "This page does not exist on the web"

        template_values = {
            "error_msg": msg,
            "handler" : "/"
        }

        self.response.write(jinja.render_template("error.html", **template_values))