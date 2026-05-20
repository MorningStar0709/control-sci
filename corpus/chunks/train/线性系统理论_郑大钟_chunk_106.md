$$
\begin{array}{l} \left[ \Phi (t _ {0}, t _ {1}) B (t _ {1}) \mid \frac {\partial}{\partial t _ {1}} \Phi (t _ {0}, t _ {1}) B (t _ {1}) \mid \dots \mid \frac {\partial^ {n - 1}}{\partial t _ {1} ^ {n - 1}} \Phi (t _ {0}, t _ {1}) B (t _ {1}) \right] \\ = \Phi (t _ {0}, t _ {1}) [ M _ {0} (t _ {1}) | M _ {1} (t _ {1}) | \dots | M _ {n - 1} (t _ {1}) ] \tag {3.68} \\ \end{array}
$$

由于 $\Phi(t_0, t_1)$ 为非奇异，故由（3.68）和（3.66）可进而导出

$$\operatorname{rank} \left[ \Phi (t _ {0}, t _ {1}) B (t _ {1}) \mid \frac {\partial}{\partial t _ {1}} \Phi (t _ {0}, t _ {1}) B (t _ {1}) \mid \dots \mid \frac {\partial^ {n - 1}}{\partial t _ {1} ^ {n - 1}} \Phi (t _ {0}, t _ {1}) B (t _ {1}) \right] = n \tag {3.69}$$

(2) 进一步证明对 $t_1 > t_0$ , $\Phi(t_0, t)B(t)$ 在 $[t_0, t_1]$ 上行线性无关。采用反证法，反设 (3.69) 成立但 $\Phi(t_0, t)B(t)$ 行线性相关，则存在 $1 \times n$ 的非零常向量 $\alpha$ 使对所有 $t \in [t_0, t_1]$ 成立

$$\alpha \Phi (t _ {0}, t) B (t) = 0 \tag {3.70}$$

这表明，对所有 $t \in [t_{0}, t_{1}]$ 和 $k = 1, 2, \cdots, n - 1$ ，又有

$$\alpha \frac {\partial^ {k}}{\partial t ^ {k}} \Phi (t _ {0}, t) B (t) = 0 \tag {3.71}$$

也即对所有 $t \in [t_0, t_1]$ 成立

$$\alpha \left[ \Phi (t _ {0}, t) B (t) \mid \frac {\partial}{\partial t} \Phi (t _ {0}, t) B (t) \mid \dots \mid \frac {\partial^ {n - 1}}{\partial t ^ {n - 1}} \Phi (t _ {0}, t) B (t) \right] = 0 \tag {3.72}$$

而这又意味着

$$\left[ \Phi (t _ {0}, t) B (t) \mid \frac {\partial}{\partial t} \Phi (t _ {0}, t) B (t) \mid \dots \mid \frac {\partial^ {n - 1}}{\partial t ^ {n - 1}} \Phi (t _ {0}, t) B (t) \right]$$

对所有 $t \in [t_0, t_1]$ 为行线性相关。显然，这和（3.69）相矛盾。所以，反设不成立，即 $\Phi(t_0, t) B(t)$ 对所有 $t \in [t_0, t_1]$ 为行线性无关。

(3) 由 $\Phi(t_0, t) B(t)$ 行线性无关， $t \in [t_0, t_1]$ ，再来证明 $W_c[t_0, t_1]$ 为非奇异。也采用反证法，反设 $W_c[t_0, t_1]$ 奇异，于是存在一个 $1 \times n$ 非零常向量 $\alpha$ 使成立 $\alpha W_c[t_0, t_1] = 0$ ，也即

$$0 = \alpha W _ {c} \left[ t _ {0}, t _ {1} \right] \alpha^ {T} = \int_ {t _ {0}} ^ {t _ {1}} \left[ \alpha \Phi \left(t _ {0}, t\right) B (t) \right] \left[ \alpha \Phi \left(t _ {0}, t\right) B (t) \right] ^ {T} d t \tag {3.73}$$

考虑到上式中被积函数为连续函数，且对所有 $t \in [t_0, t_1]$ 是非负的，所以由（3.73）又可导出

$$\alpha \Phi (t _ {0}, t) B (t) = 0, \quad t \in [ t _ {0}, t _ {1} ] \tag {3.74}$$

而这是和已知 $\Phi(t_0, t) B(t)$ 行线性无关相矛盾的。这表明，反设不成立，即 $W_c[t_0, t_1]$ 为非奇异。

（4）由 $W_{c}[t_{0}, t_{1}]$ 为非奇异， $t_{1} \in J, t_{1} > t_{0}$ ，再利用格拉姆矩阵判据，就证得系统在时刻 $t_{0}$ 为完全能控。至此，证明完成。

例 考虑如下的线性时变系统:
