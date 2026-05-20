# 17.1 单级倒立摆建模

倒立摆系统的控制问题一直是控制研究中的一个典型问题。控制的目标是通过给小车底座施加一个力 $u$ （控制量），使小车停留在预定的位置，并使摆杆不倒下，即不超过一预先定义好的垂直偏离角度范围。图17-1为一级倒立摆的示意图，小车质量为 $M$ ，摆杆的质量为 $m$ ，小车位置为 $x$ ，摆杆的角度为 $\theta$ 。

![](image/8676abc22c9c100e49411b09e7539ffea77a3b93e309919f22e5daf21733e560.jpg)

<details>
<summary>text_image</summary>

V
m
L
θ
G(xG, yG)
O
u
M
H
x
</details>

图 17-1 倒立摆系统示意图

设摆杆偏离垂直线的角度为 $\theta$ ，同时规定摆杆质心的坐标为 $(x_{\mathrm{G}},y_{\mathrm{G}})$ ，则

$$x _ {\mathrm{G}} = x + l \sin \thetay _ {\mathrm{G}} = l \cos \theta$$

则根据牛顿力学定律，建立水平和垂直运动状态方程。摆杆围绕其质心的转动运动可用力矩方程来描述。

$$I \ddot {\theta} = V l \sin \theta - H l \cos \theta$$

式中，I 为摆杆围绕其质心的转动惯量；V 为小车对摆杆的垂直分力；H 为小车对摆杆的水平分力。

摆杆质心的水平运动由下式描述。

$$m \frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} (x + l \sin \theta) = H$$

摆杆质心的垂直运动由下式描述。

$$m \frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} l \cos \theta = V - m g$$

小车的水平运动由下式来描述。

$$M \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = u - H$$

假设 $\theta$ 很小， $\sin\theta\approx\theta,\quad\cos\theta\approx1$ 。则以上各式变为

$$I \ddot {\theta} = V l \theta - H l \tag {17.1}m (\ddot {x} + l \ddot {\theta}) = H \tag {17.2}0 = V - m g \tag {17.3}M \ddot {x} = u - H \tag {17.4}$$

由式（17.2）和式（17.4）得

$$(M + m) \ddot {x} + m l \ddot {\theta} = u \tag {17.5}$$

由式（17.1）和式（17.3）得

$$(I + m l ^ {2}) \ddot {\theta} + m l \ddot {x} = m g l \theta \tag {17.6}$$

由式（17.5）和式（17.6）可得单级倒立摆方程

$$\ddot {\theta} = \frac {m (m + M) g l}{(M + m) I + M m l ^ {2}} \theta - \frac {m l}{(M + m) I + M m l ^ {2}} u \tag {17.7}\ddot {x} = - \frac {m ^ {2} g l ^ {2}}{(M + m) I + M m l ^ {2}} \theta + \frac {I + m l ^ {2}}{(M + m) I + M m l ^ {2}} u \tag {17.8}$$

式中， $I=\frac{1}{12}mL^{2}$ ; $l=\frac{1}{2}L$ 。

![](image/4e8a8b01e3e7658bf3e6c4df8fa5548526e43121675cf0b36f7f2ac3abb282ed.jpg)
