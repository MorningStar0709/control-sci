定理 1.5.4 设 $W(s)$ 是一个 $m \times r$ 真有理分式矩阵， $(A, B, C)$ 是它的一个实现。 $(A, B, C)$ 是一个最小实现的充分必要条件是 $(A, B)$ 能控和 $(A, C)$ 能观测。

证明 充分性. 设 $(A, B)$ 能控, $(A, C)$ 能观测, 那么由定理 1.5.3 知, $sI_{n} - A$ 与 $B$ 左互质, $sI_{n} - A$ 与 $C$ 右互质, 从而 $C(sI_{n} - A)^{-1}B$ 没有零极相消. 如果 $(A, B, C)$ 不是 $W(s)$ 的最小实现, 那么, 必有 $(\overline{A}, \overline{B}, \overline{C})$ 是 $W(s)$ 的最小实现. 若 $A$ 是 $n \times n$ 矩阵, $\overline{A}$ 是 $\overline{n} \times \overline{n}$ 矩阵, 则 $\overline{n} < n$ . 根据定义

$$\boldsymbol {W} (s) = \overline {{{C}}} (s \boldsymbol {I} _ {n} - \overline {{{A}}}) ^ {- 1} \overline {{{B}}} = C (s \boldsymbol {I} _ {n} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B},$$

这与 $C(sI_n - A)^{-1}B$ 没有相消矛盾. 因此, $(A,B,C)$ 是 $W(s)$ 的一个最小实现.

必要性. 设 $(A, B, C)$ 是 $W(s)$ 的最小实现. 如果 $(A, B)$ 不能控, 则由定理1.3.10知, $W(s)$ 必存在一个阶数更低的实现, 而这与 $(A, B, C)$ 为最小实现矛盾. 所以, $(A, B)$ 能控. 同理可知 $(A, C)$ 能观测.

定理 1.5.5 $W(s)$ 的两个最小实现 $(A_{1}, B_{1}, C_{1})$ 和 $(A_{2}, B_{2}, C_{2})$ 是代数等价的.

证明 预解矩阵的无穷级数表达式为

$$(s I _ {n} - A _ {i}) ^ {- 1} = \sum_ {j = 0} ^ {\infty} A _ {i} ^ {j} s ^ {- (j + 1)}, \quad i = 1, 2, \tag {1.5.15}$$

这里 $n$ 表示矩阵 $\pmb{A}_i$ 的阶数，或者说 $W(s)$ 的最小实现的阶数.

因为 $(A_{1}, B_{1}, C_{1})$ 和 $(A_{2}, B_{2}, C_{2})$ 都是 $W(s)$ 的最小实现，所以有

$$\boldsymbol {W} (s) = \boldsymbol {C} _ {1} \left(s \boldsymbol {I} _ {n} - \boldsymbol {A} _ {1}\right) ^ {- 1} \boldsymbol {B} _ {1} = \boldsymbol {C} _ {2} \left(s \boldsymbol {I} _ {n} - \boldsymbol {A} _ {2}\right) ^ {- 1} \boldsymbol {B} _ {2}.$$

将式 (1.5.15) 代入上式，然后比较等式两边 $s$ 同次幂的系数后得出

$$C _ {1} A _ {1} ^ {j} B _ {1} = C _ {2} A _ {2} ^ {j} B _ {2}, \quad j = 0, 1, 2 \dots . \tag {1.5.16}$$

令 $(A_{i}, B_{i}, C_{i})$ 的能控性矩阵为 $Q_{ci}$ , 能观测性矩阵为 $Q_{oi}$ , $i = 1, 2$ , 则

$$
\boldsymbol {Q} _ {c i} = [ \boldsymbol {B} _ {i}, \boldsymbol {A} \boldsymbol {B} _ {i}, \dots , \boldsymbol {A} ^ {n - 1} \boldsymbol {B} _ {i} ], \qquad \boldsymbol {Q} _ {o i} = \left[ \begin{array}{c} \boldsymbol {C} _ {i} \\ \boldsymbol {C} _ {i} \boldsymbol {A} \\ \vdots \\ \boldsymbol {C} _ {i} \boldsymbol {A} ^ {n - 1} \end{array} \right].
$$

利用式 (1.5.16) 可得

$$Q _ {o 1} Q _ {c 1} = Q _ {o 2} Q _ {c 2}. \tag {1.5.17}$$

由于 $(A_{i}, B_{i})$ 能控， $(A_{i}, C_{i})$ 能观测，因此必有 $Q_{oi}^{\mathrm{T}} Q_{oi}$ 和 $Q_{ci} Q_{ci}^{\mathrm{T}}$ 是非奇异矩阵. 令
