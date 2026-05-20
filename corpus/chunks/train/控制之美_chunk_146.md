# 8.3 根轨迹的几何性质

本节将讨论根轨迹的几何性质，首先来复习复数的三种表达形式。

(1) 代数形式: $z = \sigma + \mathrm{j}\omega$ , 其中, $\mathrm{j} = \sqrt{-1}$ , 是虚数单位; $\sigma$ 是复数的实部; $\omega$ 是复数的虚部。

![](image/ac01e335f444ddedd7fcd6558a6fde1a226c64b582a76f47dc77815b47beb063.jpg)

(2) 向量形式(如图 8.3.1 所示): 通过复数的复角、 $\varphi$ (相位)和模 M(绝对值)来表达。根据三角形的几何关系, 其中 $\varphi = \angle z = \arctan \frac{\omega}{\sigma}, M = |z| = \sqrt{\sigma^{2} + \omega^{2}}, \varphi$ 以逆时针方向为正。

（3）指数形式：由图8.3.1的几何关系可得 $\sigma = M\cos \varphi, \omega = M\sin \varphi$ 。所以 $z = \sigma + j\omega = M\cos \varphi + jM\sin \varphi = M(\cos \varphi + j\sin \varphi)$ 。根据欧拉公式（Euler's Formula）： $\cos \varphi + j\sin \varphi = e^{j\varphi}$ ，可得 $z = M e^{j\varphi}$ 。

![](image/9af3e75fce8fdec57878d66bb73c82fc9f480af1560a1166cafbe9a3f8ac041c.jpg)

<details>
<summary>text_image</summary>

jω
ω
M
φ
O
σ
σ
</details>

图8.3.1 复数的三种表达形式

根据上述定义，两个复数 $z_{1} = \sigma_{1} + \mathrm{j}\omega_{1} = M_{1}\mathrm{e}^{\mathrm{j}\varphi_{1}}$ 和 $z_{2} = \sigma_{2} + \mathrm{j}\omega_{2} = M_{2}\mathrm{e}^{\mathrm{j}\varphi_{2}}$ 相乘得到

$$
z _ {1} z _ {2} = M _ {1} \mathrm{e} ^ {\mathrm{j} \varphi_ {1}} M _ {2} \mathrm{e} ^ {\mathrm{j} \varphi_ {2}} = M _ {1} M _ {2} \mathrm{e} ^ {\mathrm{j} (\varphi_ {1} + \varphi_ {2})} \tag {8.3.1a}
$$

它们的比值为

$$
\frac {z _ {1}}{z _ {2}} = \frac {M _ {1} \mathrm{e} ^ {\mathrm{j} \varphi_ {1}}}{M _ {2} \mathrm{e} ^ {\mathrm{j} \varphi_ {2}}} = \frac {M _ {1}}{M _ {2}} \mathrm{e} ^ {\mathrm{j} (\varphi_ {1} - \varphi_ {2})} \tag {8.3.1b}
$$

根据式(8.3.1)，当 $s=\sigma+j\omega$ 时，传递函数 $G(s)=\frac{N(s)}{D(s)}=\frac{(s-s_{z1})(s-s_{z2})\cdots(s-s_{zm})}{(s-s_{p1})(s-s_{p2})\cdots(s-s_{pn})}$ 的模为

$$
M = | G (s = \sigma + \mathrm{j} \omega) | = \frac {\prod \text {零点到} s \text {的距离}}{\prod \text {极点到} s \text {的距离}} \Bigg | _ {s = \sigma + \mathrm{j} \omega} \tag {8.3.2a}
$$

复角为

$$
\varphi = \angle G (s = \sigma + \mathrm{j} \omega) = \left(\sum \text {零点到} s \text {的夹角} - \sum \text {极点到} s \text {的夹角}\right) \Big | _ {s = \sigma + \mathrm{j} \omega} \tag {8.3.2b}
$$

为了进一步理解式(8.3.2)，请参考以下例子。

例 8.3.1 求当 $s = -1 + \sqrt{3}j$ 时传递函数 $G(s) = \frac{s + 2}{s(s + 1)}$ 的值。

解：方法一：直接将 $s = -1 + \sqrt{3}\mathrm{j}$ 代入 $G(s) = \frac{s + 2}{s(s + 1)}$ ，可得

$$
G (s = - 1 + \sqrt {3} \mathrm{j}) = \frac {- 1 + \sqrt {3} \mathrm{j} + 2}{(- 1 + \sqrt {3} \mathrm{j}) (- 1 + \sqrt {3} \mathrm{j} + 1)} = - \frac {1}{2} - \frac {\sqrt {3}}{6} \mathrm{j} \tag {8.3.3a}
$$
