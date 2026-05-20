证明 必要性. 假设系统 (1.5.4) 是完全能控和完全能观测的. 由式 (1.2.8), (1.2.9) 知, 存在 $s$ 的多项式 $p_k(s)$ ( $k = 0, 1, \cdots, n-1$ ), 使得 $(sI_n - A)^{-1} = \frac{1}{\Delta(s)} \sum_{k=0}^{n-1} p_k(s)A^k$ . 记 $G(s) = \sum_{k=0}^{n-1} p_k(s)A^k$ , 则有

$$\Delta (s) \boldsymbol {I} _ {n} = (s \boldsymbol {I} _ {n} - \boldsymbol {A}) \boldsymbol {G} (s). \tag {1.5.8}$$

设 $s_0$ 是 $\Delta(s)$ 的一个零点. 对于 $s_0 \neq 0$ 的情况, 由式 (1.5.8) 知

$$(s _ {0} \boldsymbol {I} _ {n} - \boldsymbol {A}) \boldsymbol {G} (s _ {0}) = 0. \tag {1.5.9}$$

这说明 $G(s_0)$ 的每一非零列都是矩阵 $\pmb{A}$ 对应于特征值 $s_0$ 的特征向量，所以

$$c A G (s _ {0}) b = s _ {0} c G (s _ {0}) b. \tag {1.5.10}$$

如果有 $p(s_0) = 0$ ，则由 $p(s_0) = cG(s_0)b$ 知 $\pmb {cG}(s_0)\pmb {b} = 0,$ 进而由式(1.5.10）知

$$c A G (s _ {0}) b = 0.$$

利用等式 (1.5.9), (1.5.10) 可以递推地证明

$$\boldsymbol {c} \boldsymbol {A} ^ {k} \boldsymbol {G} (s _ {0}) \boldsymbol {b} = 0, \quad k = 1, 2, \dots , n - 1.$$

因此当 $p(s_0) = 0$ ，即 $\pmb {cG}(s_0)\pmb {b} = 0$ 时，有

$$\boldsymbol {Q} _ {o} ^ {\mathrm{T}} \boldsymbol {Q} _ {o} \boldsymbol {G} (s _ {0}) \boldsymbol {b} = 0. \tag {1.5.11}$$

由 $(A, C)$ 能观测知 $Q_{o}^{\mathrm{T}} Q_{o}$ 为满秩方阵. 所以从式 (1.5.11) 知

$$\boldsymbol {G} (s _ {0}) \boldsymbol {b} = 0, \tag {1.5.12}$$

即

$$\sum_ {k = 0} ^ {n - 1} p _ {k} (s _ {0}) \boldsymbol {A} ^ {k} \boldsymbol {b} = 0,$$

或者

$$
\boldsymbol {Q} _ {c} \left[ \begin{array}{c} p _ {0} (s _ {0}) \\ p _ {1} (s _ {0}) \\ \vdots \\ 1 \end{array} \right] = 0.
$$

这表明 $b, Ab, \cdots, A^{n-1}b$ 线性相关。这与 $(A, b)$ 完全能控矛盾，所以 $p(s_0) \neq 0$ .

当 $s_0 = 0$ 时，由式(1.5.11)得 $\pmb{cAG}(s_0)\pmb {b} = 0.$ 由此从式(1.5.11)得

$$\boldsymbol {c} \boldsymbol {A} ^ {k} \boldsymbol {G} (s _ {0}) \boldsymbol {b} = 0, \quad k = 1, 2, \dots , n - 1. \tag {1.5.13}$$

如果 $p(s_0) = 0$ ，则由 $p(s) = cG(s)b$ 知

$$\boldsymbol {c} \boldsymbol {G} (s _ {0}) \boldsymbol {b} = 0. \tag {1.5.14}$$

由于 $(A, c)$ 完全能观测，那么由式 (1.5.13)，(1.5.14) 类似地可以得到式 (1.5.12). 同样，这与 $(A, b)$ 完全能控矛盾。因此， $p(s_0) \neq 0$ 。从而由 $s_0$ 的任意性知， $\Delta(s)$ 与 $p(s)$ 互质，即 $W(s)$ 没有零极相消。

充分性. 假设系统 (1.5.4) 的传递函数没有零极相消, 而系统 (1.5.4) 不能控或不能观测, 则由定理 1.3.10 和式 (1.3.20) 知, 存在一个坐标变换, 使得它变成形如 (1.3.18) 的系统, 且有 $n_1 < n$ 和传递函数 (1.3.20). 由于 $\pmb{W}(s)$ 的特征多项式 $\det(sI_{n_1 - \overline{A}_{11}})$ 的次数 $n_1$ 小于 $n$ , 这与 $\pmb{W}(s)$ 的特征多项式 $\Delta(s)$ 为 $n$ 次相矛盾.

对多输入多输出系统，有

定理 1.5.3 定常线性系统 (1.4.16) 完全能控且完全能观测的充要条件是, $sI_{n} - A$ 与 $B$ 左互质; $sI_{n} - A$ 与 $C$ 右互质.

这个定理是定理1.3.3和定理1.3.7的直接推论，在此不再详细讨论.
