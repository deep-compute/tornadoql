"""
TornadoQL server as a simple example or skeleton
"""
from tornadoql import TornadoQL
from example_schema import DEFAULT_SCHEMA
from basescript import BaseScript

class ExampleScript(BaseScript):
    def run(self):
        TornadoQL(DEFAULT_SCHEMA, log=self.log).start()

if __name__ == '__main__':
    ExampleScript().start()
