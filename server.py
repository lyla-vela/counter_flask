from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def create_user():
    if 'times' not in session:
        session['times']=0
    else:
        session['times']=session['times']+1 
    
    return render_template('index.html')

    
@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We redirected the user to /")
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
