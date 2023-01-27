from flask import Flask
import random

app = Flask(__name__)

# 딕셔너리로 목록을 만들음
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            <H2>{content}</H2>
            Hello, Web
        </body>
    </html>
    '''

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return template(liTags, '<h2>Welcome</h2>Hello, WEB')


@app.route('/create/')
def create():
    return 'Create page'

@app.route('/read/<int:id>/') #<username> 을 변수로 설정할 수 있고, def(함수)의 인자에 username을 넣어서 동작시킬 수 있음
def read(id):
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(title, body)
    # return 'Read ' + id

app.run(port=5000, debug=True)
# ()안에 port=5001 이런식으로 port 번호 설정해줄 수 있음!
# ()안에 debug=True로 해놓으면 .py 파일이 저장될 때마다 서버가 다시 실행됨. 개발중일때만 하기 -> Debugger is active! 라는 메시지 뜸

# 브라우저로 들어가면 http response 헤더까지 만들어서 보내줌
