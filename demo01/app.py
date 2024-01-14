from flask import Flask, request
# 使用Flask类创建一个app对象
# __name__:代表当前app.py这个模块
# 1.以后出现bug，可以帮助我们快速定位
# 2.便于寻找文件，有一个相对路径
app = Flask(__name__)

# 创建一个路由和视图函数的映射
@app.route('/')
def hellp_world():
    return "Hello World!!"

@app.route('/profile')
def profile():
    return "gerenzgongxin"

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return "您访问的博客是：%s" %blog_id

@app.route('/book/list')
def book_list():
    page = request.args.get("page", default=1, type=int)
    return f"您获取的是第{page}页......"


# debug模式
# app.run(debug=True)

# host模式
# app.run(debug=True,host="0.0.0.0")

# port模式
# app.run(debug=True,host="0.0.0.0",port="8000")
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8000")