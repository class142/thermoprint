import requests
import textwrap
from escpos.printer import Network

class JokePrinter:
    def run(self):
        p = Network("10.47.13.147", 1234)
        r = requests.get('http://10.0.0.4:1880/witz')
        text = textwrap.fill(r.text, 40)
        p.text(r.text)
        p.ln(2)
        p.cut()
        p.close()
