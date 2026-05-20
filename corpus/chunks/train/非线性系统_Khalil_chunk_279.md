其中 $c_{1}, c_{2}$ 和 $\mu_{i}$ 是与 $\alpha$ 无关的正常数。因而，当 $c_{3}=1, c_{4}=2c_{2}, c_{5}=\sqrt{\sum_{i=1}^{m}\mu_{i}^{2}}$ 时， $V(z, \alpha)=z^{\mathrm{T}}P(\alpha)z$ 在 2 范数下满足式 (9.42) 至式 (9.44)。

证明: $A(\alpha)$ 的一致赫尔维茨性质意味着指数矩阵 $\exp[tA(\alpha)]$ 满足

$$\| \exp [ t A (\alpha) ] \| \leqslant k (A) e ^ {- \beta t}, \forall t \geqslant 0, \forall \alpha \in \Gamma$$

其中， $\beta > 0$ 与 $\alpha$ 无关，但 $K(A) > 0$ 与 $\alpha$ 有关。因为按指数规律衰减的边界对于 $\alpha$ 一致成立，所以需要用到 $\|A(\alpha)\|$ 有界的性质。满足 $\operatorname{Re}[\lambda(A(\alpha))] \leqslant -\sigma$ 和 $\|A(\alpha)\| \leqslant c$ 的矩阵集合是一个紧集,记为 S。设 A 和 B 是 S 的任意两个元素,考虑 $^{①}$

$$\exp [ t (A + B) ] = \exp [ t A ] + \int_ {0} ^ {t} \exp [ (t - \tau) A ] B \exp [ \tau (A + B) ] d \tau$$

运用关于 $\exp [tA]$ 的指数衰减边界，可得到

$$\| \exp [ t (A + B) ] \| \leqslant k (A) e ^ {- \beta t} + \int_ {0} ^ {t} k (A) e ^ {- \beta (t - \tau)} \| B \| \| \exp [ \tau (A + B) ] \| d \tau$$

用 $e^{\beta t}$ 遍乘各项可得

$$e ^ {\beta t} \| \exp [ t (A + B) ] \| \leqslant k (A) + k (A) \| B \| \int_ {0} ^ {t} e ^ {\beta \tau} \| \exp [ \tau (A + B) ] \| d \tau$$

应用 Gronwall-Bellman 不等式, 得

$$\| \exp [ t (A + B) ] \| \leqslant k (A) e ^ {- (\beta - k (A) \| B \|) t}, \forall t \geqslant 0$$

因此,存在一个正常数 $\gamma < \beta$ 和 A 的一个邻域 $\mathcal{N}(A)$ ，使得如果 $C \in \mathcal{N}(A)$ ，则

$$\| \exp [ t C ] \| \leqslant k (A) e ^ {- \gamma t}, \forall t \geqslant 0$$

因 S 是紧集,所以被这些邻域中的有限个邻域覆盖,从而可找到一个与 $\alpha$ 无关的正常数 k,使得

$$\| \exp [ t A (\alpha) ] \| \leqslant k e ^ {- \gamma t}, \forall t \geqslant 0, \forall \alpha \in \Gamma$$

现在考虑李雅普诺夫方程(9.48)。根据定理4.6,对于每个 $\alpha \in \Gamma$ ，方程(9.48)存在唯一的正定解。此外，定理(4.16)的证明还说明

$$P (\alpha) = \int_ {0} ^ {\infty} \left[ e ^ {t A (\alpha)} \right] ^ {\mathrm{T}} \left[ e ^ {t A (\alpha)} \right] d t$$

由于 $A(\alpha)$ 是连续可微的，所以 $P(\alpha)$ 也是连续可微的，故有

$$z ^ {\mathrm{T}} P (\alpha) z \leqslant \int_ {0} ^ {\infty} k ^ {2} e ^ {- 2 \gamma t} \| z \| _ {2} ^ {2} d t = \frac {k ^ {2}}{2 \gamma} \| z \| _ {2} ^ {2} \Rightarrow c _ {2} = \frac {k ^ {2}}{2 \gamma}$$

设 $y(t) = e^{tA(\alpha)}z$ ，则 $\dot{y} = A(\alpha)y,$

$$- y ^ {T} (t) \dot {y} (t) = - y ^ {T} (t) A (\alpha) y (t) \leqslant \| A (\alpha) \| _ {2} y ^ {T} (t) y (t) \leqslant c y ^ {T} (t) y (t)$$

且 $z^{\mathrm{T}}P(\alpha)z = \int_{0}^{\infty}y^{\mathrm{T}}(t)y(t)dt\geqslant \int_{0}^{\infty}\frac{-1}{c} y^{\mathrm{T}}(t)\dot{y} (t)dt$
