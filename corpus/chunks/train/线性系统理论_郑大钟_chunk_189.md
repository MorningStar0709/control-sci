$$\tilde {k} _ {i} = \left[ k _ {j 0}, k _ {j 1}, \dots , k _ {j d _ {j}}, 0 \dots 0 \right]$$

并且，由此可以导出：

$$
\widetilde {C} (s I - \widetilde {A} + \widetilde {B} \widetilde {K}) ^ {- 1} \widetilde {B} = \left[ \begin{array}{c c c} \widetilde {c} _ {1} (s I - \widetilde {A} _ {1} + \widetilde {b} _ {1} \widetilde {k} _ {1}) ^ {- 1} \widetilde {b} _ {1} & & \\ & \ddots & \\ & & \widetilde {c} _ {p} (s I - \widetilde {A} _ {p} + \widetilde {b} _ {p} \widetilde {k} _ {p}) ^ {- 1} \widetilde {b} _ {p} \end{array} \right]
$$

和

$$
\tilde {A} _ {i} - \tilde {b} _ {i} \tilde {k} _ {i} = \left[ \begin{array}{c c c c} 0 & & & \\ \vdots & I _ {d _ {i}} & & \\ 0 & & & 0 \\ - k _ {j 0} & - k _ {j 1} \dots - k _ {j d _ {i}} & & \\ - & * & & * \end{array} \right]
$$

这表明， $\widetilde{K}$ 的结构形式保证了解耦控制的实现，而 $\tilde{k}_i (i = 1, 2, \cdots, p)$ 的元则由解耦后的第 $i$ 个单输入-单输出控制系统的期望极点组所决定。而且，不难看出，由于需保证实现解耦，状态反馈所能控制的不是 $\tilde{A}_i$ 的全部特征值。

第6步：对于所讨论的受控系统 $\dot{x} = Ax + Bu, y = Cx$ ，使其实现解耦和对解耦后各单输入-单输出系统进行期望的极点配置的 $\{K, L\}$ 为：

$$K = E ^ {- 1} F + E ^ {- 1} \widetilde {K} Q, L = E ^ {- 1}$$

例 给定双输入-双输出的线性定常受控系统为

$$
\dot {x} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 3 & 0 & 0 & 2 \\ 0 & 0 & 0 & 1 \\ 0 & - 2 & 0 & 0 \end{array} \right] x + \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] u

y = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right] x
$$

易知,其为能控且能观测。

① 计算 $d_{i}(i = 1,2)$ 和 $E_{i}(i = 1,2)$

因为

$$
\mathbf {c} _ {i} B = \left[ \begin{array}{l l l l} 1 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{l l} 0 & 0 \end{array} \right]

\mathbf {c} _ {1} A B = \left[ \begin{array}{l l l l} 1 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 3 & 0 & 0 & 2 \\ 0 & 0 & 0 & 1 \\ 0 & - 2 & 0 & 0 \end{array} \right] \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] - \left[ \begin{array}{l l} 1 & 0 \end{array} \right]

\mathbf {c} _ {2} B = \left[ \begin{array}{l l l l} 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{l l} 0 & 0 \end{array} \right]

\mathbf {c} _ {2} A B = \left[ \begin{array}{l l l l} 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 3 & 0 & 0 & 2 \\ 0 & 0 & 0 & 1 \\ 0 & - 2 & 0 & 0 \end{array} \right] \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] = [ 0, 1 ]
$$

由此，即可定出

$$
\begin{array}{l} d _ {1} = 1, \quad d _ {2} = 1 \\ E _ {1} = [ 1 \quad 0 ], \quad E _ {2} = [ 0 \quad 1 ] \\ \end{array}
$$

② 断判可解耦性

显然，可解耦性判别阵
