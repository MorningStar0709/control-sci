# 习题 5.2

5.2.1 设 $X, Y$ 为 Banach 空间， $A \in \mathcal{L}(X, Y)$ . 试证：

(1) 若 $A$ 为紧算子，则 $A$ 把 $X$ 中的弱收敛序列变成 $Y$ 中的强收敛序列；  
(2) 当 $X$ 为自反时，(1) 的逆命题也成立，这就是说，若 $A$ 把 $X$ 中的弱收敛序列变成 $Y$ 中的强收敛序列，则 $A$ 是紧算子.

5.2.2 设 $X, Y$ 为 Banach 空间， $A_{n} \in \mathcal{K}(X, Y), \forall n \geqslant 1$ . 假定存在 $A \in \mathcal{L}(X, Y)$ ，使得 $\lim_{n \to \infty} \| A_{n} - A \| = 0$ ，则 $A$ 也是紧算子.  
5.2.3 设 $X$ 是 Banach 空间, $T$ 是 $X$ 中的紧线性算子. 试证对于任意复数 $\lambda \neq 0$ , 算子 $T - \lambda I$ 的值域 $\mathcal{R}(T - \lambda I)$ 是 $X$ 的闭子空间.  
5.2.4 设 Hilbert 空间 $\ell^2 = \left\{x = (\xi_k) \left| \|x\|^2 = \sum_{k=1}^{\infty} |\xi_k|^2 < \infty\right.\right\}$ . 试证 $\ell^2$ 中任意紧线性算子 $A$ 均可表示成 $A = A_1 + A_2$ , 其中 $A_1$ 为有穷秩算子, 即 $\dim \mathcal{R}(A_1) < \infty$ , 而 $\|A_2\| < 1$ .  
5.2.5 在 $\ell^{2}$ 中定义线性算子 A: $Ax = (\alpha_{1}\xi_{1}, \cdots, \alpha_{k}\xi_{k}, \cdots)$ , $\forall x = (\xi_{k}) \in \ell^{2}$ , 其中 $\alpha_{k}$ 为已知常数. 试指出对于什么样的 $\alpha_{k}$ , A 是有界的, 或是紧的.  
5.2.6 试证明赋范线性空间 $X$ 中的任意有穷秩有界线性算子 $A$ 可以表示成形式

$$A x = \sum_ {k = 1} ^ {n} f _ {k} (x) e _ {k}, \quad \forall x \in X,$$

其中 $e_{k} \in X, f_{k} \in X^{*}$ ，并且 $e_{1}, e_{2}, \cdots, e_{n}$ 是线性无关的.

5.2.7 设 $A$ 是 Banach 空间 $X$ 中的紧线性算子. 试证存在一单位元 $x \in X$ , 使得 $\|Ax\| = \|A\|$ .

5.2.8 设 $T$ 是 Hilbert 空间 $H$ 中的有界线性算子，已知 $TT^{*}$ 为紧算子，求证 $T$ 也是紧算子.

5.2.9 在 Hilbert 空间 $L^2(0,1)$ 中定义线性算子 $A$ ,

$$(A f) (t) = \int_ {0} ^ {t} f (s) \mathrm{d} s, \quad \forall f \in L ^ {2} (0, 1).$$

试找出 $A$ 的谱 $\sigma(A)$ , 点谱 $\sigma_p(A)$ , 连续谱 $\sigma_c(A)$ 和剩余谱 $\sigma_r(A)$ , 并证明 $\|A\| = 2/\pi$ .

5.2.10 设 $H$ 为 Hilbert 空间, $A$ 为 $H$ 中一线性算子. 对于 $\lambda \in \mathbb{C}$ , 如果有序列 $(x_{n}) \subset \mathcal{D}(A)$ , 使得 $\| x_{n} \| = 1$ , 并且 $\lim_{n \to \infty} (\lambda x_{n} - Ax_{n}) = 0$ , 则通常称 $\lambda$ 为 $A$ 的近似本征值. 试证自伴线性算子 $A$ 的谱全部由近似本征值组成.
