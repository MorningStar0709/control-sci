$$
\left[ \begin{array}{c} s ^ {k _ {1}} \hat {\xi} _ {1} (s) \\ \vdots \\ s ^ {k _ {p}} \hat {\xi} _ {p} (s) \end{array} \right] = \left[ \begin{array}{c c c} s ^ {k _ {1}} & & \\ & \ddots & \\ & & s ^ {k _ {p}} \end{array} \right] \left[ \begin{array}{c} \hat {\xi} _ {1} (s) \\ \vdots \\ \hat {\xi} _ {p} (s) \end{array} \right] = S (s) \hat {\xi} (s) = \hat {u} _ {o} (s) \tag {9.107}
$$

而其输出的拉普拉斯变换为

$$
\left[ \begin{array}{c} s ^ {k _ {1} - 1} \hat {\xi} _ {1} (s) \\ \vdots \\ \hat {\xi} _ {1} (s) \\ \hdashline \vdots \\ \vdots \\ \vdots \\ \hdashline s ^ {k _ {p} - 1} \hat {\xi} _ {p} (s) \\ \vdots \\ \hat {\xi} _ {p} (s) \end{array} \right] = \left[ \begin{array}{c c c c} s ^ {k _ {1} - 1} & & & \\ \vdots & & & \\ \vdots & & & \\ s & & & \\ 1 & & & \\ \hdashline \ddots & & & \\ & & \hdashline s ^ {k _ {p} - 1} & \\ & \vdots & & \\ & s & & \\ & & 1 \end{array} \right] \quad \left[ \begin{array}{c} \hat {\xi} _ {1} (s) \\ \hat {\xi} _ {2} (s) \\ \vdots \\ \vdots \\ \vdots \\ \hat {\xi} _ {p} (s) \end{array} \right] = \psi (s) \hat {\xi} (s) = \hat {y} _ {o} (s) \tag {9.108}
$$

所以它的传递函数矩阵即为核 MFD $\psi(s)S^{-1}(s)$ 。这表明，图 9.6 所示的积分链结构，就是核 MFD $\psi(s)S^{-1}(s)$ 的一个实现。

(4) $\psi(s)S^{-1}(s)$ 相应的核实现 $(A_{c}^{\circ}, B_{c}^{\circ}, C_{c}^{\circ})$ 可由图9.6的积分链来定出。为此，定义状态 $x^{o}$ 并表输入 $u_{o}$ 和输出 $y_{o}$ 为：

$$
x ^ {o} = y _ {o} = \left[ \begin{array}{c} \xi_ {1} ^ {(k _ {1} - 1)} \\ \vdots \\ \xi_ {1} \\ - - - - - \\ \vdots \\ - - - - - \\ \xi_ {p} ^ {(k _ {p} - 1)} \\ \vdots \\ \xi_ {p} \end{array} \right], \quad u _ {o} = \left[ \begin{array}{c} \xi_ {1} ^ {(k _ {1})} \\ \vdots \\ \vdots \\ \vdots \\ \xi_ {p} ^ {(k _ {p})} \end{array} \right] \tag {9.109}
$$

于是，由图9.6所示的积分链即可导出
