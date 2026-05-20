$$\phi_ {t} ^ {X} (x) = x + X (x) t + o \left(\left| t \right| ^ {2}\right),$$

可证明式 (3.6.13). 因为 Brockett[3] 说过, 要理解 Lie 括号的意义, 你至少在一生中要把上面的证明做一次, 因此我们将细节留给读者.

命题3.6.4 $V(M)$ 带上上述定义的Lie括号是一个Lie代数.

证明 定义 3.2.8 的 L1 和 L2 由等式 (3.6.9) 直接可得. 我们证明 Jacobi 等式. 设 $h \in C^{r}(M)$ , 那么

$$
\begin{array}{l} ([ X, [ Y, Z ] ] + [ Y, [ Z, X ] ] + [ Z, [ X, Y ] ]) (h) \\ = X (Y Z (h) - Z Y (h)) - (Y Z - Z Y) X (h) + Y (Z X (h) \quad X Z (h)) \\ - (Z X - X Z) Y (h) + Z (X Y (h) - Y X (h)) - (X Y - Y X) Z (h) = 0, \\ \forall h \in C ^ {r} (M). \\ \end{array}
$$

例3.6.3 考虑一个控制系统

$$\dot {x} = f (x) + g (x) u, \quad x \in \mathbb {R} ^ {n}, \tag {3.6.14}$$

这里 $f(x)$ 和 $g(x)$ 可看作 $\mathbb{R}^n$ 上的向量场. 由 $f(x)$ 和 $g(x)$ 生成的 $V(\mathbb{R}^n)$ 的Lie子代数记作

$$\mathcal {C} = \{f (x), g (x) \} _ {L A},$$

它称为能控性 Lie 代数 [22].

如果 $f(x) = Ax, g(x) = b,$ 这里 $\pmb{A}$ 是一个 $n \times n$ 矩阵， $b \in \mathbb{R}^n$ 。那么系统退化为线性系统。简单的计算可得

$$
\begin{array}{l} [ f, g ] = - A b, \\ [ f, [ f, g ] ] = A ^ {2} b, \\ [ f, \dots , [ f, g ] \dots ] = (- 1) ^ {k} A ^ {k} b. \\ \end{array}
$$

■
+

注意，上述的多重 Lie 括号中如果包括多于一个的 $b$ ，则其结果必为零向量。所以要得到非零向量则 $b$ 只能出现一次。于是能控性 Lie 代数变为

$$\mathcal {C} = \operatorname{span} \{b, A b, \dots , A ^ {n - 1} b \}.$$

由线性系统理论可知 [17], 线性系统能控, 当且仅当 $\operatorname{rank}(\mathcal{C}) = n$ .

命题3.6.5 设 $X, Y \in V(M), p, q \in C^r(M)$ . 那么

$$[ p X, q Y ] = p q [ X, Y ] + p X (q) Y - q Y (p) X. \tag {3.6.15}$$

证明 对任一 $h \in C^r(M)$ ,

$$
\begin{array}{l} [ p X, q Y ] h = p X (q Y (h)) - q Y (p X (h)) (3.6.16) \\ = p X (q) Y (h) + p q X (Y (h)) - q Y (p) X (h) - q p Y (X (h)) (3.6.17) \\ = p q [ X, Y ] (h) - p X (q) Y (h) - q Y (p) X (h) (3.6.18) \\ = (p q [ X, Y ] - p X (q) Y - q Y (p) X) (h). (3.6.19) \\ \end{array}
$$

因为 h 是任意的，结论显见.
