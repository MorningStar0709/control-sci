$$a _ {1} = \frac {a}{2 j}c _ {1} = \frac {\omega}{\pi} \int_ {0} ^ {\pi / \omega} \psi (a \sin \omega t + y _ {h} (t)) \exp (- j \omega t) d t$$

根据方程(7.20)，当 $k = 1$ 时，有 $G(j\omega)c_{1} + a_{1} = 0$

引入函数 $\Psi^{*}(a,y_{h}) = \frac{c_{1}}{a_{1}} = j\frac{2\omega}{\pi a}\int_{0}^{\pi /\omega}\psi (a\sin \omega t + y_{h}(t))\exp (-j\omega t)dt$

可将方程改写为 $\frac{1}{G(j\omega)} +\Psi^{*}(a,y_{h}) = 0$ (7.35)

将 $\Psi(a)$ 加到方程(7.35)的两边, 可得

$$\frac {1}{G (j \omega)} + \Psi (a) = \delta \Psi \tag {7.36}$$

其中 $\delta\Psi=\Psi(a)-\Psi^{*}(a,y_{h})$

当 $y_{h} = 0$ 时， $\Psi^{*}(a,0) = \Psi (a)$ ，这样 $\delta \Psi = 0$ ，方程(7.36)简化为调和平衡方程

$$\frac {1}{G (j \omega)} + \Psi (a) = 0 \tag {7.37}$$

因此,调和平衡方程(7.37)是精确方程(7.36)的近似,虽然误差项 $\delta\Psi$ 不能精确求出,但通常可估计其大小。下一步是求 $\delta \Psi$ 的上界，为此，我们定义两个函数 $\rho (\omega)$ 和 $\sigma (\omega)$ 。首先在复平面内画出 $1 / G(j\omega)$ 的轨迹，在同一个平面内画出在实轴上以区间 $[- \beta, -\alpha]$ 为直径的(临界)圆。注意，由于 $\alpha \leqslant \Psi (a) \leqslant \beta$ ，故 $-\Psi (a)$ 的轨迹在实轴上的圆内。现在考虑一个 $\omega$ 值，使轨迹 $1 / G(j\omega)$ 对应的 $k\omega (k > 1)$ 的点位于临界圆外，如图7.19所示。这些点中任意一点到临界圆圆心的距离为

$$\left| \frac {\alpha + \beta}{2} + \frac {1}{G (j k \omega)} \right|$$

![](image/6477c4e5d509353aaab6c055e26e5ddf9ccd4771c7aeb6eb7e9042b0af32b223.jpg)

<details>
<summary>text_image</summary>

5ω
1/G(jω)
3ω
ρ(ω)
-β
-α
临界圆
ω
</details>

图7.19 求 $\rho (\omega)$

定义 $\rho (\omega) = \inf_{k > 1;k\mathrm{odd}}\left|\frac{\alpha + \beta}{2} +\frac{1}{G(jk\omega)}\right|$ (7.38)

注意,这里只对 $k=3,5,\cdots$ 时使 $1/G(jk\omega)$ 位于临界圆外的 $\omega$ 定义 $\rho(\omega)$ , 即 $\omega$ 属于集合

$$\Omega = \{\omega \mid \rho (\omega) > \frac {1}{2} (\beta - \alpha) \}$$

在 $\Omega$ 的任意连通子集 $\Omega'$ 上，定义 $\sigma(\omega) = \frac{\left(\frac{\beta - \alpha}{2}\right)^2}{\rho(\omega) - \frac{\beta - \alpha}{2}}$ (7.39)

正的 $\sigma(\omega)$ 就是误差项 $\delta\Psi$ 的上界, 这一点将在下面的引理中论述。

引理 7.1 在已述假设条件下,有

$$\frac {\omega}{\pi} \int_ {0} ^ {2 \pi / \omega} y _ {h} ^ {2} (t) d t \leqslant \left[ \frac {2 \sigma (\omega) a}{\beta - \alpha} \right] ^ {2}, \forall \omega \in \Omega^ {\prime} \tag {7.40}| \delta \Psi | \leqslant \sigma (\omega), \forall \omega \in \Omega^ {\prime} \tag {7.41}$$

证明: 见附录 C.13。

引理7.1的证明是基于以 $y_{h} = T(y_{h})$ 的形式列出一个关于 $y_{h}(t)$ 的方程，并证明 $T(\cdot)$ 是压缩映射。这就允许我们计算式(7.40)的上界，然后用此上界计算式(7.41)误差项的上界。对非线性特性 $\psi$ 的斜率限制用于证明 $T(\cdot)$ 为压缩映射。
