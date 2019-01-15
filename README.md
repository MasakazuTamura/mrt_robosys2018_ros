# mrt_robosys2018_ros
Robosys2018 homework2

## 概要
これは, ロボットシステム学の課題2で作成した ROS パッケージです.

### mrt_kadai.launch
Keybord の矢印キー入力に対応した LED を点灯させます. 他

#### led_liner
led_liner.py, Subscribe した値に応じて LED を点滅
- 仕様
  - Key_Lock: On の間, 矢印キーの入力を無視する

#### key_input
key_input.py, key_event に対応した値を Publish
- 受け付ける入力
   - up arrow key: 0
   - down arrow key: 1
   - right arrow key: 2
   - left arrow key: 3
   - Ctrl + S: False
   - Ctrl + R: True
   - Ctrl + C: ノード終了
   
## 環境
使用した機器等
- Raspberry Pi 3 Model B V1.2
  - Ubuntu 16.04 LTS
  - https://github.com/MasakazuTamura/mrt_devdr/tree/homework2 使用
- Tera Tarm
  - Windows10 上で動作
  - キー入力は Tera Tarm 上で行う

## 使用方法
1. `~/catkin_ws/src` にこのリポジトリを clone する
	```
  $ cd ~/catkin_ws/src
	$ git clone https://github.com/MasakazuTamura/mrt_robosys2018_ros.git
	```
1. `catkin_make` を実行
	```
	$ cd ~/catkin_ws
  $ catkin_make
	```
1. `mrt_kadai.launch` を実行
	```
	$ roslaunch mrt_robosys2018_ros mrt_kadai.launch
	```

1. やめるときは, `Ctrl + C` を押下

## 動画
URL: https://youtu.be/R8WHGmgdWFw
