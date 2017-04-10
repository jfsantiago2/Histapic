
import webapp2
from webapp2_extras import jinja2


class MainPage(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **{}))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        try:
            jinja = jinja2.get_jinja2(app=self.app)
            valor = int(self.request.get("edValor"))
            template_values = {
                'edValor': valor,
                'edValorConv': valor * 9 / 5 + 32,
            }
            self.response.write(jinja.render_template("answer.html", **template_values))

        except ValueError:

            template_values = {
                'dvError': "El valor introducido es incorrecto",
            }

            self.response.write(jinja.render_template("error.html", **template_values))




