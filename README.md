
## 環境構築

ライブラリはrequirement.txtに記載
pythonバージョンは3.6~3.9なら多分動くと思う,,


## プログラムの起動方法

①cd annotation                               #READMEとかがあるプログラムのディレクトリに移動する
②python manage.py runserver	       	　    #サーバーを起動
③ブラウザでhttp://127.0.0.1:8000/にアクセスする



## 動画データを入れておく場所

 /mainapp/static/以下に入れる



## ラベル付けされた結果のAnswerファイルの出力場所
　
　/answer/以下に"日時.txt形式"で出力される


## カスタマイズできる場所

 view.py　表示やデータ保存の制御についてはここ
 template/video.html 表示するHTMLファイルについてはここ



