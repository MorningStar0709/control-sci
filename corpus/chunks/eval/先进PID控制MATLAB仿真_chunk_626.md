# 16.2.4 演示界面的 GUI 设计

首先在 MATLAB 环境下输入 “guide” 便可进入 GUI 界面的设计。本系统的 GUI 界面文件为 dlb.fig，创建并保存该文件时，可自动生成主程序框架 dlb.m。

用户在主程序框架 dlb.m 下，在相应的 GUI 组件回调函数中描述模型和编写控制算法。通过在 MATLAB 环境下运行 “guide dlb.fig” 可打开 GUI 界面。

在本系统中，采用了 GUI 开发环境的触控按钮、静态文本、可编辑文本、滑动条、坐标轴等组件。以小车质量 “M” 的 GUI 界面设计为例，首先建立小车重量的 Edit text，将其属性 tag 标签定义为 “mc”。基于 GUI 的倒立摆控制动画演示如图 16-7 所示。

![](image/08c13576a0b61769938e309cdf6229fa68d7c431d6007dffb145a72a6ac4b326.jpg)

<details>
<summary>text_image</summary>

Experiment Platform of Virtual Inverted Pendulum
实验模型
模型参数
sys1
M=
kg
L=
m
m=
kg
gs9 Bm/s
初始值
水平位置
0
m
a
框杆角度
0
rad
s
30项真
T=
sys1
Angle
sg
Angle_Velocity
sv
Drplace
dp
Velocity
dv
LOR 最优化控制
Q=
0 0 0
0 0 0
0 0 0
0 0 0
R=
计算K值
仿真
仿真时间
10 s
步长值
0.1 s
启动仿真
重置
退出
K∈[ ]
</details>

图 16-7 倒立摆控制动画演示 GUI 程序

![](image/eda8c1be6e8aae06b6e94a91247b1b2cc0b475aff723e2e589b930522c2d18c6.jpg)
