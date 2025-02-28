from flask import Flask,redirect,url_for,render_template,request
import config

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(port=config.PORT,host=config.HOST,debug=True)