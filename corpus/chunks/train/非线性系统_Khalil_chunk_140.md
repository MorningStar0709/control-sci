$$\dot {V} (t, x) \leqslant - W _ {3} (x), \quad \forall \mu \leqslant \| x \| \leqslant r, \forall t \geqslant t _ {0} \tag {4.37}$$

如果 r 与 $\mu$ 相比足够大, 可选择 c 和 $\varepsilon$ , 使 $\Lambda$ 为非空集, 且包含于 $\{\mu \leqslant \|x\| \leqslant r\}$ 内。特别地, 令 $\alpha_{1}$ 和 $\alpha_{2}$ 为 K 类函数, 满足①

$$\alpha_ {1} (\| x \|) \leqslant V (x) \leqslant \alpha_ {2} (\| x \|) \tag {4.38}$$

根据式 $(4.38)$ 左边的不等式,有

$$V (x) \leqslant c \Rightarrow \alpha_ {1} (\| x \|) \leqslant c \Leftrightarrow \| x \| \leqslant \alpha_ {1} ^ {- 1} (c)$$

因此，取 $c = \alpha_{1}(r)$ 以保证 $\Omega_c\subset B_r$ 。另一方面，根据式(4.38)右边的不等式，可得

$$\| x \| \leqslant \mu \Rightarrow V (x) \leqslant \alpha_ {2} (\mu)$$

相应地，取 $\varepsilon = \alpha_{2}(\mu)$ 以保证 $B_{\mu}\subset \Omega_{\varepsilon}$ 。为了得到 $\varepsilon < c$ ，必须有 $\mu = \alpha_2^{-1}(\alpha_1(r))$ 。图4.9为 $\Omega_c$ $\Omega_{\varepsilon},B_r$ 和 $B_{\mu}$ 的示意图。

前面论证了所有始于 $\Omega_{c}$ 内的轨线都在有限时间 T 内进入 $\Omega_{\varepsilon}$ ①。为了计算 $x(t)$ 上的最终边界，利用式(4.38)左边的不等式可写出

$$V (x) \leqslant \varepsilon \Rightarrow \alpha_ {1} (\| x \|) \leqslant \varepsilon \Leftrightarrow \| x \| \leqslant \alpha_ {1} ^ {- 1} (\varepsilon)$$

由前面的 $\varepsilon = \alpha_{2}(\mu)$ 可看出

$$x \in \Omega_ {\varepsilon} \Rightarrow \| x \| \leqslant \alpha_ {1} ^ {- 1} (\alpha_ {2} (\mu))$$

因此，最终边界可取为 $b = \alpha_{1}^{-1}(\alpha_{2}(\mu))$ 。

对连续可微函数 $V(x)$ 提出的概念可用于连续可微函数 $V(t,x)$ ，只要 $V(t,x)$ 满足不等式(4.38)，由此不等式可导出下面的用以说明一致有界性和毕竟有界性的类李雅普诺夫定理。

![](image/9676a6b7f32b6a2ed91ca6a709a0f5bdb10b2dfa63f7667c9fc0ad36b6867bb8.jpg)

<details>
<summary>text_image</summary>

Bμ
Ωε
Ωc
Br
</details>

图4.9 集合 $\Omega_{\varepsilon}$ 和 $\Omega_c$ (实线) 以及 $B_{\mu}$ 和 $B_{r}$ (虚线)

定理4.18 设 $D \subset R^n$ 是包含原点的定义域, 且 $\forall t \geqslant 0$ 和 $\forall x \in D, V: [0, \infty) \times D \to R$ 是连续可微函数, 满足

$$\alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \tag {4.39}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - W _ {3} (x), \forall \| x \| \geqslant \mu > 0 \tag {4.40}$$

式中 $\alpha_{1}$ 和 $\alpha_{2}$ 是 $\kappa$ 类函数， $W_{3}(x)$ 是连续正定函数。取 $r > 0$ 使 $B_{r} \subset D$ ，并假设

$$\mu < \alpha_ {2} ^ {- 1} (\alpha_ {1} (r)) \tag {4.41}$$

那么，存在一个KL类函数 $\beta$ ，且对于每个满足 $\|x(t_{0})\|\leqslant\alpha_{2}^{-1}(\alpha_{1}(r))$ 的初始状态 $x(t_{0})$ ，存在 $T\geqslant0$ （与 $x(t_{0})$ 和 $\mu$ 有关），使方程(4.32)的解满足
