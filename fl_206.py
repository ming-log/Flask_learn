# coding=utf-8

# 文件上传
import flask, os, sys,time
from flask import request

file_type = ['zip', 'rar', '7z']  # 允许上传的文件格式
path = '206'  # 端口号及文件存储文件夹
max_size = 10  # 最大文件大小，单位M
interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)  # 将当前文件的父目录加入临时系统变量


server = flask.Flask(__name__, static_folder='static')
server.config['MAX_CONTENT_LENGTH'] = max_size * 1024 * 1024


@server.route('/', methods=['get'])
def index():
    if not os.path.exists(path):
        os.mkdir(path)
    all_file = os.listdir(path)
    num = len(all_file)
    file_list = '<br>'.join(all_file)
    return '<h1>三峡大学【信计、统计、应数】文件提交</h1>上传的文件格式<font color="red">' + str(file_type) + '</font><br>大小需<font color="red">小于' + str(max_size) + 'M</font><br>可重复提交，只保留最后一次提交结果。<br><form action="/upload" method="post" enctype="multipart/form-data">队伍编号：<input type="text" id="num" name="num" required><br>队长姓名：<input type="text" id="name" name="name" required><br><input type="file" id="img" name="img" required><br><button type="submit">上传</button></form><font color="red">提交完毕后可刷新本页面，在已提交的文件中查看是否有相应的文件。<br>有，则说明提交成功。<br>没有，则说明提交失败，请重新提交。</font>' + '<hr>' + '已提交结果：'  + str(num) + '份<br>' + file_list


@server.route('/upload', methods=['post'])
def upload():
    name = request.form['name']
    num = request.form['num']
    fname = request.files['img']  #获取上传的文件
    upload_file_type = fname.filename.split('.')[-1]
    if upload_file_type in file_type:
        file_name = num + '_' + name + '.' + upload_file_type
        if fname:
            new_fname = path + r'/' + file_name
            fname.save(new_fname)  # 保存文件到指定路径
            return '成功上传:【%s】' % file_name
        else:
            return '{"msg": "请上传文件！"}'
    else:
        return '请上传{}文件。'.format(file_type)

print('----------路由和视图函数的对应关系----------')
print(server.url_map) #打印路由和视图函数的对应关系
server.run(host='0.0.0.0', port=int(path))