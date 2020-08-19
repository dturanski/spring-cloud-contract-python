
import os
import sys
from flask import Flask
'''Only needed if module not installed'''
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
if 'CONTRACT_TEST' in os.environ:
    from spring.cloud.contract import Stub

app = Flask(__name__)


@app.route('/add-job/<cmd>')
def add(cmd):
    if not cmd == 'bad':
        return message(cmd, 'actual')
    return bad()


def message(cmd, val):
    return "%s %s\n" % (cmd, val)


def function1(t):
    return(str(t)+'\n')


def bad():
    return 'bad command\n'


if __name__ == "__main__":
    if 'CONTRACT_TEST' in os.environ: #additional guard here is an optimization only, since the module checks anyway.
        stub = Stub(app)
        # Set the arguments to provide test values for the functions under test
        stub.create_stub(message, 'someValue', 'testing')
        stub.create_stub(bad)
        stub.create_stub(function1, t=(1, 2, 3, 4))
    app.run()
