# 5.2 线性算子谱理论

本节中 $X$ 总是表示复域 $\mathbb{C}$ 上的 Banach 空间。设 $A$ 是定义域和值域都在 $X$ 中的一闭线性算子。我们将考虑形式 $(\lambda I - A)$ 的算子，其中 $\lambda$ 为一标量， $I$ 为 $X$ 上的恒等算子。

$A$ 的豫解集 $\rho(A)$ 定义为复平面 $\mathbb{C}$ 中的集合

1 Ⅲ 2. A = 2. E, K(λ) = A, 三天分部(λ) 真有界逆}.

$\sum \in \rho(A)$ , 算子 $R(\lambda; \overline{A}) = (\lambda I - A)^{-1}$ 叫做 $\overline{A}$ 的像解式, 我们有如下的像解

$$R (\lambda ; \mathcal {A}) - R (\mu ; \mathcal {A}) = (\mu - \lambda) R (\lambda ; \mathcal {A}) R (\mu ; A), \quad \forall \lambda , \mu \in \rho (\mathcal {A}). \tag {5.2-1}$$

如果 $\mu \in \rho(A)$ 和 $|\mu - \lambda| \| R(\mu: A) \| < 1$ , 则 $\lambda \in \rho(A)$ , 并且

$$R (\lambda ; A) = \sum_ {n = 0} ^ {\infty} (\mu - \lambda) ^ {n} R ^ {n + 1} (\mu ; A), \tag {5.2.2}$$

其中级数按一致算子拓扑收敛．特别地， $R(\lambda ;A)$ 作为 $\rho (A)$ 到 $\mathcal{L}(X)$ 的函数无穷次可微，其 $n$ 阶导数是

$$\frac {\mathrm{d} ^ {n}}{\mathrm{d} \lambda^ {n}} R (\lambda ; A) = (- 1) ^ {n} n! R ^ {n + 1} (\lambda ; A). \tag {5.2.3}$$

A 的谱是指集合 $\sigma(A) \stackrel{\mathrm{def}}{=} \mathbb{C} \backslash \rho(A)$ . 谱 $\sigma(A)$ 被分解成三个互不相交的部分:

$\sigma_{p}(A) = \{\lambda \in \mathbb{C} | (\lambda I - A)$ 不是一对一的};

$\sigma_{c}(A) = \{\lambda \in \mathbb{C} \mid (\lambda I - A)$ 一对一， $\overline{\mathcal{R}(\lambda I - A)} = X$ ，但 $(\lambda I - A)^{-1}$ 无界；

$\sigma_r(A) = \{\lambda \in \mathbb{C} \mid (\lambda I - A)$ 是一对一的, 但 $\overline{\mathcal{R}(\lambda I - A)} \neq X\}$ .

$\sigma_{p}(A), \sigma_{c}(A)$ 和 $\sigma_{r}(A)$ 分别叫做 $A$ 的点谱，连续谱和剩余谱。对于每个 $\lambda \in \sigma_{p}(A)$ ，至少存在一非零向量 $x \in \mathcal{D}(A)$ 使得 $Ax = \lambda x, \lambda$ 也叫做 $A$ 的本征值， $x$ 则叫做 $A$ 的对应于 $\lambda$ 的本征向量或本征元。零空间 $\mathcal{N}(\lambda I - A)$ 叫做 $A$ 的对应于 $\lambda$ 的几何本征子空间，而其维数 $\dim \mathcal{N}(\lambda I - A)$ 则叫做 $\lambda$ 的几何重数。类似地，对于 $\lambda \in \sigma_{p}(A), A$ 的对应于 $\lambda$ 的广义本征子空间 $N_{\lambda}(A)$ 是 $X$ 中包含 $\bigcup_{n=1}^{\infty} \mathcal{N}((\lambda I - A)^{n})$ 的最小闭子空间，其维数叫做 $\lambda$ 的代数重数。如果 $\lambda \in \sigma_{p}(A)$ 并且存在一正整数 $k$ 使得 $\mathcal{N}((\lambda I - A)^{k}) = \mathcal{N}((\lambda I - A)^{k+j}), j = 1,2,\cdots$ ，那么 $\lambda$ 叫做具有有穷指标，使得上式成立的最小的这样的整数 $k$ 叫做 $\lambda$ 的指标。

设 $P \in \mathcal{L}(X)$ , $P$ 叫做 $X$ 中的投影算子, 是指它满足 $P^2 = P$ .

定理5.2.1 设 $P$ 是 $X$ 中的投影算子，则 $I - P$ 也是 $X$ 中的投影，并且 $X$ 可以分解成直接和： $X = X_{1} + X_{2}$ ，其中 $X_{1} = PX, X_{2} = (I - P)X, X_{1}, X_{2}$ 是 $X$ 的闭子空间。反之，若 $X = X_{1} + X_{2}$ 是两个闭子空间 $X_{1}$ 和 $X_{2}$ 的直和分解，则 $P_{1}, P_{2}$ 是 $X$ 中的投影，其中 $P_{j}x = x_{j}, x = x_{1} + x_{2}, x_{j} \in X_{j}, j = 1, 2$ .
