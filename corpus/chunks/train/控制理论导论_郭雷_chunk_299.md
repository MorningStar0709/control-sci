证明 (1) 设 $f_{k}(\lambda)$ 为 $X_{k} - EX_{k}$ 的特征函数，那么 $\frac{X_j - EX_j}{n}$ 的特征函数为 $f_{j}\left(\frac{\lambda}{n}\right)$ . 注意到

$$\max _ {1 \leqslant j \leqslant n} \frac {E | x _ {j} - E X _ {j} | ^ {1 + \delta}}{n ^ {1 + \delta}} \leqslant \frac {1}{n ^ {1 + \delta}} \sum_ {j = 1} ^ {n} E | X _ {j} - E X _ {j} | ^ {1 + \delta} \underset {n \rightarrow \infty} {\longrightarrow} 0.$$

根据特征函数的性质 $4(\delta > 0)$ , 对任一固定的 $\lambda$ . 对 $j \leqslant n$ 一致地有

$$f _ {j} \left(\frac {\lambda}{n}\right) = 1 + \frac {2 ^ {1 - \delta}}{1 + \delta} \theta_ {n j} \frac {E | X _ {j} - E X _ {j} | ^ {1 + \delta}}{n ^ {1 + \delta}} \cdot | \lambda | ^ {1 + \delta} \underset {n \rightarrow \infty} {\longrightarrow} 1,$$

这里 $|\theta_{nj}| \in (0,1]$ . 所以只要 $n$ 充分大，存在 $\theta_n \in (0,1]$ 使

$$\sum_ {j = 1} ^ {n} \log f _ {j} \left(\frac {\lambda}{n}\right) = 2 \theta_ {n} | \lambda | ^ {1 + \delta} \frac {1}{n ^ {1 + \delta}} \sum_ {j = 1} ^ {n} E | X _ {j} - E X _ {j} | ^ {1 + \delta} \underset {n \rightarrow \infty} {\longrightarrow} 0,$$

即 $\prod_{j=1}^{n} f_j \left( \frac{\lambda}{n} \right) \underset{n \to \infty}{\longrightarrow} 1$ ，或 $\frac{1}{n} \sum_{j=1}^{n} (X_j - EX_j)$ 的分布函数趋于在 0 点退化的分布函数.

(2) 记 $\sigma_{j}^{2} = E(X_{j} - EX_{j})^{2}$ . 从定理的条件及 Lyapunov 不等式知

$$\max _ {j \leqslant n} \left(\frac {\sigma_ {j}}{s _ {n}}\right) ^ {2 + \delta} \leqslant \max _ {j \leqslant n} \frac {E | X _ {j} - E X _ {j} | ^ {2 + \delta}}{s _ {n} ^ {2 + \delta}} \leqslant \frac {1}{s _ {n} ^ {2 + \delta}} \sum_ {j = 1} ^ {n} E | X _ {j} - E X _ {j} | ^ {2 + \delta} \rightarrow 0.$$

所以对任一固定的 $\lambda_{j}$ 对 $j\leqslant n$ 一致地有

$$f _ {j} \left(\frac {\lambda}{s _ {n}}\right) = 1 - \frac {\lambda^ {2}}{2} \frac {\sigma_ {j} ^ {2}}{s _ {n} ^ {2}} + \frac {2 ^ {1 - \delta}}{(1 + \delta) (2 + \delta)} \theta_ {n k} | \lambda | ^ {2 + \delta} \frac {E | X _ {j} - E X _ {j} | ^ {2 + \delta}}{s _ {n} ^ {2 + \delta}} \rightarrow 1, \quad | \theta_ {n k} | \leqslant 1.$$

所以对充分大的 $n$

$$\sum_ {j = 1} ^ {n} \log f _ {j} \left(\frac {\lambda}{s _ {n}}\right) = - \frac {\lambda^ {2}}{2} (1 + o (1)) + 2 \theta_ {n} | \lambda | ^ {2 + \delta} \frac {1}{s _ {n} ^ {2 + \delta}} \sum_ {j = 1} ^ {n} E | X _ {j} - E X _ {j} | ^ {2 + \delta}, \quad | \theta_ {n} | \leqslant 1.$$

当 $n \to \infty$ 时，上式右端趋于 $-\frac{\lambda^2}{2}$ ，即 $\prod_{j=1}^{n} f_j \left( \frac{\lambda}{s_n} \right) \to e^{-\frac{\lambda^2}{2}}$ .
