# 动态URL
from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return "User: %s" % username

@app.route('/post/<float:post_id>')  # 可指定数据类型float
def show_post(post_id):
    return "Post ID: %.3f" % post_id


if __name__ == '__main__':
    # app.run()
    # 调试模式：可事实修改脚本内容
    app.debug = True
    app.run()

