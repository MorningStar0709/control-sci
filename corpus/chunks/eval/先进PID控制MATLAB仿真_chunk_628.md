# 『仿真程序』

（1）主程序：dlb.m，包括调用示意图程序 model.jpg、倒立摆模型的数学描述、LQR 算法的计算、界面的创建、扰动的设定和仿真参数的设定等。由于程序较长，见本书的配书程序包。  
（2）演示界面程序：采用 GUI 设计环境进行设计，程序名为 dll.fig，如图 16-10 所示。

通过 MATLAB 命令“guide”可打开 GUI 设计环境。在 MATLAB 环境下输入“guide.dlb.fig”可打开倒立摆控制的演示界面程序进行设计或修改。

![](image/71b96e33968e8ece25107427571e6efc8fc10afc91d8001b7392eb36c0304281.jpg)

<details>
<summary>text_image</summary>

d1b.fig
File Edit View Layout Tools Help
Experiment Platform of Virtual Inverted Pendulum
实验模型
模型参数
sys3
M=
1 kg
L=
1 m
m=
1 kg
g=9.8m/s²
初始值*
水平位置 0 m
< 0>
摆杆角度 0 rad
< 0>
启动仿真
仿真
仿真时间 10 s
步长值 0.1 s
启动仿真
Angle
ag
Angle_Velocity
av
Displace
dp
Velocity
dv
3D仿真
T=
sys1
LQR 最优控制
S 0 0 0
Q=
0 S 0 0
0 0 S 0
0 0 0 S
R=
5
计算K值
重置 退出
K=[ ]
</details>

图 16-10 倒立摆控制系统的 GUI 设计界面

（3）倒立摆示意图，文件名为 model.jpg，如图 16-11 所示，该图为手工绘制。

![](image/bead1de8d76ad351147f1fde4af04a66b48bdbae27c6c1bcc8a5ccbb428f541b.jpg)

<details>
<summary>text_image</summary>

m
L
Angle
M
</details>

图 16-11 倒立摆示意图
