# 寝る前に直前まで見ていたサイトを起きてからも見たい
# いままでメモ帳に記載してたけど、リンクのコピペとかしずらい
# URLとサイト名、あとどう考えたかとかもメモしてhtml化しよう！

import os
import datetime

# htmlファイルを作成する
today = datetime.date.today() # 現在の「年-月-日」を読み取る
path = 'E:\EveryDayMemo\ ' + str(today) + '.html'

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
        # 2はリンクとそのリンク先の説明を書く
        text_urll = str(input(f"リンクをコピペ>>"))
        text_urlm = str(input(f"リンクのメモ　>>"))
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