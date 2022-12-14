# Flask除了能够匹配URL，还能够生成URL。
# Flask可以用url_for来给指定的函数构造URL
# 它接受函数名作为第一个参数，也接受对应URL规则的变量部分的命名参数。
# 未知变量名部分会添加到URL末尾作为查询参数

from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ID: %d' % post_id

@app.route('/url/')
def redirect_to_url():
    # 跳转到show_post()视图函数
    # redirect: 重定向
    return redirect(url_for('show_post', post_id=100))

if __name__ == '__main__':
    # app.run()
    # host: IP地址
    # port: 端口
    # debug: True 调试模式，修改代码可实时进行网页更新
    app.run(host='0.0.0.0', port=1234, debug=True)
