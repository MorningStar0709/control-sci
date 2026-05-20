$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} | (\varphi_ {n k}, b _ {j}) | ^ {2} <   \infty , \quad 1 \leqslant j \leqslant m, \\ \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} | (\varphi_ {n k}, x) | ^ {2} <   \infty , \quad \forall x \in H. \\ \end{array}
$$

令

$$\alpha_ {n j} = \sum_ {k = 1} ^ {r _ {n}} (b _ {j}, \varphi_ {n k}) (\varphi_ {n k}, x), \quad n \geqslant 1, 1 \leqslant j \leqslant m, \tag {10.2.22}$$

则对于任意固定的 $j, 1 \leqslant j \leqslant m$ ，有

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \left| \alpha_ {n j} \right| \leqslant \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} \left| (\varphi_ {n k}, b _ {j}) \right| | (\varphi_ {n k}, x) | \\ \leqslant \left(\sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} | (\varphi_ {n k}, b _ {j}) | ^ {2}\right) ^ {\frac {1}{2}} \left(\sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} | (\varphi_ {n k}, x) | ^ {2}\right) ^ {\frac {1}{2}} <   \infty . \\ \end{array}
$$

因此对于数列 $\{\lambda_n\}$ 和 $\{\alpha_{nj}\} (1\leqslant j\leqslant m)$ , 引理 10.2.1 的条件满足, 从而由

$$\sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {r _ {n}} \mathrm{e} ^ {\lambda_ {n} t} (\varphi_ {n k}, b _ {j}) (\varphi_ {n k}, x) = 0, \quad \forall t \geqslant 0, 1 \leqslant j \leqslant m$$

推出 $\alpha_{nj} = 0, \forall n \geqslant 1, 1 \leqslant j \leqslant m.$

另一方面，由于解析性，我们可以把

$$\sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \sum_ {k = 1} ^ {r _ {n}} (x, \varphi_ {n k}) (\varphi_ {n k}, b _ {j}) = 0, \quad j = 1, \dots , m, 0 \leqslant t \leqslant t _ {f}$$

延拓到所有 $t > 0$ . 因此我们证明了, 上式成立等价于 $\alpha_{kj} = 0, \forall n \geqslant 1, 1 \leqslant j \leqslant m$ . 现在我们把式 (10.2.22) 写成向量-矩阵形式.

$$
\left[ \begin{array}{c} \alpha_ {n 1} \\ \alpha_ {n 1} \\ \vdots \\ \alpha_ {n r _ {n}} \end{array} \right] = \left[ \begin{array}{c c c c} (b _ {1}, \varphi_ {n 1}) & (b _ {2}, \varphi_ {n 1}) & \dots & (b _ {m}, \varphi_ {n 1}) \\ (b _ {2}, \varphi_ {n 2}) & (b _ {2}, \varphi_ {n 2}) & \dots & (b _ {m}, \varphi_ {n 2}) \\ \vdots & \vdots & & \vdots \\ (b _ {1}, \varphi_ {n r _ {n}}) & (b _ {2}, \varphi_ {n r _ {n}}) & \dots & (b _ {m}, \varphi_ {n r _ {n}}) \end{array} \right] \left[ \begin{array}{c} (\varphi_ {n 1}, x) \\ (\varphi_ {n 1}, x) \\ \vdots \\ (\varphi_ {n r _ {n}}, x) \end{array} \right].
$$

注意

$$(\varphi_ {n k}, x) = 0, \quad n \geqslant 1, \quad 1 \leqslant k \leqslant r _ {n} \Longleftrightarrow x = 0.$$

但显然

$$\mathcal {N} (B _ {n}) = \{0 \} \Longleftrightarrow \mathcal {N} (B _ {n} ^ {*} B _ {n}) = \{0 \} \Longleftrightarrow \operatorname{rank} B _ {n} = r _ {n},$$
