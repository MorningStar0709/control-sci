$$
\begin{array}{l} (\mu I - T) ^ {- 1} y (x) = \int_ {\partial G _ {2}} f (\lambda) (\mu I - T) ^ {- 1} (\lambda I - T) ^ {- 1} x d \lambda \\ = \int_ {\partial G _ {2}} \frac {f (\lambda)}{\mu - \lambda} (\lambda I - T) ^ {- 1} x d \lambda - \int_ {\partial G _ {2}} \frac {f (\lambda)}{\mu - \lambda} (\mu I - T) ^ {- 1} x d \lambda \\ = \int_ {\partial G _ {2}} \frac {f (\lambda)}{\mu - \lambda} (\lambda I - T) ^ {- 1} x d \lambda , \quad \forall \mu \notin G _ {2}. \\ \end{array}
$$

但显然上式右端在 $G_{2}^{c}$ 上是解析的．因此 $y(x)\in X_0$

我们知道 $\lambda_0\in \sigma (T)$ 必定属于 $T$ 的近似点谱，故对于任给的 $\varepsilon >0,$ 存在 $x_{\varepsilon}\in X,$ $\| x_{\varepsilon}\| = 1$ ，使得 $\| (\lambda_0I - T)x_\varepsilon \| < \varepsilon .$ 注意豫解式 $(\lambda I - T)^{-1}$ 可以表示成

$$(\lambda I - T) ^ {- 1} x _ {\varepsilon} = \frac {1}{\lambda_ {0} - \lambda} (\lambda I - T) ^ {- 1} h _ {\varepsilon} + \frac {x _ {\varepsilon}}{\lambda - \lambda_ {0}},$$

其中 $h_{\varepsilon} = (\lambda_0I - T)x_{\varepsilon}$ . 因此

$$y (x _ {\varepsilon}) = \int_ {\partial G _ {2}} \frac {f (\lambda)}{\lambda_ {0} - \lambda} (\lambda I - T) ^ {- 1} h _ {\varepsilon} \mathrm{d} \lambda + 2 \pi \mathrm{i} f (\lambda_ {0}) x _ {\varepsilon}.$$

但 $f(\lambda_0) \neq 0$ , 并且上式中的积分当 $\varepsilon \to 0$ 时收敛于 0, 从而当 $\varepsilon$ 充分小时 $y(x_{\varepsilon}) \neq 0$ . 证毕.

根据线性算子的算子演算理论 (见文献 [4]), 对于 $X$ 中的有界线性算子 $T$ , 设 $\Gamma$ 是包围 $\sigma(T)$ 的封闭曲线, $\Gamma \subset \rho(A), f, g$ 是定义在 $\Gamma$ 所包围的闭区域上的两个连续复函数, 并且在该区域内部是解析的. 令

$$f (T) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} f (\lambda) R (\lambda ; T) \mathrm{d} \lambda ,g (T) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} g (\lambda) R (\lambda ; T) \mathrm{d} \lambda ,$$

则

$$f (T) g (T) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} f (\lambda) g (\lambda) R (\lambda ; T) \mathrm{d} \lambda . \tag {5.3.65}$$

定理5.3.28 设 $A$ 是Banach空间 $X$ 上 $C_0$ 等距半群 $T(t)$ 的生成算子，则 $\sigma(A) \cap \mathbb{R} \neq \varnothing$ .

证明 (1) 假定 $T(t)$ 不是群, 则必有 $\sigma(A) = \{\lambda \in \mathbb{C} \mid \operatorname{Re} \lambda \leqslant 0\}$ . 事实上, 从 $T(t)$ 的等距性可知当 $\operatorname{Re} \lambda \leqslant 0$ 时, $\mathcal{R}(\lambda I - A)$ 是一闭子空间. 如果存在 $\lambda \leqslant 0$ 使得 $\lambda \in \rho(A)$ , 则容易验证 $\mathbb{C}_{-} \subset \rho(A)$ , 其中

$$\mathbb {C} _ {-} = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda < 0 \right\},$$

此外， $\| R(\lambda; A) \| \leqslant |\operatorname{Re} \lambda|^{-1}, \forall \lambda \in \mathbb{C}_{-}$ . 因此 $A$ 生成群.
