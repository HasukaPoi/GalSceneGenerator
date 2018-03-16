# GalSceneGenerator
A tool to fast generate a galgame-liked picture, wrote by python.<br>
一个使用Python编写的能够快速生成类似于GalGame游戏画面的图片的工具。

## Update Footprint 升级足迹
- 2018/3/10: 本项目诞生并产生第一份代码
- 2018/3/15: 加入本栏目
- 2018/3/17: 完善了总四行的文字布局、移除除概述栏外的英文描述（好麻烦）。

## How to Use 如何使用
1. 确认你的机器上安装了Python和pip。
1. 运行 ```pip install pillow```来安装PIL库。
1. 克隆一份这个仓库到本地。
1. 在仓库文件夹中运行python（命令行）。
1. ```import galscene```
1. 使用  ```galscene.gen()```

以下是```gen()```函数的参数定义：

全都可以留空。留空的时候会调用/default里的文件

- image: 背景图片，尺寸必须为**1280\*720**
- filt: 对话框背景，**目前请留空**。因为代码中该图像放置在背景中的坐标是固定的。
- text0: 说话人名字栏，会自动在两侧加上方括号。留空则不显示。
- text1,2,3: 三行本文。
- ttf: 字体文件。（默认为思源黑体 Medium(SourceHanSans-Medium.otf)）（由于文件尺寸，没有放在此repo里）

## Known Problems and TODO 已知问题和需要改进的地方
Which mentioned in the above is almost the all. And...<br>基本上就是上面说到的那些，以及……

1. 不能更改文字颜色。

1. 没有文字阴影（和其他特效）

## Dependencies 依赖
[Pillow](https://pypi.python.org/pypi/Pillow)

## Environment 环境
Windows 10, Python 3