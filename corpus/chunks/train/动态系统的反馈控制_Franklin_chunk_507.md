# 7.3节习题

7.1 写出如图 7.83 所描述电路的动态方程。将方程写成 $y(t)$ 的二阶微分方程形式。假设输入为零，用拉普拉斯变换法解关于 $y(t)$ 的微分方程，参数值和初始条件如图所示。在 Matlab 中，用 initial 命令验证答案。

![](image/9701f01d038e17dbfb1123ad9c5509c535f0ae6b70080cdc50da53bc8de32ded.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with inductors, capacitor, and voltage source labeled with parameters L=1H, R=2Ω, C=1F, and output y(t)
</details>

图7.83 习题7.1的电路

递恢复法有何优势？

7.10 在反馈控制中，使用估计器的主要原因是什么？

7.11 如果估计器增益为 L，给出由估计器产生的闭环极点的一个表达式。

7.12 在什么条件下，可以选取估计器增益 L 使得 $\alpha_{e}(s)=0$ 的根是任意的？

7.13 如果选定的参考输入使得估计器的输入与过程的输入相同，整个系统的闭环传递函数是什么？

7.14 如果引入的参考输入使得零点能配置为 $\gamma(s)$ 的根，整个系统的闭环传递函数是什么？

7.15 在状态反馈控制设计方法中，引入积分控制的三种标准方法是什么？

7.2 用于引力探测 B(GP-B)实验的卫星科学探索器发射于 2004 年 4 月 30 日，原理图如图 7.84 所示。假设航天器加上氦气瓶的总质量 $m_{1}$ 为 2000kg。探测器质量为 $m_{2}$ 为 1000kg。转子将会悬浮在探测器内，并且被迫跟随电容驱动机制的探测器。耦合的弹簧劲度系数 k 大小为 $3.2 \times 10^{6}$ ，黏性阻尼 b 大小为 $4.6 \times 10^{3}$ 。

![](image/fc8df4ac078817d1c2a29f4b04abefe69cbd9fa627b7a294d2261bac6fe45c5f.jpg)

<details>
<summary>text_image</summary>

u
m₁
k
b
转子
m₂
y₁
y₂
</details>

图 7.84 GP-B 卫星探测器的示意图

(a) 用惯性位置变量 $y_{1}$ 和 $y_{2}$ 写出由物块 $m_{1}$ 和 $m_{2}$ 组成的系统运动的动态方程。

(b) 实际的扰动 u 是陨尘并且导致的移动也是很小的，因此，用标度变量 $z_{1}=10^{6}y_{1}$ ， $z_{2}=10^{6}y_{2}$ ，以及 v=1000u 改写方程。

(c) 对于物块 $m_{1}$ ，用状态 $x=\left[z_{1}\quad\dot{z}_{1}\quad z_{2}\quad\dot{z}_{2}\right]^{T}$ ，输出 $y=z_{2}$ ，脉冲输入 $u=10^{-3}\delta(t)$ (N·s)，把方程写成状态变量形式。

(d) 用数值将运动方程按如下的形式写入 Matlab，并定义 Matlab 系统：sysGPB = ss(A, B, C, D)，用 Matlab 命令脉冲 (sysGPB) 绘制由脉冲引起的响应曲线 y，这是转子必须遵循的信号。

$$\dot {x} = A x + B v \tag {7.281}y = C x + D v \tag {7.282}$$

(e) 用 Matlab 命令 p=eig(F) 寻找系统的极点(或根)，命令 z=tzero(A, B, C, D) 寻找系统的零点。
