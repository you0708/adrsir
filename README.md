# 赤外線学習リモコン基板 ADRSIR 関連スクリプト
株式会社ビット・トレード・ワンが販売する赤外線学習リモコン基板 ADRSIR (http://bit-trade-one.co.jp/product/module/adrsir/) を使って赤外線データを扱うための Python スクリプト。

* adrsir.py
  * ADRSIR の送受信をするためのライブラリ
* ir_control.py
  * ADRSIR を使って赤外線データを扱うコマンドラインツール
* ir_data
  * データ保存用ディレクトリ

## HOW TO USE
### インストール
```
$ git clone https://github.com/you0708/adrsir.git
$ cd adrsir
```

### 学習させた赤外線データの保存
```
$ ./ir_control.py save tv
[*] saved ir_data/tv/ch0.data
[*] saved ir_data/tv/ch1.data
[*] saved ir_data/tv/ch2.data
[*] saved ir_data/tv/ch3.data
[*] saved ir_data/tv/ch4.data
[*] saved ir_data/tv/ch5.data
[*] saved ir_data/tv/ch6.data
[*] saved ir_data/tv/ch7.data
[*] saved ir_data/tv/ch8.data
[*] saved ir_data/tv/ch9.data
```

### 任意の赤外線データの送信
```
$ ./ir_control.py send tv/ch0.data
[*] send ir_data/tv/ch0.data
```

### 保存した赤外線データの書き戻し
```
$ ./ir_control.py restore tv
[*] restore IR data from ir_data/tv
[*] writing ir_data/tv/ch0.data into ch0
[*] writing ir_data/tv/ch1.data into ch1
[*] writing ir_data/tv/ch2.data into ch2
[*] writing ir_data/tv/ch3.data into ch3
[*] writing ir_data/tv/ch4.data into ch4
[*] writing ir_data/tv/ch5.data into ch5
[*] writing ir_data/tv/ch6.data into ch6
[*] writing ir_data/tv/ch7.data into ch7
[*] writing ir_data/tv/ch8.data into ch8
[*] writing ir_data/tv/ch9.data into ch9
[*] restored
```

## 参考情報
* 本日も元気に赤外線照射中の皆様へ、ソフトウェアアップデートのお知らせです！
  * http://bit-trade-one.co.jp/blog/20180219/
* リモコンいじり放題！！ラズパイ専用 学習リモコン基板で使えるソフトウェア3種詰め合わせ公開 | Bit Trade One, LTD
  * http://bit-trade-one.co.jp/blog/2017121302/
* tokieng/adrsirlib: ADRSIR(ビットトレードワン製赤外線送受信機) 用のライブラリ
  * https://github.com/tokieng/adrsirlib

## License
Apache License 2.0. See [LICENSE](/LICENSE).
