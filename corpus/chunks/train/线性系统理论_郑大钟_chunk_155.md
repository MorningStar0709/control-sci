(ii) 由 (4.46) 可知, 零平衡状态 $x_{t} = 0$ 为渐近稳定, 当且仅当 $\| e^{At}\|$ 对一切 $t \geqslant 0$ 为有界, 且当 $t \to \infty$ 时 $\| e^{At}\| \to 0$ . 如上所证, $\| e^{At}\|$ 有界, 当且仅当 $A$ 的所有特征值均具有负或零实部。再利用 (4.48) 和 (4.49) 又知, 当 $t \to \infty$ 时 $\| e^{At}\| \to 0$ , 当且仅当 $t \to \infty$ 时 $[t^{\beta_i}e^{\alpha_i t + j\omega_i t}] \to 0$ , 而这等价于 $A$ 的特征值均具有负实部。结论 (ii) 证毕。

而且，还可看出，由于所讨论的系统为线性的和定常的，所以其为稳定时必是一致稳定的，当其为渐近稳定时必是大范围一致渐近稳定的。

例 给定线性定常自治系统

$$
\dot {x} = \left[ \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

容易定出,其平衡状态为

$$
\boldsymbol {x} _ {e} = \left[ \begin{array}{l} 0 \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

其中 $x_{2}$ 和 $x_{3}$ 为任意实数。也即，状态空间中 $x_{2} - x_{3}$ 平面上的每一个点均为平衡状态。再之，可定出 $\pmb{A}$ 的特征值为 $-1,0,0$ ，而由

$$
\begin{array}{l} (s I - A) ^ {- 1} = \left[ \begin{array}{c c c} s + 1 & 0 & 0 \\ 0 & s & 0 \\ 0 & 0 & s \end{array} \right] ^ {- 1} = \frac {1}{s ^ {2} (s + 1)} \left[ \begin{array}{c c c} s ^ {2} & 0 & 0 \\ 0 & s (s + 1) & 0 \\ 0 & 0 & s (s + 1) \end{array} \right] \\ = \frac {1}{s (s + 1)} \left[ \begin{array}{c c c} s & 0 & 0 \\ 0 & (s + 1) & 0 \\ 0 & 0 & (s + 1) \end{array} \right] \\ \end{array}
$$

可知其最小多项式为 $s(s + 1)$ ，所以特征值0仅是最小多项式的一个单根。于是，根据特征值判据即知，此系统的每个平衡状态是李亚普诺夫意义下稳定的，但不是渐近稳定的。

判断线性定常自治系统(4.44)的运动稳定性的另一种方法，是直接利用李亚普诺夫第二方法的定理。并且，由此可导出相应的判据。

结论2[李亚普诺夫判据] 线性定常系统(4.44)的零平衡状态 $x_{e} = 0$ 为渐近稳定的充分必要条件，是对任意给定的一个正定对称矩阵 $Q$ ，如下形式的李亚普诺夫矩阵方程

$$A ^ {T} P + P A = - Q \tag {4.50}$$

有唯一正定对称矩阵解 P.

证 充分性： $P$ 正定，欲证 $\pmb{x}_{\epsilon} = 0$ 为渐近稳定。为此，取 $V(\pmb {x}) = \pmb{x}^{T}\pmb {P}\pmb{x}$ ，则由 $P = P^T >0$ 可知 $V(\pmb {x})$ 为正定。进而，可得

$$
\begin{array}{l} \dot {V} (\boldsymbol {x}) = \dot {\boldsymbol {x}} ^ {T} P \boldsymbol {x} + \boldsymbol {x} ^ {T} P \dot {\boldsymbol {x}} = (A \boldsymbol {x}) ^ {T} P \boldsymbol {x} + \boldsymbol {x} ^ {T} P (A \boldsymbol {x}) \\ = \boldsymbol {x} ^ {T} \left(A ^ {T} P + P A\right) \boldsymbol {x} = - \boldsymbol {x} ^ {T} Q \boldsymbol {x} \tag {4.51} \\ \end{array}
$$

考虑到 $Q = Q^T > 0$ 又可知 $\dot{V}(\pmb{x})$ 为负定。从而，由李亚普诺夫稳定性定理即知，零平衡状态 $\pmb{x}_{\varepsilon} = \pmb{0}$ 为渐近稳定。

必要性： $x_{i} = 0$ 为渐近稳定，欲证 $P$ 为唯一且正定。为此，考虑如下的矩阵方程

$$\dot {X} = A ^ {T} X + X A, \quad X (0) = Q, t \geqslant 0 \tag {4.52}$$

易知其解矩阵为

$$X (t) = e ^ {A ^ {T} t} Q e ^ {A t}, \quad t \geqslant 0 \tag {4.53}$$

再对(4.52)由 $t = 0$ 至 $t = \infty$ 求取积分，可得
