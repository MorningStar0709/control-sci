设 $f(t,x), \frac{\partial f(t,x)}{\partial x}$ 分别为 $\mathbb{R}^{n+1}$ 中某开域 $\Omega_{n+1}$ 内的连续向量值函数和连续矩阵值函数。现引入变量代换

$$
\left\{ \begin{array}{l} \tau = t - t _ {0}, \\ y = x - x _ {0}. \end{array} \right. \tag {2.2.36}
$$

在变量代换 (2.2.36) 下，微分方程 (2.2.19) 化为

$$\frac {\mathrm{d} y}{\mathrm{d} \tau} = f (\tau + t _ {0}, y + x _ {0}), \tag {2.2.37}$$

而微分方程 (2.2.19) 以 $(t_0, x_0)$ 为初值的解 $\varphi(t; t_0, x_0)$ 变换为微分方程 (2.2.37) 的以 $(0, 0)$ 为初值的解。容易看出函数

$$f (\tau + t _ {0}, y + x _ {0}), \quad \frac {\partial f (\tau + t _ {0} , y + x _ {0})}{\partial x}$$

对于那些使 $(\tau + t_0, y + x_0) \in \Omega_{n+1}$ 的 $(\tau, y)$ 有定义并连续. 因此向量微分方程 (2.2.37) 中包含 $n + 1$ 个参数 $t_0, x_{10}, x_{20}, \cdots, x_{n0}$ , 其右端也满足定理 2.2.12 的条件. 如果方程 (2.2.37) 的以 $(0,0)$ 为初值条件的解 $\psi(\tau; t_0, x_0)$ 在某闭区间 $\alpha_1 \leqslant \tau \leqslant \alpha_2$ 上有定义, 那么存在正数 $\sigma > 0$ , 使得当 $|\bar{t}_0 - t_0| < \sigma$ , $|\bar{x}_0 - x_0| < \sigma$ 时, 方程 (2.2.37) 以 $(0,0)$ 为初值的解 $\psi(\tau; \bar{t}_0, \bar{x}_0)$ 也在闭区间 $\alpha_1 \leqslant \tau \leqslant \alpha_2$ 上确定, 并且 $\psi(\tau; t_0, x_0)$ 是三变量 $(\tau; t_0, x_0)$ 的连续函数.

注意 $\psi (\tau ;t_0,x_0)$ 能够延拓到区间 $\alpha_{1} - \delta \leqslant \tau \leqslant \alpha_{2} + \delta$ 上，这里 $\delta$ 是某个适当小的正数．所以存在某个正数 $\sigma_{1}(\sigma_{1}\leqslant \sigma)$ 使得当 $|\bar{t}_0 - t_0| <   \sigma_1,|\bar{x}_0 - x_0| <   \sigma_1$ 时， $\psi (\tau ;\bar{t}_0,\bar{x}_0)$ 也在区间 $\alpha_{1} - \delta \leqslant \tau \leqslant \alpha_{2} + \delta$ 上有定义.

回到微分方程 (2.2.19), 如果它的以 $(t_0, x_0)$ 为初值的解 $x_0 + \psi(t - t_0; t_0, x_0)$ 本来是在区间 $\alpha_1 + t_0 \leqslant t \leqslant \alpha_2 + t_0$ 上有定义, 那么就可以延拓到闭区间 $\alpha_1 + t_0 - \delta \leqslant t \leqslant \alpha_2 + t_0 + \delta$ 上; 从而它以 $(\bar{t}_0, \bar{x}_0)$ 初值的解 $\bar{x}_0 + \psi(t - \bar{t}_0; \bar{t}_0, \bar{x}_0)$ 在区间 $\alpha_1 + \bar{t}_0 - \delta \leqslant t \leqslant \alpha_2 + \bar{t}_0 + \delta$ 上有定义, 即在区间 $t_0 + \alpha_1 - |\bar{t}_0 - t_0| \leqslant t \leqslant t_0 + \alpha_2 + |\bar{t}_0 - t_0|$ 上有定义. 由此推知, 当 $|\bar{t}_0 - t_0| \leqslant \min\{\delta, \sigma_1\}, |\bar{x}_0 - x_0| < \sigma_1$ 时, 微分方程 (2.2.19) 的解 $\bar{x}_0 + \psi(t - \bar{t}_0; \bar{t}_0, \bar{x}_0)$ 在闭区间 $\alpha_1 + t_0 \leqslant t \leqslant \alpha_2 + t_0$ 上有定义, 并且是 $(t; \bar{t}_0, \bar{x}_0)$ 的连续函数. 这样即得到微分方程 (2.2.19) 的解关于初值的连续依赖性的定理如下:
