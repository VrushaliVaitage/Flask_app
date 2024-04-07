from flask import Flask, render_template, request

app=Flask(__name__)

# simple view creation
@app.route('/')
def first_view():
    return 'This is simple flask function code'

# template  rendering
@app.route('/temp')
def temp_view():
    return render_template('demo.html')

# context
@app.route('/context')
def view():
    name = 'Vrushali'
    list = ['Krishna', 'Vishal','Shiva']
    return render_template('home.html', nm=name,ln=list )

# GET_request >>>> data is fetched by request.args:
@app.route('/v1')
def view1():
    return render_template('loginG.html')

@app.route('/v2')
def view2():
    unm = request.args.get('unm')
    pwd = request.args.get('pwd')
    return render_template('success.html')

# POST request--->> data is fetched by request.form dict>>
@app.route('/v3')
def view3():
    return render_template('loginP.html')

@app.route('/v4', methods=['POST'])
def view4():
    unm = request.form.get('unm')
    pwd = request.form.get('pwd')
   
    print (f'username:{unm} and password:{pwd}')
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)