定理5.1.4 设 $X$ 为一赋范线性空间，则对于每一 $x_0 \in X$ ，存在 $f \in X^*$ 使得

$$f (x _ {0}) = \| x _ {0} \|, \quad \| f \| = 1.$$

定理5.1.5 设 $X$ 是一赋范线性空间， $X_0$ 是 $X$ 的一真闭子空间，则对于任意 $x_0 \in X \setminus X_0$ ，存在一泛函 $f \in X^*$ 使得 $f(x) = 0, \forall x \in X_0$ ，并且 $f(x_0) = 1$ .

$X$ 的对偶空间 $X^{*}$ 作为一个Banach空间,也有其自身的对偶空间 $X^{**} = (X^{*})^{*}$ ,叫做 $X$ 的二次对偶空间.在自然嵌入下,我们可以写 $X \subset X^{**}$ .如果 $X = X^{**}$ ,则 $X$ 叫做自反的.

赋范线性空间 $X$ 中的序列 $\{x_{n}\}$ 叫做弱收敛于 $x_0\in X$ ，是指

$$\lim _ {n \rightarrow \infty} \langle x _ {n}, f \rangle = \langle x _ {0}, f \rangle , \quad \forall f \in X ^ {*}.$$

相应地，序列 $\{x_{n}\} \subset X$ 叫做强收敛于 $x_0$ ，是指它按范数收敛，即

$$\lim _ {n \rightarrow \infty} \| x _ {n} - x _ {0} \| = 0.$$

对偶空间 $X^{*}$ 中的序列 $\{f_n\}$ 叫做弱 $*$ 收敛于 $f_0 \in X^*$ , 是指

$$\lim _ {n \rightarrow \infty} \langle x, f _ {n} \rangle = \langle x, f _ {0} \rangle , \quad \forall x \in X.$$

今后我们将使用记号 $\stackrel{s}{\longrightarrow}$ 或 $s$ -lim 表示强收敛， $\stackrel{w}{\longrightarrow}$ 或 $w$ -lim 表示弱收敛，而 $\stackrel{w^{*}}{\longrightarrow}$ 或 $w^{*}$ -lim 表示弱 \* 收敛。有时候，为了记号简单起见，我们也会使用记号 $\rightarrow$ 表示强收敛，而 $\rightarrow$ 表示弱或弱 \* 收敛。

如果 $M, N$ 是线性空间 $X$ 的两个子空间，使得 $M \cap N = \{0\}$ ，我们定义一新的子空间 $M + N = \{x + y \mid x \in M, y \in N\}$ ，叫做 $M$ 和 $N$ 的直和。

设 $X$ 和 $Y$ 为两个赋范线性空间， $A$ 为 $X$ 到 $Y$ 的一线性算子，其定义域为 $X$ 中的线性子空间 $\mathcal{D}(A)$ ，而值域 $\mathcal{R}(A)$ 是指 $Y$ 中的集合

$$\mathcal {R} (A) = \left\{A x \mid x \in \mathcal {D} (A) \right\}.$$

如果 $D(A)$ 在 $X$ 中稠，则 $A$ 称为稠定的。 $A$ 的图像 $G(A)$ 是乘积空间 $X \times Y$ 中的集合

$$G (A) = \left\{\left[ x, A x \right] \in X \times Y \mid x \in \mathcal {D} (A) \right\}.$$

线性算子 $A$ 叫做闭的，是指其图像 $G(A)$ 是 $X \times Y$ 中一闭子空间。换句话说， $A$ 是闭的，是指 $x_{n} \in \mathcal{D}(A), n \geqslant 1$ 和 $x_{n} \to x, Ax_{n} \to y (n \to \infty)$ 推出 $x \in \mathcal{D}(A)$ ，并且 $Ax = y$ .

如果 $A$ 是 $X$ 到 $Y$ 的有界线性算子，定义域为 $\mathcal{D}(A) = X$ ，则我们定义 $A$ 的范数为

$$\| A \| = \sup \left\{\| A x \| \mid x \in X, \| x \| = 1 \right\}.$$

$\mathcal{L}(X,Y)$ 表示 $X$ 到 $Y$ 的有界线性算子全体按上述范数构成的赋范线性空间。如果 $Y$ 是Banach空间，则 $\mathcal{L}(X,Y)$ 也是Banach空间。为简单起见，当 $X = Y$ 时，我们将写 $\mathcal{L}(X) = \mathcal{L}(X,X)$ 。

序列 $\{A_n\} \subset \mathcal{L}(X,Y)$ 叫做一致或按一致算子拓扑收敛于 $A \in \mathcal{L}(X,Y)$ , 是指当 $n \to \infty$ 时 $\| A_n - A \| \to 0$ , 而 $\{A_n\} \subset \mathcal{L}(X,Y)$ 叫做强收敛于 $A \in \mathcal{L}(X,Y)$ , 是指当 $n \to \infty$ 时, 对所有 $x \in X$ 有 $A_n x \to Ax$ .

如果 $A$ 是 $X$ 中稠定有界线性算子，那么 $A$ 可以唯一地按连续性延拓成定义在整个 $X$ 上的一个有界线性算子，并且保持其范数不变.
