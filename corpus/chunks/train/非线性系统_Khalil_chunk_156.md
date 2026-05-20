4.67 设 A 是系统(4.61)在原点线性化的矩阵, 即 $A = \left[\frac{\partial f}{\partial x}\right](0)$ 。证明: 如果 A 的所有特征值的模都小于 1, 则原点是渐近稳定的。

4.68 设 $x = 0$ 是非线性离散时间系统 $x(k + 1) = f(x(k))$ 的平衡点, 其中 $f: D \to R^n$ 是连续可微的, 并且 $D = \{x \in R^n \mid \| x \| < r\}$ 。设 $C, \gamma < 1$ 和 $r_0$ 是正常数, 且有 $r_0 < r / C$ 。设 $D_0 = \{x \in R^n \mid \| x \| < r_0\}$ 。假设该系统的解满足

$$\| x (k) \| \leqslant C \| x (0) \| \gamma^ {k}, \forall x (0) \in D _ {0}, \forall k \geqslant 0$$

试证明存在函数 $V: D_{0} \rightarrow R$ ，满足

$$c _ {1} \| x \| ^ {2} \leqslant V (x) \leqslant c _ {2} \| x \| ^ {2}\Delta V (x) = V (f (x)) - V (x) \leqslant - c _ {3} \| x \| ^ {2}\left| V (x) - V (y) \right| \leqslant c _ {4} \| x - y \| (\| x \| + \| y \|)$$

其中，所有 $x, y \in D_0, c_1, c_2, c_3$ 和 $c_4$ 为正常数。
