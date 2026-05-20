$$R (s) = X (s) D (s) + Y (s) N (s) \tag {6.38}$$

其中 $X(s)$ 和 $Y(s)$ 分别是 $p \times p$ 和 $p \times q$ 的多项式矩阵。

证 由构造定理的式(6.23)，可以导出

$$R (s) = U _ {1 1} (s) D (s) + U _ {1 2} (s) N (s) \tag {6.39}$$

其中 $U_{11}(s)$ 和 $U_{12}(s)$ 分别为 $p \times p$ 和 $p \times q$ 的多项式矩阵。现表 $U_{11}(s) = X(s)$ 和 $U_{12}(s) = Y(s)$ ，即得(6.38)。于是证明完成。

性质5 和标量多项式时的情况不同，多项式矩阵 $D(s)$ 和 $N(s)$ 的 $\gcd$ 的多项式元的次数可以高于 $D(s)$ 和 $N(s)$ 的多项式元的次数。

我们通过举例来说明这个性质。给定多项式矩阵 $D(s)$ 和 $N(s)$ 如下：

$$
D (s) = \left[ \begin{array}{c c} s & 3 s + 1 \\ - 1 & s ^ {2} + s - 2 \end{array} \right], N (s) = [ - 1 \quad s ^ {2} + 2 s - 1 ]
$$

前面已经求出,它们的一个 gcd 为

$$
R (s) = \left[ \begin{array}{c c} 1 & - s ^ {2} - s + 2 \\ 0 & s + 1 \end{array} \right]
$$

现选定如下的一个单模阵 $W(s)$ :

$$
W (s) = \left[ \begin{array}{c c} s ^ {k} & 1 \\ s ^ {k} + 1 & 1 \end{array} \right], k = 3, 4, \dots
$$

则据性质1可知，如下导出的多项式矩阵

$$
\begin{array}{l} R _ {1} (s) = W (s) R (s) = \left[ \begin{array}{c c} s ^ {k} & 1 \\ s ^ {k} + 1 & 1 \end{array} \right] \left[ \begin{array}{c c} 1 & - s ^ {2} - s + 2 \\ 0 & s + 1 \end{array} \right] \\ = \left[ \begin{array}{c c} s ^ {k} & s ^ {k} (- s ^ {2} - s + 2) + (s + 1) \\ s ^ {k} + 1 & (s ^ {k} + 1) (- s ^ {2} - s + 2) + (s + 1) \end{array} \right] \\ \end{array}
$$

也是 $D(s)$ 和 $N(s)$ 的 $\operatorname{gcrd}$ ，但其多项式元的次数显然高于 $D(s)$ 和 $N(s)$ 的多项式元的次数。

对 gcld 的一点说明 如上对构造定理和最大公因子的性质的讨论都是相对于 gcrd 进行的。但是，考虑到 gcld 和 gcrd 在定义上的对偶性，因此关于 gcld 的性质和构造定理将可很容易地按照对偶关系由 gcrd 的相应结果来导出。由于这个缘故，所以这里不再对 gcld 进行专门的和详细的讨论。
