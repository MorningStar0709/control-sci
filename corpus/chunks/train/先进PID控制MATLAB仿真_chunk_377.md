# 7.5.3 仿真实例

设被控对象为

$$\ddot {\theta} + 2 0 \dot {\theta} + 2 5 \theta = 1 3 3 u$$

参考模型为

$$\ddot {\theta} _ {m} + 2 0 \dot {\theta} _ {m} + 3 0 \theta_ {m} = 5 0 r$$

则 $A=\begin{bmatrix}0&1\\ -b_{2}&-b_{1}\end{bmatrix}=\begin{bmatrix}0&1\\ -30&-20\end{bmatrix}$ ，在 MATLAB 下，运行 $\mathrm{eig}(A)$ 可得 A 的特征值为 -1.6334 和 -18.3666。

指令信号分两种，当 S=1 时为方波，当 S=2 时为正弦。取 S=1，即指令信号为方波，MATLAB 表示为 $r=\operatorname{sgn}\left(\sin\left(0.1\pi t\right)\right)$ ，控制器参数取 $\lambda_{0}=\lambda_{1}=\lambda_{2}=200$ ，取 $Q=\begin{bmatrix}20&10\\ 10&20\end{bmatrix}$ 。

采用 M 语言进行仿真，可得 $P=\begin{bmatrix}12.1667&0.3333\\0.3333&0.5167\end{bmatrix}$ 。仿真中，被控对象初始状态取为 [0.5,0]，参考模型初始状态取为 [0,0]。

采用控制律式（7.27）和自适应律式（7.29），自适应参数 $k_{0}$ 、 $k_{1}$ 、 $k_{2}$ 的初始状态取为[0,0,0]。仿真结果如图7-13～图7-15所示，图7-13所示为参考模型位置跟踪及跟踪误差，图7-14所示为控制器输出，图7-15所示为控制器参数 $k_{0}$ 、 $k_{1}$ 、 $k_{2}$ 的自适应变化过程。还可以采用Simulink实现控制系统的仿真，程序附后。

![](image/dca8179807840322476a8e91d6c4be139baaa724f3ba8163448cea2069b17614.jpg)  
图 7-13 位置跟踪及跟踪误差

![](image/bb5ba639a89a0c7c58bed24999e6300acdcb94f86b64f19f291c536347256836.jpg)

<details>
<summary>line</summary>

| Time(s) | Control input |
| --- | --- |
| 0 | 0.3 |
| 10 | -0.6 |
| 20 | 0.8 |
| 30 | -0.6 |
| 40 | 0.6 |
| 50 | -0.6 |
| 60 | -0.3 |
</details>

图 7-14 控制器输出信号

![](image/93a546671a298c348f9eb5a8adb5948562362c4c24b6f15681c9619395da2022.jpg)

<details>
<summary>line</summary>

| Time(s) | k0 |
| --- | --- |
| 0 | 0.5 |
| 10 | 0.5 |
| 20 | 0.5 |
| 30 | 0.5 |
| 40 | 0.5 |
| 50 | 0.5 |
| 60 | 0.5 |
</details>

![](image/6bb38600a687d8e3fe5baf139511da7144f3f827c28dd5d2dc5d73ce0fee18c2.jpg)

<details>
<summary>line</summary>

| Time(s) | k1 |
| --- | --- |
| 0 | 0.0 |
| 10 | -0.2 |
| 20 | 0.2 |
| 30 | -0.2 |
| 40 | 0.2 |
| 50 | -0.2 |
| 60 | 0.0 |
</details>

![](image/7243737bcaa88e1cf3c033f9e696aed4926378d0a1eb9552a98ad8f3b9c70019.jpg)

<details>
<summary>line</summary>

| Time(s) | k2 |
| --- | --- |
| 0 | -0.5 |
| 10 | -0.5 |
| 20 | 0 |
| 30 | 0 |
| 40 | 0 |
| 50 | 0 |
| 60 | 0 |
</details>

图 7-15 $k_{0}$ 、 $k_{1}$ 、 $k_{2}$ 的变化过程
