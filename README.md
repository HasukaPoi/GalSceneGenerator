# GalSceneGenerator
A tool to fast generate a galgame-liked picture, wrote by python.<br>
一个使用Python编写的能够快速生成类似于GalGame游戏画面的图片的工具。

## How to Use 如何使用
1. Make sure that python installed. <br>确认你的机器上安装了Python。
1. Clone the repo to local. <br>克隆一份这个仓库到本地。
1. Run python in repo folder(with Bash, cmd, etc). <br>在仓库文件夹中运行python（命令行）。
1. ```import galscene```
1. Use 使用  ```galscene.gen()```

The args of ```gen()``` is like:<br>以下是```gen()```函数的参数定义：

All of them can be leave empty and the source in /default will be used.<br>
全都可以留空。留空的时候会调用/default里的文件

- image: Background, must be **1280\*720** <br>
image: 背景图片，尺寸必须为**1280\*720**
- filter: Background of text box. **Please leave it empty now** bcs the position of it is fixed in code right now.<br>
filter: 对话框背景，**目前请留空**。因为代码中该图像放置在背景中的坐标是固定的。
- text: The content of text box. Use \\n to make newline (**Line spacing not perfect now**)<br>
text: 对话框的内容。使用\\n来起新行（**但是现在行距不匹配**）
- ttf: Font file. (Default: SourceHanSans-Medium.otf) (Not included in this repo due to file size)<br>
ttf: 字体文件。（默认为思源黑体 Medium）（由于文件尺寸，没有放在此repo里）

## Known Problems and TODO 已知问题和需要改进的地方
Which mentioned in the above is almost the all. And...<br>基本上就是上面说到的那些，以及……

1. Missing a text area of speaker.<br>
没有说话人名的文本。

1. Text color can't be changed.<br>
不能更改文字颜色。

1. Not have a text shadow(and other effects).<br>
没有文字阴影（和其他特效）

## Dependencies 依赖
[Pillow](https://pypi.python.org/pypi/Pillow)

## Environment 环境
Windows 10, Python 3