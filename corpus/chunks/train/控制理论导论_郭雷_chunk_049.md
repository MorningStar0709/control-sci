$$\boldsymbol {\Psi} ^ {\mathrm{T}} (t _ {0}, t) = \boldsymbol {\Phi} (t, t _ {0}).$$

这说明线性系统 $(A(t), B(t), C(t))$ 的状态转移矩阵 $\Phi(t, t_0)$ 是它的对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 的状态转移矩阵 $\Psi(t, t_0)$ 的转置逆，这是线性系统对偶关系的主要特征.

根据定义，系统 $(A(t), B(t), C(t))$ 的能控性矩阵为

$$
\begin{array}{l} \boldsymbol {W} \left(t _ {1}, t _ {0}\right) = \int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {\Phi} \left(t _ {1}: \tau\right) \boldsymbol {B} (\tau) \boldsymbol {B} ^ {\mathrm{T}} (\tau) \boldsymbol {\Phi} ^ {\mathrm{T}} \left(t _ {1}, \tau\right) \mathrm{d} \tau , \\ = \int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {\Psi} (\tau , t _ {1}) \boldsymbol {B} (\tau) \boldsymbol {B} ^ {\mathrm{T}} (\tau) \boldsymbol {\Psi} ^ {\mathrm{T}} (\tau . t _ {1}) \mathrm{d} \tau , \\ = \Psi^ {T} (t _ {0}, t _ {1}) M _ {d} (t _ {1}, t _ {0}) \Psi (t _ {0}, t _ {1}). \\ \end{array}
$$

这里 $M_{d}(t_{1}, t_{0})$ 是系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 的能观测性矩阵. 因为矩阵 $\Psi(t_{0}, t_{1})$ 是非奇异的, 所以矩阵 $W(t_{1}, t_{0})$ 和 $M_{d}(t_{1}, t_{0})$ 的正定性是等价的. 因此, 系统 $(A(t), B(t), C(t))$ 在 $t_{0}$ 时刻完全能控的充要条件是它们的对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 在 $t_{0}$ 时刻完全能观测.

同样可以证明，系统 $(A(t), B(t), C(t))$ 在 $t_0$ 时刻完全能观测的充要条件是它的对偶系统 $(-A^{\mathrm{T}}(t), C^{\mathrm{T}}(t), B^{\mathrm{T}}(t))$ 在 $t_0$ 时刻完全能控.

对定常线性系统，如果系统在某时刻完全能观测，则它必在 $[0, \infty)$ 上也是完全能观测的，所以就不再说“在 $t_0$ 时刻”了。

定理1.3.6 定常线性系统 $(A, B, C)$ 能观测的充要条件是

$$\operatorname{rank} Q _ {o} = n,$$

这里

$$
Q _ {o} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right]. \tag {1.3.15}
$$

称 $Q_{0}$ 为定常线性系统 $(A, B, C)$ 的能观测性矩阵.

定理1.3.6和定理1.3.2是对偶的．通过对偶原理不难得到它的证明.

推论1.3.4 已知定常线性系统 $(A, B, C)$ , 如果 $A$ 的最小多项式是 $k$ 次的, 且 $k < n$ , 那么系统 $(A, B, C)$ 完全能观测的充要条件是

$$
\operatorname{rank} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {k - 1} \end{array} \right] = n.
$$

推论1.3.5 如果定常线性系统 $(A, B, C)$ 是单输出的，那么它完全能观测的充要条件是

$$\det Q _ {o} \neq 0.$$

在研究系统的完全能控性时，可用系统的输入解耦零点来判断系统的能控性，对于系统的完全能观测性，则可以通过输出解耦零点来判别。

定理1.3.7 定常线性系统 $(A, B, C)$ 完全能观测性的充要条件是, 对每个 $s \in \sigma(A)$ 都有

$$
\operatorname{rank} \left[ \begin{array}{c} A - s I _ {n} \\ C \end{array} \right] = n.
$$
