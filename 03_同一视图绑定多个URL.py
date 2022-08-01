from flask import Flask

app = Flask(__name__)

# 同一个视图绑定多个URL
# 用多个装饰器进行装饰即可
@app.route('/')
@app.route('/index')
def index():
    return "Welcome to Flask"

if __name__ == '__main__':
    # app.run()
    # host: IP地址
    # port: 端口
    # debug: True 调试模式，修改代码可实时进行网页更新
    app.run(host='0.0.0.0', port=1234, debug=True)
