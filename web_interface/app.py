from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      return render_template("result.html")
if __name__== "__main__":
    app.debug = True
    app.run()