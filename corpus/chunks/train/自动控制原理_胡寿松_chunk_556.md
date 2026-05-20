# (2) 死区与滞环继电非线性环节

注意到滞环与输入信号及其变化率的关系,通过作图法获得 $y(t)$ 如图 8-38 所示。输出 $y(t)$ 的数学表达式为

$$
y (t) = \left\{ \begin{array}{l l} 0, & 0 \leqslant \omega t <   \psi_ {1} \\ M, & \psi_ {1} \leqslant \omega t \leqslant \psi_ {2} \\ 0, & \psi_ {2} <   \omega t \leqslant \pi \end{array} \right. \tag {8-73}
$$

![](image/2c0a5bb80d6d848d3dbe93cd892b13e9f3f90acff64e140b21e5558854c60eca.jpg)

<details>
<summary>text_image</summary>

y
M
0
mh
h
x
y
0
ψ₁
ψ₂
π+ψ₂
2π-ψ₁
2π
ωt
ωt
</details>

图 8-38 死区滞环继电特性和正弦响应曲线

图中，由于非线性特性导致 $y(t)$ 产生不同线性变化的区间端点为

$$\psi_ {1} = \arcsin \frac {h}{A} \tag {8-74}\psi_ {2} = \pi - \arcsin \frac {m h}{A} \tag {8-75}$$

由图 8-38 可见, $y(t)$ 为奇对称函数,而非奇函数,由式(8-60)

$$A _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} y (t) \cos \omega t d \omega t = \frac {2}{\pi} \int_ {\psi_ {1}} ^ {\psi_ {2}} M \cos \omega t d \omega t = \frac {2 M h}{\pi A} (m - 1)B _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} y (t) \sin \omega t d \omega t = \frac {2}{\pi} \int_ {\phi_ {1}} ^ {\phi_ {2}} M \sin \omega t d \omega t= \frac {2 M}{\pi} \left[ \sqrt {1 - \left(\frac {m h}{A}\right) ^ {2}} + \sqrt {1 - \left(\frac {h}{A}\right) ^ {2}} \right]$$

死区滞环继电特性的描述函数为

$$N (A) = \frac {2 M}{\pi A} \left[ \sqrt {1 - \left(\frac {m h}{A}\right) ^ {2}} + \sqrt {1 - \left(\frac {h}{A}\right) ^ {2}} \right] + \mathrm{j} \frac {2 M h}{\pi A ^ {2}} (m - 1), \qquad A \geqslant h \tag {8-76}$$

取 h=0，得理想继电特性的描述函数为

$$N (A) = \frac {4 M}{\pi A} \tag {8-77}$$

取 $m = 1$ ，得死区继电特性的描述函数为

$$N (A) = \frac {4 M}{\pi A} \sqrt {1 - \left(\frac {h}{A}\right) ^ {2}}, \qquad A \geqslant h \tag {8-78}$$

取 $m = -1$ ，得滞环继电特性的描述函数为

$$N (A) = \frac {4 M}{\pi A} \sqrt {1 - \left(\frac {h}{A}\right) ^ {2}} - \mathrm{j} \frac {4 M h}{\pi A ^ {2}}, \qquad A \geqslant h \tag {8-79}$$

表 8-1 列出了一些典型非线性特性的描述函数,以供查用。

表 8-1 非线性特性及其描述函数
