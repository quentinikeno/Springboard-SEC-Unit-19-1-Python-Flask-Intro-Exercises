from flask import Flask, request
import operations as op

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{op.add(a, b)}'

@app.route('/sub')
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{op.sub(a, b)}'

@app.route('/mult')
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{op.mult(a, b)}'

@app.route('/div')
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{op.div(a, b)}'

op_dict = {
    'add': op.add,
    'sub': op.sub,
    'mult': op.mult,
    'div': op.div
}

@app.route('/math/<q_operation>')
def all_in_one(q_operation):
    operation = op_dict.get(q_operation)
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{operation(a, b)}'