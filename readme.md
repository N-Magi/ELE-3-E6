# ELE-3-E6 仕様策定
基板作成及びドキュメント
及びPyVisaを使用したPython自動計測スクリプト
## 全般
#### 電源周り
|項目|値|
|:---:|:---:|
|VCC|5V + 7V|
|電源電圧過電圧保護(シャットダウン)|[12V~](https://akizukidenshi.com/catalog/g/gI-07497/)|
|信号入力過電圧保護(クランプ)|[3.6V~](https://akizukidenshi.com/catalog/g/gI-08709/)| 
|電源入力端子|バナナ|

#### トランジスタ

- TO-92パッケージ ECB配列 ([2sc1815](https://akizukidenshi.com/catalog/g/gI-11344/) 系 V<sub>EBO</sub> = 5V V<sub>CEO</sub> = 50V V<sub>CBO</sub> = 60V

#### 抵抗

- 1W 金皮
- R<sub>L</sub> : <span style="color: red; ">きまってない</span>

#### ケース

- <span style="color: red; ">きまってない</span> (アクリルって透明だしキレイですよね)

####  UI

- 過電圧表示(LED)

## No.1 Trスイッチング基礎特性

#### C<sub>s</sub>コンデンサ

- <span style="color: red; ">きまってない</span> 

#### 測定端子
※BNCのみ基板備え付け

※バナナは基本的に筐体備え付け　コネクタ接続式
- 1 * 信号入力(Vin) : BNC/バナナ コンパチ
- 1 * 信号出力(Vout) : BNC/バナナ コンパチ
- 電圧入力
  - VCC : バナナ
  - GND : バナナ
- 測定
  - VCC : ばなな
  - Vin : バナナ
  - GND : バナナ
  - V<sub>A</sub> : バナナ
  - V<sub>A'</sub> : バナナ
  - V<sub>C</sub> : バナナ

#### UI

- 1 * Toggle SW(No.1,2切り替え用)
- なし(Pulse/DC は入力端子に接続する計測器で決める)

## No2.スイッチ回路の特性

#### ダイオード(D1)

- [１Ｎ４１４８　１００Ｖ２００ｍＡ](https://akizukidenshi.com/catalog/g/gI-00941/)

#### 測定端子
※BNCのみ基板備え付け

※バナナは基本的に筐体備え付け　コネクタ接続式
- 1 * 信号入力(Vin) : BNC/バナナ コンパチ
- 1 * 信号出力(Vout) : BNC/バナナ コンパチ
- 電圧入力
  - VCC : バナナ
  - GND : バナナ
- 測定
  - VCC : ばなな
  - Vin : バナナ
  - GND : バナナ
  - V<sub>Z</sub> : バナナ
  - V<sub>C</sub> : バナナ

#### UI

- 1 * Toggle SW(No.1,2切り替え用)
- 2 * Toggle SW

