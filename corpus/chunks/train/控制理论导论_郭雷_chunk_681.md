$$
\begin{array}{l} E \prod_ {k = m} ^ {n} \left(1 - \frac {1}{x _ {k}}\right) = E y _ {n} \leqslant E \sqrt {x _ {n} y _ {n}} \\ = E \sqrt {Z _ {n} \prod_ {i = m - 1} ^ {n - 1} \gamma_ {i}} \leqslant \sqrt {E Z _ {n}} \cdot \sqrt {E \prod_ {i = m - 1} ^ {n - 1} \gamma_ {i}} \\ \leqslant \sqrt {M _ {0}} \cdot \left\{E \prod_ {i = m - 1} ^ {n - 1} E \left[ \alpha_ {i + 1} ^ {4} \mid \mathcal {F} _ {i} \right] \right\} ^ {1 / 8} \\ \leqslant \sqrt {M _ {0}} M ^ {1 / 8} \gamma^ {1 / 8 (n - m + 1)}. \\ \end{array}
$$

这就证明了当 $N \leqslant 1$ 时结论 (iii) 成立.

下面考虑 $N \in (0, \infty)$ 的一般情形.

利用式 (9.3.10) 知可取常数 $C$ 充分大使

$$E [ \xi_ {k + 1} I (\xi_ {k + 1} \geqslant C) | \mathcal {F} _ {k} ] \leqslant 1,$$

且

$$\delta \stackrel {\text { def }} {=} (1 + \epsilon_ {0}) \frac {C}{1 + C} > 1.$$

于是利用式 (9.3.8) 得

$$x _ {k + 1} \leqslant \alpha_ {k + 1} x _ {k} + C + \xi_ {k + 1} I (\xi_ {k + 1} > C). \tag {9.3.13}$$

不失一般性，假设上式中等号对所有的 $k \geqslant 0$ 都成立。于是令 $\bar{x}_k = x_k(1 + C)^{-1}$ 得

$$\bar {x} _ {k + 1} = \alpha_ {k} \bar {x} _ {k} + \eta_ {k + 1}, \tag {9.3.14}$$

其中

$$\eta_ {k + 1} = (1 + C) ^ {- 1} [ C + \xi_ {k + 1} I (\xi_ {k + 1} > C) ].$$

显然， $E[\eta_{k + 1}|\mathcal{F}_k]\leqslant 1.$ 于是利用刚证明的结果知 $\left\{\frac{1}{\bar{x}_k}\right\} \in S^0.$

注意到 $\alpha_{k} \geqslant \epsilon_{0} > 0$ ，从式 (9.3.14) 得

$$\bar {x} _ {k + 1} \geqslant \alpha_ {k + 1} \left(\frac {C}{1 + C}\right) + \frac {C}{1 + C} \geqslant \frac {C}{1 + C} (1 + \epsilon_ {0}) > 1, \quad k \geqslant 1.$$

于是利用命题9.3.2（取 $\epsilon = \frac{1}{1 + C}$ ）知 $\left\{\frac{1}{x_k}\right\} \in S^0$ 。证毕。

推论9.3.2 设 $\{x_{k}\}$ 满足命题9.3.3的条件，而 $\{y_{n},\mathcal{F}_{n}\}$ 是非负适应序列，满足

$$y _ {k + 1} \leqslant \beta y _ {k} + \eta_ {k + 1}, \quad 0 \leqslant \beta < 1, \forall k,$$

其中

$$E [ \eta_ {k} ^ {2 q} | \mathcal {F} _ {k - 1} ] \leqslant M _ {1} < \infty , \quad q > \frac {\log \epsilon_ {0}}{\log \beta},$$

而 $\epsilon_0$ 由式 (9.3.9) 给出, 则有 $\left\{\frac{1}{x_k + y_k}\right\} \in S^0$ .

证明 取 $\epsilon$ 充分小使 $(1 + \epsilon)\beta^{q} \leqslant \epsilon_{0}$ 并定义

$$T _ {k} = \frac {1}{q} y _ {k} ^ {q} + \frac {1}{s}, \quad s = \left(1 - \frac {1}{q}\right) ^ {- 1}.$$

注意到对任何 $\epsilon > 0, q > 0$ 存在常数 $M > 0$ 使

$$(x + y) ^ {q} \leqslant (1 + \epsilon) x ^ {q} + M y ^ {q}, \quad x \geqslant 0, y \geqslant 0.$$

于是有
