# Wiener 过程 (Brown 运动) 及随机积分

上面在Markov过程的定义中，曾提到时间可以是连续的，但我们主要讨论了随机序列，时间是离散的，下面两节主要讨论连续时间的随机过程.

设 $(\Omega, \mathcal{F}, P)$ 为基本概率空间， $(\mathbb{R}^{+}, \mathcal{B})$ 为正实数空间， $\mathbb{R}^{+} = [0, \infty)$ ， $\mathcal{B}$ 为 $\mathbb{R}^{+}$ 中的 Borel $\sigma$ -代数，用 $\mathcal{F} \times \mathcal{B}$ 表示包括形如 $F \times B$ 集合的最小 $\sigma$ -代数，其中 $F \in \mathcal{F}$ ， $B \in \mathcal{B}$ .

取值于 $(\mathbb{R}^l, \mathcal{B}^l)$ 并定义于 $(\Omega \times \mathbb{R}^+, \mathcal{F} \times \mathcal{B})$ 的函数 $\xi_t(\omega)$ ，称 $l$ 维连续时间随机过程，通常不显写 $\omega$ ，记作 $\xi_t$ 。

如果对任意 $B \in \mathcal{B}^l$ , $\{(\omega, t) : \xi_t(\omega) \in \mathcal{B}\} \in \mathcal{F} \times \mathcal{B}$ , 则称 $\xi_t(\omega)$ 为可测随机过程.

固定 $\omega$ 后， $\xi_t(\omega)$ 是定义在 $[0, \infty)$ 上的实函数，称为 $\xi_t$ 的轨线。如果除了可能的零概率事件外， $\xi_t$ 的所有轨线左（或右）连续则 $\xi_t$ 叫左（或右）连续。这时过程必可测。

1827 年英国生物学家 Brown 发现悬浮在液面上的花粉微粒做着高度不规则运动，这种现象后来被称为 Brown 运动。它的严述数学建模，归功于 Wiener，所以叫 Wiener 过程。

设 $l$ 维 $w_{t}$ 和非降 $\sigma$ -代数族 $\mathcal{F}_t$ 相适应 $(w_{t},\mathcal{F}_{t})$ ， $t \geqslant 0$ 。 $w_{0} = 0$ ， $Ew_{t} = 0$ ， $E\| w_{t}\|^2 < \infty, \forall t \geqslant 0$ ，且

$$E \left[ \left(w _ {t} - w _ {s}\right) \left(w _ {t} - w _ {s}\right) ^ {\mathrm{T}} \mid \mathcal {F} _ {s} \right] = (t - s) I, \quad \forall t \geqslant s. \tag {4.3.12}$$

还设 $(w_{t},\mathcal{F}_{t})$ 是鞅，它的a.s.轨线连续．那么称 $(w_{t},\mathcal{F}_{t})$ 为Wiener过程.

定理 4.3.2 Wiener 过程是独立增量过程，即对 $s_{1} < t_{1} \leqslant s_{2} < t_{2}, w_{t_{2}} - w_{s_{2}}$ 和 $w_{t_{1}} - w_{s_{1}}$ 独立，并且 $w_{t} - w_{s} (\forall t > s)$ 为正态，成立重对数律

$$\limsup _ {t \to \infty} \frac {\left\| w _ {t} \right\| ^ {2}}{2 l t \log \log t} = 1, \qquad \text { a.s. } \tag {4.3.13}$$

$w_{t}$ 的轨线在几乎所有 $t$ 都不可微分.

推论4.3.1 Wiener过程是Markov过程．这从独立增量性以及定理4.3.1中可看出：不妨设 $w_{t}$ 是一维的，注意到 $w_{t + s} - w_s$ 和 $w_{\lambda},0\leqslant \lambda \leqslant s$ 独立，所以

$$
\begin{array}{l} P \left(w _ {t + s} <   a \mid w _ {\lambda}, 0 \leqslant \lambda \leqslant s\right) = P \left(w _ {t + s} - w _ {s} <   a - w _ {s} \mid w _ {\lambda}, 0 \leqslant \lambda \leqslant s\right) \\ = P \left(w _ {t + s} - w _ {s} <   a - x\right) | _ {x = w _ {s}} \\ = P \left(w _ {t + s} - w _ {s} <   a - w _ {s} \mid w _ {s}\right) = P \left(w _ {t + s} <   a \mid w _ {s}\right). \\ \end{array}
$$

在上面，我们讨论过对直交增量过程的随机积分，被积函数为确定性函数。现在来看对 Wiener 过程的积分，被积函数为随机过程。

设 $\mathcal{F}_t$ 为非降 $\sigma$ -代数， $(\xi_t, \mathcal{F}_t)$ 为适应过程。如果
