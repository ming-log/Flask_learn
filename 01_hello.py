from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')  # 什么样的URL能触发函数    根目录  /
def hello_world():
    return "今天天气真好，你说呢"

@app.route('/hello')  # /hello
def hello():
    return "hello world!"

if __name__ == '__main__':
    # app.run()
    # host: IP地址
    # port: 端口
    # debug: True 调试模式，修改代码可实时进行网页更新
    app.run(host='0.0.0.0', port=1234, debug=True)
