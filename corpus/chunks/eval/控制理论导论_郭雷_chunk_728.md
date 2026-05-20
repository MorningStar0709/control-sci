# 10.1 无穷维线性系统的稳定性

稳定性是控制系统理论中研究的基本问题之一。控制的一个重要目的就是使原来不稳定的系统成为稳定的系统。本节我们考虑 Banach 空间 X 中线性系统

$$\frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t), \quad x (0) = x _ {0} \tag {10.1.1}$$

的各种稳定性概念，这里 A 是 X 上某个 $C_{0}$ 半群 $T(t)$ 的生成算子。从第 5 章我们知道式 (10.1.1) 的 (温和) 解是

$$\boldsymbol {x} (t) = T (t) \boldsymbol {x} _ {0}, \quad t \geqslant 0. \tag {10.1.2}$$

因此，在谈及线性系统(10.1.1)的稳定性时，等同于说半群 $T(t)$ 的稳定性.

定义10.1.1 设 $T(t)$ 是Banach空间 $X$ 上一 $C_0$ 半群. 那么

(a) $T(t)$ 称为一致指数渐近稳定的，是指存在两个正常数 $M$ 和 $\omega$ 使得

$$\| T (t) \| \leqslant M \mathrm{e} ^ {- \omega t}, \quad \forall t \geqslant 0; \tag {10.1.3}$$

(b) $T(t)$ 称为指数渐近稳定的，是指对于每一 $x \in X$ ，存在两个正常数 $M_x$ 和 $\omega_x$ 使得 $\| T(t)x \| \leqslant M_x e^{-\omega_x t}$ ;

(c) $T(t)$ 称为一致渐近稳定的，是指当 $t \to \infty$ 时， $\| T(t) \| \to 0$ ;

(d) $T(t)$ 称为强 $L^p$ -稳定的 $(p \geqslant 1)$ , 是指对于任意 $x \in X$ , $\| T(\cdot)x \| \in L^p(0, \infty)$ ;

(e) $T(t)$ 称为强渐近稳定的，是指对于任意 $x \in X$ ，当 $t \to \infty$ 时， $\| T(t)x \| \to 0$ ;

(f) $T(t)$ 称为弱渐近稳定的，是指对于任意 $x \in X, x^{*} \in X^{*}$ ，当 $t \to \infty$ 时， $\langle T(t)x, x^{*} \rangle \to 0$ ;

(g) $T(t)$ 称为一致稳定的或一致有界的，是指存在正常数 $M$ 使得 $\| T(t)\| \leqslant M, \forall t \geqslant 0$ ;

(h) $T(t)$ 称为弱 $L^{p}$ -稳定的 $(p \geqslant 1)$ , 是指对于任意 $x \in X$ , $x^{*} \in X^{*}$ , $\langle T(\cdot)x, x^{*} \rangle \in L^{p}(0, \infty)$ .

在阐明上述各种稳定性之间的关系之前，我们先证明一个有关 $C_0$ 半群增长阶的引理.

引理10.1.1 设 $T(t)$ 是Banach空间 $X$ 上一闭稠定线性算子 $A$ 生成的 $C_0$ 半群，则存在一实数 $\omega_0, -\infty \leqslant \omega_0 < \infty$ ，使得

$$\lim _ {t \rightarrow \infty} \frac {\log \| T (t) \|}{t} = \inf _ {t > 0} \frac {\log \| T (t) \|}{t} = \omega_ {0}, \tag {10.1.4}$$

并且对于任意实数 $\omega >\omega_0$ ，存在实数 $M = M_{\omega}\geqslant 1$ ，使得

$$\| T (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0 \tag {10.1.5}$$

证明 设 $p(t) = \log \| T(t)\|$ . 从 $\| T(t + s)\| \leqslant \| T(t)\| \| T(s)\|$ , 我们有 $p(0) = 0$ , 以及

$$p (t + s) \leqslant p (t) + p (s), \quad \forall t, s \geqslant 0.$$

令

$$\omega_ {0} \stackrel {\text { def }} {=} \inf _ {t > 0} \frac {\log \| T (t) \|}{t}.$$

首先我们考虑 $\omega_0$ 为有穷的情形．给定任意 $\varepsilon > 0$ ，取正数 $a$ 使得 $p(a) \leqslant (\omega_0 + \varepsilon)a$ .

于是当 $t > a$ 时，我们有

$$
\begin{array}{l} \omega_ {0} \leqslant \frac {p (t)}{t} \leqslant \frac {p (n a)}{t} + \frac {p (t - n a)}{t} \\ \leqslant \frac {n a}{t} \frac {p (a)}{a} + \frac {p (t - n a)}{t} \\ \leqslant \frac {n a}{t} (\omega_ {0} + \varepsilon) + \frac {p (t - n a)}{t}, \\ \end{array}
$$
