# 4.2.1 典型一阶系统和典型系统输入信号

典型一阶系统的微分方程为

$$\frac {\mathrm{d} x (t)}{\mathrm{d} t} + a x (t) = a u (t) \tag {4.2.1}$$

其中， $a$ 是一个常数。考虑零初始条件 $x(0) = u(0) = 0$ ，对式(4.2.1)等号两边进行拉普拉斯变换，可得

$$s X (s) + a X (s) = a U (s) \tag {4.2.2}$$

调整后可以得到系统的传递函数为

$$G (s) = \frac {X (s)}{U (s)} = \frac {a}{s + a} \tag {4.2.3}$$

$G(s)$ 的极点是 $s_{p}=-a$ 。

下面介绍两个典型的系统输入信号。

单位冲激函数(见2.1.1节)，定义为

$$
\left\{ \begin{array}{l} \delta (t) = 0, t \neq 0 \\ \int_ {- \infty} ^ {\infty} \delta (t) \mathrm{d} t = 1 \end{array} \right. \tag {4.2.4}
$$

其拉普拉斯变换为

$$\mathcal {L} [ \delta (t) ] = \int_ {0} ^ {\infty} \delta (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathrm{e} ^ {- s 0} = 1 \tag {4.2.5}$$

单位阶跃函数(Unit Step): 读者可以在英语国家的一些公共场所看到小心台阶(Watch Your Step)的警示牌, 如图 4.2.1(a)所示。“阶跃”(Step)可以理解为一个台阶。“单位”阶跃是指幅度为 1 的阶跃函数, 如图 4.2.1(b)所示。它的数学表达式为

$$
u (t) = \left\{ \begin{array}{l l} 1, & t \geqslant 0 \\ 0, & t <   0 \end{array} \right. \tag {4.2.6}
$$

其对应的拉普拉斯变换为

$$\mathcal {L} [ 1 ] = \mathcal {L} \left[ \mathrm{e} ^ {- 0 t} \right] = \frac {1}{s + 0} = \frac {1}{s} \tag {4.2.7}$$

![](image/f395eb9a4f897cf4cc592fddf6dbba2c544d7673bf6b61e72c279936cf9d7856.jpg)

<details>
<summary>text_image</summary>

CAUTION
Watch
Your Step.
</details>

(a) 小心台阶(Watch Your Step)   
![](image/e96a795405697602551bc672de06c0d509dc41ec12341e730a3e3ed2e15f3875.jpg)

<details>
<summary>line</summary>

| t | u(t) |
| --- | --- |
| 0 | 1 |
| t = 0 | 1 |
</details>

(b) 单位阶跃函数  
图4.2.1 单位阶跃函数理解与图示
