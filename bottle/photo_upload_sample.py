from bottle import route,request,run,os
​
# HTTP://localhost:8080/と入力すると実行される関数
@route('/')
def home():
    return '''
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="upload"/>
        <input type="submit" value="upload">
    </form>
    '''
​
# HTTP://localhost:8080/と入力すると実行される関数
@route('/upload',method='POST')
def upload():
    # formタグのuploadで指定された送信ファイルを受け取る
    upload=request.files.get('upload')
    # 送信されたファイルのパスを受け取る
    name,ext=os.path.splitext(upload.filename)
    # パスに含まれていないとき実行する
    if ext not in('.png','jpg','jpeg','JPG'):
        return 'File extension not allowed.'
    # 指定したディレクトリに保存する
    save_path="./"
    upload.save(save_path)
    return 'OK'
​
# Webサーバを起動する
run(host='localhost',port=8080,debug=True)