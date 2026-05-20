上面所讨论的微分方程的右端函数 $f$ 并不包含与 $t$ 无关的独立变化的参数。人们可以从两方面提出问题：一是当初值改变时，相应的初值问题的解将发生怎样的变化？再一个是实际工程中一大类问题需要用包含有一个或几个参数的微分方程来描述。这类微分方程解的性态是否也将随参数的改变而发生“缓慢”或“急剧”的变化？下面将讨论的解对参数和初值的依赖关系属于解的性态发生“缓慢”变化的范畴。至于解的性态发生“急剧”变化如分岔、混沌等问题，这里不作讨论。

考察含有参数 $\mu$ 的微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = f (t, x; \mu), \tag {2.2.33}$$

其中 $x \in \mathbb{R}^n, t \in \mathbb{R}, \mu \in \mathbb{R}^l; f: \mathbb{R}^1 \times \mathbb{R}^n \times \mathbb{R}^l \to \mathbb{R}^n$ . 这里假定 $f(t, x; \mu), \frac{\partial f(t, x; \mu)}{\partial x}$ 在 $\mathbb{R}^1 \times \mathbb{R}^n \times \mathbb{R}^l$ 中的某区域 $\Omega_{n+l+1}$ 内有定义且连续.

定理 2.2.11 $^{[12]}$ 设 $f(t,x;\mu),\frac{\partial f(t,x;\mu)}{\partial x}$ 分别是定义在 $\Omega_{n+l+1}$ 内的连续向量值函数和矩阵值函数。对于 $\Omega_{n+l+1}$ 内任一固定点 $(t_{0},x_{0};\mu_{0})$ ，如果微分方程(2.2.33)以 $(t_{0},x_{0})$ 为初值的解 $\varphi(t;\mu_{0})$ 在包含 $t_{0}$ 为内点的某闭区间 $[t_{1},t_{2}]$ 上存在，则存在正数 $\sigma>0$ ，使得对于区域 $S_{\sigma}(\mu_{0})=\{\mu||\mu-\mu_{0}|\leqslant\sigma\}$ 内任一 $\mu$ ，方程(2.2.33)的满足初始条件

$$\varphi (t _ {0}; \mu) = x _ {0} \tag {2.2.34}$$

的解 $\varphi(t; \mu)$ 也在区间 $[r_1, r_2]$ 上存在，并且 $\varphi(t; \mu)$ 在 $[r_1, r_2] \times S_{\sigma}(\mu_0)$ 上是连续的.

定理 2.2.12 $^{[12]}$ 假设微分方程 (2.2.33) 的右端函数 $f(t, x; \mu)$ 及其对 x 和对 $\mu$ 的偏导数

$$\frac {\partial f (t , x ; \mu)}{\partial x}, \quad \frac {\partial f (t , x ; \mu)}{\partial \mu}$$

分别是在关于 $\mu$ 为凸的区域 $\Omega_{n + l + 1}$ 内定义的连续向量值函数和矩阵值函数. 设 $(t_0, x_0, \mu_0)$ 为 $\Omega_{n + l + 1}$ 内任一固定点. 如果微分方程 (2.2.33) 以 $(t_0, x_0)$ 为初值的解 $\varphi(t; \mu_0)$ 在闭区间 $[r_1, r_2]$ 上存在, 则

(1) 存在正数 $\sigma > 0$ , 使得当 $|\mu - \mu_0| \leqslant \sigma$ 时, 微分方程 (2.2.33) 的以 $(t_0, x_0)$ 为初值的解 $\varphi(t; \mu)$ 有关于 $\mu$ 的连续偏导数 $\frac{\partial \varphi(t; \mu)}{\partial \mu}$ ;

(2) 混合导数 $\frac{\partial^2\varphi(t;\mu)}{\partial t\partial\mu}$ 也是连续的；

(3) $\frac{\partial\varphi(t;\mu)}{\partial\mu}$ 满足下列线性非齐次矩阵微分方程

$$Z (t) = \frac {\partial f (t , \varphi (t ; \mu) ; \mu)}{\partial x} Z (t) + \frac {\partial f (t , \varphi (t ; \mu) ; \mu)}{\partial \mu} \tag {2.2.35}$$

和初始条件

$$Z (t _ {0}) = 0.$$

从原则上讲，有了微分方程解对参数的连续性和可微性定理后，其解对初始值的连续性和可微性关系问题容易解答，因为初始值也可以看作为参数。但是为了便于理解和引用，我们仍将简述之。下面为了明显看清解对初始值的关系，我们把微分方程(2.2.19)的以 $(t_0, x_0)$ 为初值的解记为 $\varphi(t; t_0, x_0)$ ，这里 $(t_0, x_0)$ 是 $f(t, x)$ 的定义区域内的任一固定点。
