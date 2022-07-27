from flask import Flask
app = Flask(__name__)

# 同一个视图绑定多个URL
# 用多个装饰器进行装饰即可
@app.route('/')
@app.route('/index')
def index():
    return "Welcome to Flask"

if __name__ == '__main__':
    app.run(debug=True)
