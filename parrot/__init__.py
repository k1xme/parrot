from flask import Flask

app = Flask("parrot")


from parrot.services import basic
