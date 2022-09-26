from flask import Flask,render_template,request
app = Flask(__name__,template_folder="templates")

@app.route('/')
def hello_world():
 return render_template("index.html")

#@app.route('/result',method = ['POST'])
#  def result():
#    # output = request.form.to_dict()
#    # name = output["name"]
#    # return render_template("index.html",name = name)
#    return 'sdsadsdfsd12312312312313'


@app.route('/c',methods=['POST', 'GET'])
def c():
   output = request.form.to_dict()
   name = output["name"]
   return render_template("index.html",name = name)


if __name__ == '__main__':
   app.run(debug=True,port=8080)