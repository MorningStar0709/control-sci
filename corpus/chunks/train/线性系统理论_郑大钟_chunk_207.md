$$\boldsymbol {u} ^ {*} (t) = - R ^ {- 1} B ^ {T} P (t, \mathbf {0}, \infty) \boldsymbol {x} ^ {*} (t) = - R ^ {- 1} B ^ {T} P \boldsymbol {x} ^ {*} (t) \tag {5.231}$$

而由闭环状态方程

$$\dot {x} ^ {*} = (A - B R ^ {- 1} B ^ {T} P) x ^ {*}, \quad x ^ {*} (0) = x _ {0} \tag {5.232}$$

则可定出

$$x ^ {*} (t) = e ^ {2 t} x _ {0}, \quad \overline {{A}} \triangleq (A - B R ^ {- 1} B ^ {T} P) \tag {5.233}$$

此外，由于 $x_0 \neq 0$ ，依运动的连续性可知，必存在 $t_f (0 < t_f < \infty)$ ，使对一切 $z \in [0, t_f]$ $x^*(t) \neq 0$ 。于是，由此并利用 (5.231) 和 (5.233)，可由 (5.230) 进一步导出：

$$
\begin{array}{l} \boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} = \int_ {0} ^ {\infty} \boldsymbol {x} ^ {* T} [ Q + P B R ^ {- 1} B ^ {T} P ] \boldsymbol {x} ^ {*} d t \\ \geqslant \int_ {0} ^ {t _ {f}} x ^ {* T} [ Q + P B R ^ {- 1} B ^ {T} P ] x ^ {*} d t \\ = \int_ {0} ^ {t _ {f}} (e ^ {\lambda t} x _ {0}) ^ {T} [ Q + P B R ^ {- 1} B ^ {T} P ] (e ^ {\lambda t} x _ {0}) d t \tag {5.234} \\ \end{array}
$$

上式中， $e^{\lambda t}$ 为非奇异，而由 R > 0（正定）可知 $PBR^{-1}B^{T}P \geqslant 0$ （正半定）。这表明，当 Q > 0 时，必有 $[Q + PBR^{-1}B^{T}P] > 0$ ，也即对一切 $t \in [0, t_{f}]$

$$\left(e ^ {\lambda t} \boldsymbol {x} _ {0}\right) ^ {T} [ Q + P B R ^ {- 1} B ^ {T} P ] \left(e ^ {\lambda t} \boldsymbol {x} _ {0}\right) > 0, \quad \boldsymbol {x} _ {0} \neq 0 \tag {5.235}$$

从而，意味着

$$\boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} > 0 \tag {5.236}$$

也就是 $P$ 为正定。而当 $Q \geqslant 0$ 和 $(A, H)$ 为能观测 $(Q = H^T H)$ 时，同样可证明 $P$ 为正定。可采用反证法来证明这一点，反设 $P$ 不是为正定而是为正半定，则必存在某个 $\bar{x}_0 \neq 0$ 使成立

$$0 = \bar {x} _ {0} ^ {T} P \bar {x} _ {0} = \int_ {0} ^ {\infty} [ x ^ {* T} Q x ^ {*} + u ^ {* T} R u ^ {*} ] d t \tag {5.237}$$

由于 $R > 0$ 和 $Q \geqslant 0$ , 故欲上式成立, 一般地应有

$$\int_ {0} ^ {\infty} \boldsymbol {u} ^ {* T} R \boldsymbol {u} ^ {*} d t = 0 \tag {5.238}$$

和

$$\int_ {0} ^ {\infty} \boldsymbol {x} ^ {* T} Q \boldsymbol {x} ^ {*} d t = 0 \tag {5.239}$$

再因 $R > 0$ ，则由（5.238）可导出 $\pmb{u}^{*}(t)\equiv 0$ ；再由 $Q = H^{T}H$ ，故可从(5.239)得到

$$0 = \int_ {0} ^ {\infty} \boldsymbol {x} ^ {* T} H ^ {T} H \boldsymbol {x} ^ {*} d t = \int_ {0} ^ {\infty} (H \boldsymbol {x} ^ {*}) ^ {T} (H \boldsymbol {x} ^ {*}) d t \tag {5.240}$$

也即有

$$H x ^ {*} (t) = 0, \quad \forall t \geqslant 0 \tag {5.241}$$

而这和已知 $(A, H)$ 为完全能观测是相矛盾的，所以反设不成立，也就是此种情况下也必有 $P$ 为正定。证明完成。

在上述所作的讨论的基础上，现在就可直接来给出定常的无限时间 LQ 问题的最优解的有关结论。

结论1 对于定常的无限时间LQ调节问题(5.210)和(5.211)， $u^{*}(\cdot)$ 为其最优控制的充分必要条件是其具有形式：

$$\boldsymbol {u} ^ {*} (t) = - K ^ {*} \boldsymbol {x} ^ {*} (t), \quad K ^ {*} = R ^ {- 1} B ^ {T} P \tag {5.242}$$

最优轨线 $x^{*}(t)$ 为下述状态方程的解：
