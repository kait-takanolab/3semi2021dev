from bottle import route,request,run,os
import mysql.connector

# HTTP://localhost:8080/と入力すると実行される関数
@route('/')
def home():
    return '''
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="upload"/>
        <input type="submit" value="upload">
    </form>
    '''
    
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
    
@route('/db')
def dbcon():
    cnx = mysql.connector.connect(user='scott', password='tiger',
                              host='127.0.0.1',
                              database='kisounit2')

    # カーソルの取得(検索結果からデータ１件ずつ抜き取るための仕組み)
    database = cnx.cursor(buffered = True)

    # データの取得
    sql = 'SELECT * FROM emp WHERE ename = "KING"';
    database.execute(sql)

    #表示
    rows = database.fetchall()
    print(rows)

    #カーソル終了
    database.close()

    #MySQl切断
    cnx.close()
    return str(rows)
    
    

# Webサーバを起動する
run(host='localhost',port=8080,debug=True)