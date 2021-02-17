from flask import Flask
app = Flask(__name__) # create a flask app named app
@app.route("/")
def home():
return '''My name is Otu Eleri. This is my CA2 work.
My GitHub URL is https://github.com/honeywellnoodles'''
# In the return statement above, Use your own name and GitHub URL
if __name__ == "__main__": app.run(port=5005)