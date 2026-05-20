$$
\begin{array}{l} [ \overline {{{B}}}, \overline {{{A B}}}, \dots , \overline {{{A}}} ^ {n - 1} \overline {{{B}}} ] = T [ B, A B, \dots , A ^ {n - 1} B ], \\ \left[ \begin{array}{c} \overline {{C}} \\ \overline {{C A}} \\ \vdots \\ \overline {{C A}} ^ {n - 1} \end{array} \right] = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] T ^ {- 1}, \\ \end{array}
$$

则由 T 的非奇异性知引理的结论成立.

假设系统 $(A,B,C)$ 不完全能控，则 $\chi_{1}=\operatorname{span}[B,AB,\cdots,A^{n-1}B]$ 的维数 $\mu$ 小于n.取 $\chi_{1}$ 的一组基 $e_{1},e_{2},\cdots,e_{\mu}$ ，则可将 $R^{n}$ 分解为 $R^{n}=\chi_{1}\oplus\chi_{1}^{\perp}$ .这里 $\chi_{1}^{\perp}$ 表示 $R^{n}$ 中 $\chi_{1}$ 的直交补空间．取 $\chi_{1}^{\perp}$ 的一组基 $e_{\mu+1},e_{\mu+2},\cdots,e_{n}$ ，并记

$$\boldsymbol {T} = \left[ e _ {1}, e _ {2}, \dots , e _ {n} \right].$$

显然，这样构成的矩阵 $\pmb{T}$ 是非奇异的。利用Cayley-Hamilton定理不难证明，子空间 $\mathcal{X}_1$ 是 $A$ 的不变子空间，即 $A\mathcal{X}_1\subset \mathcal{X}_1$ 。因此有

$$
\left\{ \begin{array}{l} A e _ {1} = a _ {1 1} e _ {1} + a _ {2 1} e _ {2} + \dots + a _ {\mu 1} e _ {\mu}, \\ A e _ {2} = a _ {1 2} e _ {1} + a _ {2 2} e _ {2} + \dots + a _ {\mu 2} e _ {\mu}, \\ \quad \vdots \\ A e _ {\mu} = a _ {1 \mu} e _ {1} + a _ {2 \mu} e _ {2} + \dots + a _ {\mu \mu} e _ {\mu}, \\ A e _ {\mu + 1} = a _ {1 \mu + 1} e _ {1} + a _ {2 \mu + 1} e _ {2} + \dots + a _ {\mu \mu + 1} e _ {\mu} + \dots + a _ {n \mu + 1} e _ {n}, \\ \quad \vdots \\ A e _ {n} = a _ {1 n} e _ {1} + a _ {2 n} e _ {2} + \dots + a _ {\mu n} e _ {\mu} + \dots + a _ {n n} e _ {n}, \end{array} \right.
$$

其中 $a_{ij}$ 都是实数， $i=1,2,\cdots,n; j=1,2,\cdots,n.$

如果记

$$
\overline {{{A}}} _ {1} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 \mu} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 \mu} \\ \vdots & \vdots & & \vdots \\ a _ {\mu 1} & a _ {\mu 2} & \dots & a _ {\mu \mu} \end{array} \right], \quad \overline {{{A}}} _ {2} = \left[ \begin{array}{c c c c} a _ {\mu + 1 \mu + 1} & a _ {\mu + 1 \mu + 2} & \dots & a _ {\mu + 1 n} \\ a _ {\mu + 2 \mu + 1} & a _ {\mu + 2 \mu + 2} & \dots & a _ {\mu + 2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n \mu + 1} & a _ {n \mu + 2} & \dots & a _ {n n} \end{array} \right],
