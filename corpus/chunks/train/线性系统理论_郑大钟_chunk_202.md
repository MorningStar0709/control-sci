这样, 利用 (5.193) 和 (5.194) 相等, 并考虑到一般地有 $x^{*}(t) \neq 0$ , 就导出了 $P(t)$ 应满足的方程:

$$- \dot {P} (t) = P (t) A + A ^ {T} P (t) + Q - P (t) B R ^ {- 1} B ^ {T} P (t) \tag {5.195}$$

此外，利用(5.191)和(5.192)，还可导出 $P(t)$ 应满足的端点条件：

$$P \left(\iota_ {f}\right) = S \tag {5.196}$$

于是，把(5.192)代入(5.189)，就导出了 $u^{*}(\cdot)$ 的形式为：

$$\mathbf {u} ^ {*} (t) = - R ^ {- 1} B ^ {T} P (t) \mathbf {x} ^ {*} (t) \tag {5.197}$$

其中， $P(t)$ 为 (5.195) 和 (5.196) 的解阵。从而，必要性得证。

充分性：已知 $\boldsymbol{u}^{*}(t) = -R^{-1}B^{T}P(t)\boldsymbol{x}^{*}(t)$ ，欲证 $\boldsymbol{u}^{*}(\cdot)$ 为最优控制。

引入如下的等式:

$$
\begin{array}{l} \frac {1}{2} x ^ {T} \left(t _ {j}\right) P \left(t _ {j}\right) x \left(t _ {j}\right) - \frac {1}{2} x ^ {T} (0) P (0) x (0) = \frac {1}{2} \int_ {0} ^ {t _ {j}} \frac {d}{d t} [ x ^ {T} P (t) x ] d t \\ - \frac {1}{2} \int_ {0} ^ {t _ {f}} [ \dot {\boldsymbol {x}} ^ {T} P (t) \boldsymbol {x} + \boldsymbol {x} ^ {T} \dot {P} (t) \boldsymbol {x} + \boldsymbol {x} ^ {T} P (t) \dot {\boldsymbol {x}} ] d t \tag {5.198} \\ \end{array}
$$

进而,利用(5.174)和(5.179),可把上式进一步改写为:

$$
\begin{array}{l} \frac {1}{2} x ^ {T} \left(t _ {f}\right) P \left(t _ {f}\right) x \left(t _ {f}\right) - \frac {1}{2} x ^ {T} (0) P (0) x (0) \\ - \frac {1}{2} \int_ {0} ^ {t _ {f}} \left\{\boldsymbol {x} ^ {T} \left[ A ^ {T} P (t) + \dot {P} (t) + P (t) A \right] \boldsymbol {x} + \boldsymbol {u} ^ {T} B ^ {T} P (t) \boldsymbol {x} + \boldsymbol {x} ^ {T} P (t) B \boldsymbol {u} \right\} d t \\ = \frac {1}{2} \int_ {0} ^ {t _ {f}} \left\{- x ^ {T} Q x + x ^ {T} P (t) B R ^ {- 1} B ^ {T} P (t) x + u ^ {T} B ^ {T} P (t) x + x ^ {T} P (t) B u \right\} d t \tag {5.199} \\ \end{array}
$$

再对上式作“配方”，又有

$$
\begin{array}{l} \frac {1}{2} x ^ {T} \left(t _ {f}\right) P \left(t _ {f}\right) x \left(t _ {f}\right) - \frac {1}{2} x ^ {T} (0) P (0) x (0) \\ = \frac {1}{2} \int_ {0} ^ {t _ {f}} \left\{- x ^ {T} Q x - u ^ {T} R u + [ u + R ^ {- 1} B ^ {T} P (t) x ] ^ {T} R [ u + R ^ {- 1} B ^ {T} P (t) x ] \right\} d t \tag {5.200} \\ \end{array}
$$

于是，由此并注意到 $P(t_{f}) = S$ ，可以导出

$$
\begin{array}{l} J (u (\cdot)) = \frac {1}{2} x ^ {T} \left(t _ {j}\right) S x \left(t _ {j}\right) + \frac {1}{2} \int_ {0} ^ {t _ {j}} \left[ x ^ {T} Q x + u ^ {T} R u \right] d t \\ - \frac {1}{2} x ^ {T} (0) P (0) x (0) + \frac {1}{2} \int_ {0} ^ {t _ {f}} [ u + R ^ {- 1} B ^ {T} P (t) x ] ^ {T} R [ u \\ + R ^ {- 1} B ^ {T} P (t) x ] d t \tag {5.201} \\ \end{array}
$$

这表明，当取 $u^{*}(t) = -R^{-1}B^{T}P(t)x^{*}(t)$ 时，性能指标 $J(u(\cdot))$ 将取最小值

$$J ^ {*} = J \left(u ^ {*} (\cdot)\right) = \frac {1}{2} x ^ {T} (0) P (0) x (0) \tag {5.202}$$
