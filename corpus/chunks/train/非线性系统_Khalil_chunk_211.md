# 7.1.1 圆判据

定理 7.1 如果满足下列条件这一,则系统(7.1)\~(7.3)是绝对稳定的。

- $\psi \in [K_1, \infty)$ ，且 $G(s)[I + K_1 G(s)]^{-1}$ 是严格正实的，  
- $\psi \in [K_1, K_2]$ , 其中 $K = K_1 - K_2 = K^{\mathrm{T}} > 0$ , 且 $[I + K_2G(s)][I + K_1G(s)]^{-1}$ 是严格正实的。

如果仅在集合 $Y \subset R^{P}$ 上满足扇形区域条件, 则上述条件保证系统是有限区域绝对稳定的。

该定理称为多变量圆判据,将其用于标量条件情况下就会理解其含义。方程(7.4)对任意 $\psi\in[K_{1},\infty]$ 或 $\psi\in[K_{1},K_{2}]$ 有唯一解u的必要条件是矩阵 $(I+K_{1}D)$ 为非奇异阵。在方程(7.4)中取 $\psi=K_{1}y$ 即可得到这个结论。因此,传递函数 $[I+K_{1}G(s)]^{-1}$ 是正则的。

证明:首先在扇形区域 $[0,\infty]$ 上证明定理,然后通过环路变换扩展到其他情况。如果 $\psi\in[0,\infty]$ 和 $G(s)$ 是严格正实的,就得到两个无源系统的反馈连接。由引理6.4可知,线性动力学系统的存储函数为 $V(x)=(1/2)x^{\mathrm{T}}Px$ ,这里 $P=P^{T}>0$ ,满足Kalman-Yakubovich-Popov方程

$$P A + A ^ {\mathrm{T}} P = - L ^ {\mathrm{T}} L - \varepsilon P \tag {7.6}P B = C ^ {\mathrm{T}} - L ^ {\mathrm{T}} W \tag {7.7}W ^ {\mathrm{T}} W = D + D ^ {\mathrm{T}} \tag {7.8}$$

$\varepsilon>0$ 。以 $V(x)$ 作为备选李雅普诺夫函数，得

$$\dot {V} = \frac {1}{2} x ^ {\mathrm{T}} P \dot {x} + \frac {1}{2} \dot {x} ^ {\mathrm{T}} P x = \frac {1}{2} x ^ {\mathrm{T}} (P A + A ^ {\mathrm{T}} P) x + x ^ {\mathrm{T}} P B u$$

利用方程(7.6)和方程(7.7)得

$$
\begin{array}{l} \dot {V} = - \frac {1}{2} x ^ {\mathrm{T}} L ^ {\mathrm{T}} L x - \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x + x ^ {\mathrm{T}} \left(C ^ {\mathrm{T}} - L ^ {\mathrm{T}} W\right) u \\ = - \frac {1}{2} x ^ {\mathrm{T}} L ^ {\mathrm{T}} L x - \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x + (C x + D u) ^ {\mathrm{T}} u - u ^ {\mathrm{T}} D u - x ^ {\mathrm{T}} L ^ {\mathrm{T}} W u \\ \end{array}
$$

利用方程(7.8)和 $u^{T}Du=\frac{1}{2}u^{T}(D+D^{T})u$ ，得

$$\dot {V} = - \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x - \frac {1}{2} (L x + W u) ^ {\mathrm{T}} (L x + W u) - y ^ {\mathrm{T}} \psi (t, y)$$

由于 $y^{\mathrm{T}}\psi (t,y)\geqslant 0$ ，所以有

$$\dot {V} \leqslant - \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x$$

该式说明原点是全局指数稳定的。如果 $\psi$ 仅对 $y \in Y$ 满足扇形区域条件, 那么上述分析在原点的某个邻域内成立, 这就证明原点是指数稳定的。 $\psi \in [K_1, \infty]$ 的情况可以通过图7.2所示的环路变换, 转换为属于 $[0, \infty]$ 的非线性问题。因此, 如果 $G(s)[I + K_1 G(s)]^{-1}$ 是严格正实的, 则系统绝对稳定。而 $\psi \in [K_1, K_2]$ 的情况可以通过图7.3所示的环路变换, 转换为属于 $[0, \infty]$ 的非线性问题。因此, 如果

$$I + K G (s) [ I + K _ {1} G (s) ] ^ {- 1} = [ I + K _ {2} G (s) ] [ I + K _ {1} G (s) ] ^ {- 1}$$

是严格正实的,则系统是绝对稳定的。

![](image/1017c8e733880dda829431b719959e7a670ce4b4e64ff0b763c0c20a3ca5d91c.jpg)

<details>
<summary>flowchart</summary>
