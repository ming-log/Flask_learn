from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')  # 渲染模板

@app.route('/user/<username>')
def show_user(username):
    return render_template('user.html',
                           name=username,
                           name_len=len(username),
                           ls=[2,5,3,6,5],
                           dict_={'name':'骆明', 'age':'18'},
                           comments='今天星期三')  # 渲染模板

@app.route('/base')
def base():
    return render_template('use_base.html')

if __name__ == '__main__':
    app.run(debug=True)
