import os
import webapp2
from webapp2_extras import jinja2

class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        msg = None

        try:
            msg = self.request.GET['msg']

        except:
            msg = None

        if msg == None:
            msg = "CRITICAL - contact development team"

        template_values = {
            "error_msg": msg,
        }

        self.response.write(jinja.render_template("error.html", **template_values))