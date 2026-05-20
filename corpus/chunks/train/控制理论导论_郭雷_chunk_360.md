# 习题 5.1

5.1.1 设 $\mathbb{R}^n$ 上定义两种范数

$$\| x \| _ {1} = | \xi_ {1} | + \dots + | \xi_ {n} |, \quad \forall x = (\xi_ {1}, \dots , \xi_ {n}) ^ {\mathrm{T}} \in \mathbb {R} ^ {n},\| x \| _ {\infty} = \max \left\{\left| \xi_ {k} \right| \mid 1 \leqslant k \leqslant n \right\}, \quad \forall x = (\xi_ {1}, \dots , \xi_ {n}) ^ {\mathrm{T}} \in \mathbb {R} ^ {n},$$

相应的 Banach 空间分别记作 $X_{1}$ 和 $X_{\infty}$ . 设 $T: R^{n} \rightarrow R^{n}$ 为一线性算子 (即线性变换), 在 $R^{n}$ 的标准规范直交基上其矩阵表示为 $A = \{a_{ij}\}$ , 即对于 $x = (\xi_{1}, \cdots, \xi_{n})^{T}$ , 有 $Tx = (\eta_{1}, \cdots, \eta_{n})^{T}$ , 其中 $\eta_{k} = a_{k1}\xi_{1} + \cdots + a_{kn}\xi_{n}$ . 试证.

(1) 若 $T: X_1 \to X_1$ , 则 $\|A\|_1 = \max\{a_{j1} + a_{j2} + \cdots + a_{jn}| 1 \leqslant j \leqslant n\}$ ;   
(2) 若 $T: X_1 \to X_\infty$ , 则 $\|A\|_{1,\infty} = \max \{|a_{jk}||1 \leqslant j, k \leqslant n\}$ ;  
(3) 若 $T: X_{\infty} \to X_{\infty}$ , 则 $\|A\|_{\infty} = \max \{a_{j1} + a_{j2} + \cdots + a_{jn} | 1 \leqslant k \leqslant n\}$ .

5.1.2 设 $X_{2} = R^{n}$ 上定义范数 $\|x\|_{2} = (\left|\xi_{1}\right|^{2} + \cdots + \left|\xi_{n}\right|^{2})^{1/2}$ ，而 $T: X_{2} \to X_{2}$ 为线性算子。试证，

(1) $T$ 的矩阵表示 $A$ 的范数与 $X_{2}$ 中基底的选择无关，并且 $\| T\| = \| A\|$   
(2) $\| T\| = \max \{\lambda_k(A^{\mathrm{T}}A)|1\leqslant k\leqslant n\}$ , 其中 $\lambda_{k}(M)$ 表示对称矩阵 $M$ 的从小到大排序的第 $k$ 个本征值.

5.1.3 设 $X$ 为 Banach 空间, $A \in \mathcal{L}(X), \lambda \in \mathbb{C}$ , 求证当 $|\lambda| > \| A\|$ 时, 算子 $A$ 的 Neuman 级数 $\sum_{k=0}^{\infty} A^{k} / \lambda^{k+1}$ 按算子范数收敛列 $(\lambda I - A)^{-1} \in \mathcal{L}(X)$ , 其中 $I$ 为 $X$ 中的恒等算子.

5.1.4 试证 $L^2 (-\pi ,\pi)$ 中的泛函序列

$$f _ {n} (\varphi) = \int_ {\pi} ^ {\pi} \varphi (t) \cos n t \mathrm{d} t, \quad \varphi \in L ^ {2} (- \pi , \pi)$$

弱收敛于零.

5.1.5 证明有穷维赋范空间必定是完备的.

5.1.6 证明闭区间 $[a, b]$ 上的连续函数空间 $C[a, b]$ 相对于范数 $\|f\| = \int_{a}^{b}|f(t)|\mathrm{d}t$ 来说是不完备的.

5.1.7 设 $X$ 是Banach空间. 序列 $\{x_{n}\} \subset X$ 满足

$$\sum_ {n = 1} ^ {\infty} \| x _ {n} \| = \mu < \infty .$$

试证级数 $\sum_{k=1}^{\infty} x_k$ 收敛，即存在 $x \in X$ 使得 $x = \lim_{n \to \infty} \sum_{k=1}^{n} x_k$ . 此外，有 $\|x\| \leqslant \mu$ .

5.1.8 设 $X$ 是赋范空间, $x_0 \in X$ 为任意非零元. 试证存在 $f \in X^*$ 使得 $\| f \| = 1$ , $f(x_0) = \| x_0 \|$ .

5.1.9 设 $\left\{x_{k} \mid 1 \leqslant k < \infty\right\}$ 为赋范空间 $X$ 中的任意线性无关序列，试证存在线性泛函序列 $\left\{f_{k} \mid 1 \leqslant k < \infty\right\} \subset X^{*}$ ，使得 $\| f_{k} \| = 1$ ，并且 $f_{j}(x_{k}) = \delta_{kj}$ .

5.1.10 定义线性算子 $A: C[0,1] \to C[0,1]$ 如下，
