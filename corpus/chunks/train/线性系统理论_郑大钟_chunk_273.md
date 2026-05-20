# 习题

6.1 判断下列多项式矩阵是否为非奇异:

$$
Q _ {1} (s) = \left[ \begin{array}{c c} s ^ {2} + 3 s + 4 & s + 1 \\ s + 2 & 1 \end{array} \right] \tag {i}

Q _ {2} (s) = \left[ \begin{array}{c c} s + 2 & s + 3 \\ s ^ {2} + 3 s + 2 & s ^ {2} + 4 s + 3 \end{array} \right] \tag {ii}

Q _ {3} (s) = \left[ \begin{array}{c c c} s + 3 & s + 4 & 1 \\ 1 & s + 1 & s + 2 \\ 0 & s ^ {2} + s & s \end{array} \right] \tag {iii}
$$

6.2 判断下列各多项式向量组是否为线性无关:

$$
\left[ \begin{array}{c} s ^ {2} + 7 s + 1 2 \\ s + 3 \end{array} \right], \left[ \begin{array}{c} s ^ {2} + 5 s + 4 \\ s + 1 \end{array} \right] \tag {i}

\text {(ii)} \left[ \begin{array}{c} 0 \\ s + 3 \\ s + 1 \end{array} \right], \quad \left[ \begin{array}{c} 4 \\ s + 2 \\ s ^ {2} + s \end{array} \right], \quad \left[ \begin{array}{c} s + 1 \\ s \\ 3 \end{array} \right]
$$

6.3 判断下列各多项式矩阵是否为单模矩阵:

$$
Q _ {1} (s) = \left[ \begin{array}{c c} s + 3 & s + 2 \\ s ^ {2} + 2 s - 1 & s ^ {2} + s \end{array} \right] \tag {i}

Q _ {2} (s) = \left[ \begin{array}{c c} s + 4 & 1 \\ s ^ {2} + 2 s + 1 & s + 2 \end{array} \right] \tag {ii}

Q _ {3} (s) = \left[ \begin{array}{c c c} s + 1 & 1 & s + 1 \\ 0 & s + 2 & 3 \\ s + 3 & 1 & s + 3 \end{array} \right] \tag {iii}
$$

6.4 表下列单模阵为初等矩阵的乘积:

$$
Q (s) = \left[ \begin{array}{c c c} s ^ {2} + 2 s + 1 & s + 4 & 1 \\ 1 & - 1 & 0 \\ - (s ^ {2} + 4) & s ^ {2} & 0 \end{array} \right]
$$

6.5 令 P 和 $Q(s)$ 分别为 $n \times n$ 常量阵和多项式矩阵，现知 $Q(s)$ 为单模矩阵，则能否断言 $PQ(s)$ 也必为单模矩阵，说明理由。

6.6 将下列多项式矩阵变换为行埃尔米特形：

$$
Q (s) = \left[ \begin{array}{c c c c} 0 & 0 & (s + 1) ^ {2} & - s ^ {2} + s + 1 \\ 0 & 0 & - (s + 1) & s - 1 \\ s + 1 & s ^ {2} & s ^ {2} + s + 1 & s \end{array} \right]
$$

6.7 求出下列两个多项式矩 $D(s)$ 和 $N(s)$ 的一个 $\gcd$ :

$$
D (s) = \left[ \begin{array}{l l} s ^ {2} + 2 s & s + 3 \\ 2 s ^ {2} + s & 3 s - 2 \end{array} \right], N (s) = [ s \quad 1 ]
$$

6.8 证明 gcld 的构造定理：给定 $q \times q$ 和 $q \times p$ 的多项式矩阵 $A(s)$ 和 $B(s)$ ，如果可找到一个 $(p + q) \times (p + q)$ 的单模阵 $V(s)$ ，使成立

$$
\begin{array}{l} [ A (s) \quad B (s) ] V (s) = [ A (s) \quad B (s) ] \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \\ = [ L (s) \quad 0 ] \\ \end{array}
$$

则 $q \times q$ 的多项式矩阵 $L(s)$ 即为 $A(s)$ 和 $B(s)$ 的一个 $\mathbf{g}\mathrm{c}\mathrm{l}\mathrm{d}_{\circ}$

6.9 证明：设 $L(s)$ 是 $q \times q$ 和 $q \times p$ 的多项式矩阵 $A(s)$ 和 $B(s)$ 的一个 $\gcd$ ，则 $L(s)$ 必可表为

$$L (s) = A (s) X (s) + B (s) Y (s)$$

其中 $X(s)$ 和 $Y(s)$ 分别为 $q \times q$ 和 $p \times q$ 的多项式矩阵。

6.10 判断下列矩阵对是否为右互质：

$$
D (s) = \left[ \begin{array}{c c} s + 1 & 0 \\ s ^ {2} + s - 2 & s - 1 \end{array} \right], N (s) = [ s + 2 \quad s + 1 ] \tag {i}

D (s) = \left[ \begin{array}{c c} s - 1 & 0 \\ s ^ {2} + s - 2 & s + 1 \end{array} \right], N (s) = [ s - 1 \quad s + 1 ]
