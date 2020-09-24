from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')

def abc():
    return render_template('percentage.html')

@app.route('/kik', methods=['GET','POST'])

def xyz():
    if(request.method=='POST'):
        num1=int(request.form['n1'])
        num2=int(request.form['n2'])
        num3=int(request.form['n3'])
        total=(num1+num2+num3)/3
        return render_template('percentage.html',result=total)
if __name__=='__main__':
    app.run()