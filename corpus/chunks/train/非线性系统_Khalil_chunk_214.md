对于 $G(j\omega)$ 的奈奎斯特曲线上的一点 $q$ ，两个复数 $(1 / \beta) + G(j\omega)$ 和 $(1 / \alpha) + G(j\omega)$ 可以分别由连接 $q$ 到 $-(1 / \beta) + j0$ 和 $-(1 / \alpha) + j0$ 的直线表示，如图7.4所示。当两个复数幅角差值小于 $\pi / 2$ 时，也就是说，在图7.4中， $(\theta_1 - \theta_2)$ 小于 $\pi / 2$ ，这两个复数比值的实部是正的。如果定义 $D(\alpha, \beta)$ 是复平面中的闭圆盘，其直径是连接 $-(1 / \alpha) + j0$ 和 $-(1 / \beta) + j0$ 两点的线段，则容易看出，只要 $q$ 在圆盘 $D(\alpha, \beta)$ 之外， $(\theta_1 - \theta_2)$ 就小于 $\pi / 2$ 。由于要求式(7.11)对所有 $\omega$ 成立，因此在 $G(j\omega)$ 的奈奎斯特曲线上的所有点必须严格在圆盘 $D(\alpha, \beta)$ 之外。另一方面，如果 $G(s) / [1 + \alpha G(s)]$ 是赫尔维茨的，则 $Z(s)$ 也是赫尔维茨的。奈奎斯特判据说：当且仅当 $G(j\omega)$ 的奈奎斯特曲线不通过点 $-(1 / \alpha) + j0$ ，且逆时针方向环绕该点 $m$ 次，则 $G(s) / [1 + \alpha G(s)]$ 是赫尔维茨的，其中 $m$ 是 $G(s)$ 在右半开复平面中极点的个数①。因而，如果 $G(j\omega)$ 的奈奎斯特曲线不进入圆盘 $D(\alpha, \beta)$ ，且沿逆时针方向环绕其 $m$ 次，则满足定理7.1中的条件。下面考虑 $\beta > 0$ 且 $\alpha = 0$ 的情况。定理7.1要求 $1 + \beta G(s)$ 是严格正实的，这就要求 $G(s)$ 是赫尔维茨的，且有

$$\operatorname{Re} [ 1 + \beta G (j \omega) ] > 0, \forall \omega \in [ - \infty , \infty ]$$

后面的条件可以重写为 $\operatorname{Re}[G(j\omega)] > -\frac{1}{\beta}, \forall \omega \in [-\infty, \infty]$

这个条件相当于图解法中要求 $G(j\omega)$ 的奈奎斯特曲线全部位于直线 $Re[s]=-1/\beta$ 的右侧。最后考虑 $\alpha<0<\beta$ 的情况。在这种情况下，条件(7.10)相当于

$$\mathrm{Re} \left[ \frac {\frac {1}{\beta} + G (j \omega)}{\frac {1}{\alpha} + G (j \omega)} \right] < 0, \forall \omega \in [ - \infty , \infty ] \tag {7.12}$$

这里的不等式符号与前面相反,因为当从式(7.10)变换到式(7.12)时,两侧均乘以 $\alpha/\beta$ , 它是个负数。重复前面的论证,容易看出如果式(7.12)成立,则 $G(j\omega)$ 的奈奎斯特曲线一定位于圆盘 $D(\alpha,\beta)$ 的内部,因而奈奎斯特曲线不可能环绕 $-(1/\alpha)+j0$ 点。所以根据奈奎斯特判据可以得出,要使 $G(s)/[1+\alpha G(s)]$ 是赫尔维茨的,则 $G(s)$ 必须是赫尔维茨的。以上三种情况的稳定性判据可以总结为下面的定理,即所谓圆判据。

![](image/7babfd048f9a5fe569da45a0af11e071b787ad5e149c1e5729abfa38cd8d849e.jpg)

<details>
<summary>text_image</summary>

D(\u03b1,\u03b2)
-1/\u03b1
\theta_2
-1/\u03b2
\theta_1
q
</details>

图 7.4 圆判据的图形表示

定理7.2 考虑形如系统(7.1)\~(7.3)的标量系统,这里 $\{A,B,C,D\}$ 是 $G(s)$ 的一个最小实现,且 $\psi\in[\alpha,\beta]$ 。如果以下条件之一满足,则系统绝对稳定:

1. 如果 $0 < \alpha < \beta, G(j\omega)$ 的奈奎斯特曲线不进入圆盘 $D(\alpha, \beta)$ 内，且沿逆时针方向环绕其 m 次，其中 m 是 $G(s)$ 具有正实部的极点数。  
2. 如果 $0 = \alpha < \beta, G(s)$ 是赫尔维茨的，且 $G(s)$ 的奈奎斯特曲线位于直线 $\operatorname{Re}[s] = -1/\beta$ 的右侧。  
3. 如果 $\alpha<0<\beta,G(s)$ 是赫尔维茨的，且 $G(j\omega)$ 的奈奎斯特曲线位于圆盘 $D(\alpha,\beta)$ 的内部。

如果仅仅在一个区间 $[a, b]$ 内满足扇形区域条件，则上述条件保证了系统在有限区域内绝对稳定。
