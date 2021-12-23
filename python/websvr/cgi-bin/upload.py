import cgi
import os

print("Content-Type: text/html; charset=UTF-8")
print("")
# print("Hello World.")

MEGA = 1048576    # 一度にアップロードするデータサイズ
path = "./uploaded_data/"
form_data = cgi.FieldStorage()    # HTMLのフォームからデータを受け取る準備

file_name = form_data['imagefile'].filename    # ファイル名を取得
full_path = path + file_name    # ファイル名にパスを付加
if os.path.exists(full_path):    # 上書き確認
  print(file_name + ' already exists.<br>')
  
uploaded_file = open(full_path, 'wb')    # アップロードされたデータを保存する新規ファイルを同名で作成
item = form_data['imagefile']
while True:
  chunk = item.file.read(MEGA)
  if not chunk:
    break
  uploaded_file.write(chunk)
uploaded_file.close()
print(file_name + ' has just been uploaded.<br>')    # アップロードされたことを表示
