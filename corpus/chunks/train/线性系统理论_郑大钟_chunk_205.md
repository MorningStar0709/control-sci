$$
\begin{array}{l} J (\tilde {u} (\cdot)) = \int_ {0} ^ {\infty} \left(\tilde {x} ^ {T} Q \tilde {x} + \tilde {u} ^ {T} R \tilde {u}\right) d t \\ = \int_ {0} ^ {t _ {1}} \left(x _ {1} ^ {T} Q x _ {1} + u _ {1} ^ {T} R u _ {1}\right) d t \\ = M (0, x _ {0}) <   \infty \tag {5.216} \\ \end{array}
$$

进而，表 $u^{*}(\cdot)$ 和 $x^{*}(\cdot)$ 为问题的最优控制和最优轨线， $J^{*}$ 为相应的最优性能值，那么根据最优性又可导出：

$$
\begin{array}{l} J ^ {*} = x _ {0} ^ {T} P (0, 0, t _ {i}) x _ {0} \\ = \int_ {0} ^ {t _ {f}} \left(x ^ {* T} Q x ^ {*} + u ^ {* T} R u ^ {*}\right) d t \\ \leqslant \int_ {0} ^ {t _ {f}} \left(\tilde {x} ^ {T} Q \tilde {x} + \tilde {u} ^ {T} R \tilde {u}\right) d t \\ \end{array}

\begin{array}{l} \leqslant \int_ {0} ^ {\infty} \left(\tilde {\boldsymbol {x}} ^ {T} Q \tilde {\boldsymbol {x}} + \tilde {\boldsymbol {u}} ^ {T} R \tilde {\boldsymbol {u}}\right) d t \\ = M \left(0, x _ {0}\right) <   \infty \tag {5.217} \\ \end{array}
$$

这表明， $P(0,0,t_{f})$ 对一切 $t_{f} \geqslant 0$ 有上界。证明完成。

(2) 对任意 $t \geqslant 0$ ，极限 $\lim_{t_j \to \infty} P(t, 0, t_j) = P(t, 0, \infty)$ 存在。

证 由于(5.212)为定常矩阵微分方程,故必成立 $P(t,0,t_f) = P(0,0,t_f - t)$ , 从而可知上述命题等价于证明 $P(0,0,\infty)$ 的存在性。为此,考虑并表 $P(0,0,t_f)$ 为:

$$
P (0, \mathbf {0}, t _ {f}) = \left[ \begin{array}{c c} p _ {1 1} (0, \mathbf {0}, t _ {f}) & \dots \dots p _ {1 n} (0, \mathbf {0}, t _ {f}) \\ \vdots & \vdots \\ p _ {n 1} (0, \mathbf {0}, t _ {f}) & \dots \dots p _ {n n} (0, \mathbf {0}, t _ {f}) \end{array} \right] \tag {5.218}
$$

且由其为对称矩阵知，必成立

$$p _ {i j} (0, 0, t _ {j}) = p _ {i i} (0, 0, t _ {j}), \quad i \neq j \tag {5.219}$$

现先来证明对角线元 $p_{ii}(0, 0, t_f)$ 当 $t_f \to \infty$ 时的存在性。为此，令 $x_0 \neq 0$ 为任意初态，且取 $t_2 > t_f$ ，并表 $J_2^*$ 和 $J^*$ 为末时刻分别是 $t_2$ 和 $t_f$ 的 LQ 问题的最优性能值，于是就有：

$$
\begin{array}{l} \boldsymbol {x} _ {0} ^ {T} P (0, 0, t _ {f}) \boldsymbol {x} _ {0} = J ^ {*} = \int_ {0} ^ {t _ {f}} \left(\boldsymbol {x} ^ {* T} Q \boldsymbol {x} ^ {*} + \boldsymbol {u} ^ {* T} R \boldsymbol {u} ^ {*}\right) d t \\ \leqslant \int_ {0} ^ {t _ {f}} \left(\boldsymbol {x} _ {2} ^ {* T} Q \boldsymbol {x} _ {2} ^ {*} + \boldsymbol {u} _ {2} ^ {* T} R \boldsymbol {u} _ {2} ^ {*}\right) d t \\ \leqslant \int_ {0} ^ {t _ {2}} \left(\boldsymbol {x} _ {2} ^ {* T} Q \boldsymbol {x} _ {2} ^ {*} + \boldsymbol {u} _ {2} ^ {* T} R \boldsymbol {u} _ {2} ^ {*}\right) d t \\ = J _ {2} ^ {*} = x _ {0} ^ {T} P (0, 0, t _ {2}) x _ {0} \tag {5.220} \\ \end{array}
$$

进而，取

$$\boldsymbol {x} _ {0} = \boldsymbol {e} _ {i} = [ 0 \dots 0, 1, 0 \dots 0 ] ^ {T}, \quad i = 1, 2, \dots , n \tag {5.221}$$

那么，将此代入（5.220），并考虑到
