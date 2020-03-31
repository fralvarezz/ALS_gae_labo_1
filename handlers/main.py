#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

class MainHandler(webapp2.RequestHandler):
    def post(self):
        regex="0*[1-9][0-9]*(.[0-9]+)?"

        kms = self.request.get("kms", "Desconocido")
        try:
            kms = float(kms)
        except ValueError:
            kms = "Desconocido"
        tiempo = self.request.get("tiempo", "Desconocido")
        try:
            tiempo = float(tiempo)
        except ValueError:
            tiempo = "Desconocido"
        consumo_medio = self.request.get("consumo_medio", "Desconocido")
        try:
            consumo_medio = float(consumo_medio)
        except ValueError:
            consumo_medio = "Desconocido"

        if kms != "Desconocido" and tiempo != "Desconocido":
            self.response.write("Velocidad media de " + str(kms/tiempo) + "km/h\n")
        if kms != "Desconocido" and consumo_medio != "Desconocido":
            self.response.write("Consumo de " + str(kms*consumo_medio) + " litros\n")


        #self.response.write("Consumo de " + kms * consumo_medio + " litros")




app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
