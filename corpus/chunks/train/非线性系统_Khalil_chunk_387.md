它可能随 x 变化,但如果 $\Delta = \operatorname{span}\left\{f_{1}, \cdots, f_{k}\right\}$ , 其中 $\left\{f_{1}(x), \cdots, f_{k}(x)\right\}$ 对所有 $x \in D$ 是线性独立的, 则对于所有 $x \in D$ , $\dim(\Delta(x)) = k$ 。此时称 $\Delta$ 是 D 上的非奇异分布, 由 $f_{1}, \cdots, f_{k}$ 生成。

如果 $g_{1}\in \Delta ,\quad g_{2}\in \Delta \Rightarrow [g_{1},g_{2}]\in \Delta$

则分布 $\Delta$ 是对合的。如果 $\Delta$ 是 D 上的非奇异分布，由 $f_{1}, \cdots, f_{k}$ 生成，则可以验证（见习题 13.9）当且仅当 $[f_{i}, f_{j}] \in \Delta, \forall 1 \leqslant i, j \leqslant k$

时, $\Delta$ 是对合的。

例13.11 设 $D = R^3, \Delta = \operatorname{span}\{f_1, f_2\}$ , 其中

$$
f _ {1} = \left[ \begin{array}{c} 2 x _ {2} \\ 1 \\ 0 \end{array} \right], f _ {2} = \left[ \begin{array}{c} 1 \\ 0 \\ x _ {2} \end{array} \right]
$$

可以验证,对于所有 $x \in D$ , $\dim(\Delta(x)) = 2$ , 并且当且仅当对于所有 $x \in D$ , $\operatorname{rank}[f_{1}(x), f_{2}(x), [f_{1}, f_{2}](x)] = 2$ 时,

$$
[ f _ {1}, f _ {2} ] = \frac {\partial f _ {2}}{\partial x} f _ {1} - \frac {\partial f _ {1}}{\partial x} f _ {2} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right]
$$

$\left[f_{1},f_{2}\right]\in\Delta$ 。但是

$$
\operatorname{rank} \left[ f _ {1} (x), f _ {2} (x), [ f _ {1}, f _ {2} ] (x) \right] = \operatorname{rank} \left[ \begin{array}{c c c} 2 x _ {2} & 1 & 0 \\ 1 & 0 & 0 \\ 0 & x _ {2} & 1 \end{array} \right] = 3, \forall x \in D
$$

因此, $\Delta$ 不是对合的。

例13.12 设 $D = \{x\in R^3 |x_1^2 +x_3^2\neq 0\}$ ， $\Delta = \mathrm{span}\{f_1,f_2\}$ ，其中

$$
f _ {1} = \left[ \begin{array}{c} 2 x _ {3} \\ - 1 \\ 0 \end{array} \right], f _ {2} = \left[ \begin{array}{c} - x _ {1} \\ - 2 x _ {2} \\ x _ {3} \end{array} \right]
$$

可以验证对于所有 $x \in D, \dim(\Delta(x)) = 2$ ，且有

$$
\left[ f _ {1}, f _ {2} \right] = \frac {\partial f _ {2}}{\partial x} f _ {1} - \frac {\partial f _ {1}}{\partial x} f _ {2} = \left[ \begin{array}{c} - 4 x _ {3} \\ 2 \\ 0 \end{array} \right]
$$

和 $\operatorname{rank}[f_1(x), f_2(x), [f_1, f_2](x)] = \operatorname{rank}\left[ \begin{array}{ccc} 2x_3 & -x_1 & -4x_3 \\ -1 & -2x_2 & 2 \\ 0 & x_3 & 0 \end{array} \right] = 2, \forall x \in D$

因此， $[f_1,f_2]\in \Delta$ 。由于 $[f_2,f_1] = -[f_1,f_2]$ ，故可以推出 $\Delta$ 是对合的。

现在我们讨论这类可反馈线性化的系统。

定理 13.2 对于系统(13.27)，当且仅当存在定义域 $D_{0} \subset D$ ，使得

1. 对于所有 $x \in D_{0}$ ，矩阵 $\mathcal{G}(x) = [g(x), ad_{f} g(x), \cdots, ad_{f}^{n-1} g(x)]$ 的秩为 n，  
2. 分布 $D = \operatorname{span}\left\{ g, ad_{f}g, \cdots, ad_{f}^{n-2}g \right\}$ 在 $D_{0}$ 上是对合的，

则该系统是可反馈线性化的。

◇

证明: 见附录 C.22。
