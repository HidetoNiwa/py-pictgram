# py-pictgram
Pythonを用いたTokyo2020オリンピックのピクトグラム風画像生成スクリプト

## 動作確認済み環境

- Windows10
- Python3.7

## 必須ソフト

- Python3.7
  - [インストール方法（Python Japan）](https://www.python.jp/install/windows/install.html)
- OpenCV(Python)
  - [Python 3.8 に OpenCV 4.3 など環境を構築する(Qiita)](https://qiita.com/cointoss1973/items/92d82f9accb239a276a0)
- Numpy(Python)
  - [3分でできるNumPyのインストール方法(DeepAge)](https://deepage.net/features/numpy-install.html)

## アルゴリズム（概略）

1. 画像取り込み（pic.png）
2. 「ガウスフィルタ」で平滑化
3. 画像をグレースケールに変換
4. Otsuの2値化法で画像の2値化（白黒）
5. 2値化した画像を、東京オリンピック公式カラーに変換
