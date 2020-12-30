# 測距センサモジュールの計測値をサーボモータに出力する
## 使用ライブラリ（想定）
- pigpio
- VL53L1X
- smbus2

# 仮想環境を作る

```bash
$ python3 -m venv .
```

# 仮想環境について

仮想環境を立ち上げる
```bash
$ source bin/activate
```
仮想環境を停止する
```bash
deactivate
```

# 必要なライブラリをインストール
仮想環境を立ち上げた状態で実行する
```bash
([仮想環境名]) ~ $
```

```bash
$ pip install pigpio vl53l1x smbus2
``` 

```bash
$ pip list
Package       Version
------------- -------
pigpio        1.78   
pip           18.1   
pkg-resources 0.0.0  
setuptools    40.8.0 
smbus2        0.4.0  
VL53L1X       0.0.5  
```

# 現状の動作
今回使用したサーボモータのパルス幅の範囲は`500 ~ 2500`

測距センサモジュール計測距離を最大70cmまでとして、
計測した対象までの距離(cm)を以下の式でパルス値を計算。

```python
pulse = int((distance / 70) * 1900 + 500)
```

計算したパルス幅をサーボモータに伝えてモータの位置を制御。