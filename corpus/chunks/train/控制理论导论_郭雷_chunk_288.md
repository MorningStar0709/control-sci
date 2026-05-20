$$(E | \pmb {\xi} + \pmb {\eta} | ^ {r}) ^ {\frac {1}{r}} \leqslant (E | \pmb {\xi} | ^ {r}) ^ {\frac {1}{r}} + (E | \pmb {\eta} | ^ {r}) ^ {\frac {1}{r}}. \tag {4.1.17}$$

证明 $r = 1$ 是不足道的情形，不妨设 $r > 1$ 。对不等式

$$E | \xi + \eta | ^ {r} \leqslant E (| \xi | | \xi + \eta | ^ {r - 1}) + E (| \eta | | \xi + \eta | ^ {r - 1})$$

的右端的两项分别用 Hölder 不等式，取 $s$ 满足 $\frac{1}{r} + \frac{1}{s} = 1$ ，就有

$$E | \boldsymbol {\xi} + \eta | ^ {r} \leqslant [ (E | \boldsymbol {\xi} | ^ {r}) ^ {\frac {1}{r}} + (E | \eta | ^ {r}) ^ {\frac {1}{r}} ] (E | \boldsymbol {\xi} + \eta | ^ {(r - 1) s}) ^ {\frac {1}{s}}.$$

注意到 $(r - 1)s = r$ ，对上式除以 $(E|\xi +\eta |^r)^{\frac{1}{s}}$ 后，便得式(4.1.17).

Jensen 不等式 设 $g(\cdot)$ 为凸 Borel 函数, $E|\xi| < \infty$ , 则

$$g (E \pmb {\xi}) \leqslant E g (\pmb {\xi}). \tag {4.1.18}$$

证明 当 $g(\cdot)$ 是可微分的凸函数时，它的导数必非降，当它不一定可微时，对任意固定的 $x_0$

$$\lambda_ {x _ {0}} (x) \stackrel {\text { def }} {=} \frac {g (x) - g (x _ {0})}{x - x _ {0}}$$

作为 $x$ 的函数也是不降的．记

$$\mu (x _ {0}) = \lim _ {x \mid x _ {0}} \lambda_ {x _ {0}} (x),$$

那么

$$\mu (x _ {0}) \leqslant \lambda_ {x _ {0}} (x), \quad \forall x > x _ {0},\mu (x _ {0}) \geqslant \lambda_ {x _ {0}} (x), \quad \forall x < x _ {0}.$$

由此知

$$\mu (x _ {0}) (x - x _ {0}) \leqslant g (x) - g (x _ {0}), \quad \forall x \in \mathbb {R} ^ {1}.$$

今取 $x_0 = E\xi, x = \xi$ . 取期望后便得

$$\mu (E \pmb {\xi}) E (\pmb {\xi} - E \pmb {\xi}) \leqslant E g (\pmb {\xi}) - g (E \pmb {\xi}),$$

由此便得式 (4.1.18).

Lyapunov 不等式 设 $0 < s < t$ ，则

$$(E | \pmb {\xi} | ^ {s}) ^ {\frac {1}{s}} \leqslant (E | \pmb {\xi} | ^ {t}) ^ {\frac {1}{t}},$$

即 $(E|\xi|^t)^{\frac{1}{t}}$ 对 $t$ 是非降函数.

证明 记 $r = \frac{t}{s}, \eta = |\xi|^s$ ，对 $g(x) = |x|^r$ 用Jenscn不等式得

$$\left| E \eta \right| ^ {r} \leqslant E \left| \eta \right| ^ {r},$$

即

$$(E | \pmb {\xi} | ^ {s}) ^ {r} \leqslant E | \pmb {\xi} | ^ {s r} \text {或} (E | \pmb {\xi} | ^ {s}) ^ {\frac {t}{s}} \leqslant E | \pmb {\xi} | ^ {t}.$$

Chebyshev 不等式 对任一 $\epsilon > 0$ 都有

$$P (| \xi | \geqslant \epsilon) \leqslant \frac {E | \xi |}{\epsilon}.$$

证明

$$E | \boldsymbol {\xi} | \geqslant E (| \boldsymbol {\xi} | I _ {[ | \boldsymbol {\xi} | \geqslant \epsilon ]}) \geqslant \epsilon E (I _ {[ | \boldsymbol {\xi} | \geqslant \epsilon ]}) = \epsilon P (| \boldsymbol {\xi} | \geqslant \epsilon).$$
