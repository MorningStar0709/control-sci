# 7.5.1 问题描述

设被控对象为

$$\ddot {\theta} + a _ {1} \dot {\theta} + a _ {2} \theta = a u \tag {7.20}$$

式中， $\theta$ 为系统输出转角；u 为控制输入； $a_{1}$ 、 $a_{2}$ 为非负的实数，未知；a 为正实数，未知。

定义参考模型为

$$\ddot {\theta} _ {m} + b _ {1} \dot {\theta} _ {m} + b _ {2} \theta_ {m} = b r \tag {7.21}$$

式中， $\theta_{m}$ 为模型输出；r 为系统指令输入； $b_{1}$ 、 $b_{2}$ 、b 为已知正实数。

定义误差信号为

$$e = \theta_ {m} - \theta \tag {7.22}$$

由式（7.20）～式（7.22）得到误差动态方程：

$$\ddot {e} + b _ {1} \dot {e} + b _ {2} e = b r - a u + (a _ {1} - b _ {1}) \dot {\theta} + + (a _ {2} - b _ {2}) \theta \tag {7.23}$$

定义 $\varepsilon=\left[e\quad\dot{e}\right]^{T}$ ，则得到误差状态方程如下

$$
\dot {\varepsilon} = A \varepsilon - \left[ \begin{array}{l} 0 \\ a \end{array} \right] u + \left[ \begin{array}{l} 0 \\ \Delta \end{array} \right] \tag {7.24}
$$

式中， $\Delta=br+\left(a_{1}-b_{1}\right)\dot{\theta}+\left(a_{2}-b_{2}\right)\theta;\quad A=\begin{bmatrix}0&1\\ -b_{2}&-b_{1}\end{bmatrix}$ 。

![](image/46ed35ac038edc3d50c63c9f64ebb46605fec0b5233300c3f84d30619aadb933.jpg)
