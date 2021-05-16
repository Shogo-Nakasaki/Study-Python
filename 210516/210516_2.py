# クリプトタブだとYoutubeが頻繁にオフラインになる
# 普段使っているブラウザでリンクを漁ってきて良い感じにHTMLファイルにする。
# beautifulsoupを用いてのスクレイピングの確認も兼ねる

import os
import datetime
import requests

from bs4 import BeautifulSoup

# htmlファイルを作成する
today = datetime.date.today() # 現在の「年-月-日」を読み取る
path = 'D:\EveryDayMemo\ ' + str(today) + '.html'
f = open(path,'w')
f.close()

# htmlファイルに記入していく_い
f = open(path,'a')
f.write('<!DOCTYPE html>\n<html>\n  <head>\n    <title>' + str(today) + '</title>\n  </head>\n  <body>\n')
f.close()

# htmlファイルに記入していく_ろ
choice = 0
f = open(path,'a')
while (True): #ここからループ
    f = open(path,'a')
    # １：メモ、２：リンク、３：終了 
    choice = int(input(f"\n1:メモを記入\n2:リンクを記入\n3.終了\nどれを実行しますか？>>"))
    if(choice == 1):
        # 1はやっていたことをテキストでメモする
        text_memo = str(input(f"メモの記載内容は？>>"))
        f.write(text_memo + '<br>')
    elif(choice == 2):
        # リンクからスクレイピング
        url = input(f"添付するリンク>>")
        html = requests.get(url)
        soup = BeautifulSoup(html.content,'html.parser')
        #タイトル情報を引き抜き出力
        text_title = str(soup.find('title'))
        text_title = text_title.lstrip('<title>')
        text_title = text_title.rstrip('</title>')
        # 2はリンクとそのリンク先の説明を書く
        text_urll = str(url)
        text_urlm = text_title
        f.write('<a href="'+ text_urll + '">'+ text_urlm +'</a>' + '<br>')
    elif(choice == 3):
        # 3はブレイク
        break
    else:
        continue
    f.close()

# htmlファイルに記入していく_は
f = open(path,'a')
f.write('\n  </body>\n</html>')
f.close()