# 习题 4.2

4.2.1 设 $\{X_{n}\}$ 为 iid 随机变量列， $E|X_1| > 0, S_n = \sum_{i=1}^{n} X_i$ 。如果 $\frac{S_n}{n} \xrightarrow{P} 0$ ，证明 $\inf\{n \geqslant 1: S_n \geqslant 0\} < \infty$ a.s., $\inf\{n \geqslant 1: S_n < 0\} < \infty$ ，且

$$P \{\lim _ {n} \sup S _ {n} = \infty \} = 1 = P \{\lim _ {n \to \infty} \inf S _ {n} = - \infty \}.$$

4.2.2 设 $\{X_{n}\}$ 为 iid 并对某个 $p \in (0, \infty)$ , $E|X_{1}|^{p} = \infty$ , 证明 $P\{\limsup_{n \to \infty} |S_{n}| / n^{\frac{1}{p}} = \infty\} = 1$ , 这里 $S_{n} = \sum_{i=1}^{n} X_{i}$ .

4.2.3 设 $\{X_{n}\}$ 相互独立, $P\{x_{n} = 1\} = P(x_{n} = -1) = 1 / 2$ . 证明对任意 $p > 2$ , $\sum_{n=1}^{\infty} E|X_{n} / \sqrt{n}|^{p} < \infty$ , 但 $\sum_{n=1}^{\infty} X_{n} / \sqrt{n}$ a.s. 发散.

4.2.4 设 $\{X_{n}\}$ 为 iid. 证明对任一 $\alpha \in \left(0, \frac{1}{2}\right]$ , 必成立下列 i), ii), iii) 三者之一,

i) $S_{n} / n^{\alpha}\rightarrow \infty$ a.s.; ii) $S_{n} / n^{\alpha}\rightarrow -\infty$ a.s.; iii) $\limsup_{n\to \infty}S_n / n^\alpha = \liminf_{n\to \infty}S_n / n^\alpha =$ $-\infty ,$ 这里 $S_{n} = \sum_{i = 1}^{n}X_{i}$

4.2.5 设 $\{X_{n}\}$ 为 iid, $S_{n} = \sum_{i=1}^{n} X_{i}, \{\mathcal{F}_{n}\}$ 为 $\sigma$ -代数族, $\mathcal{F}_{n} \uparrow, \mathcal{F}_{n}$ 和 $X_{n+1}$ 独立. 如果 $EX_{1}$ 存在, $\tau$ 是对 $\{\mathcal{F}_{n}\}$ 的停时, $E\tau < \infty$ , 证明 $ES_{\tau} = EX_{1} \cdot E\tau$ .

4.2.6 设 $\{X_{n}\}$ 为 iid, $S_{n} = \sum_{i=1}^{n} X_{i}$ , 证明能找到常数列 $c_{n}$ 使 $\frac{(S_{n} - c_{n})}{n} \to 0$ a.s. 的充要条件是 $E|X_{1}| < \infty$ .

4.2.7 设 $\{X_{n}\}$ 为 iid, $E|X_1| > 0$ , 证明 $\limsup_{n\to \infty}\frac{1}{n^{1 / 2}}\left|\sum_{i = 1}^{n}X_i\right| = \infty$ a.s.

4.2.8 设 $\{X_{n}\}$ 为 iid, 在 $[0,1]$ 上均匀分布, 记 $T = \inf \left\{n > 1 : \sum_{i=1}^{n} X_{i} \geqslant 1\right\}$ , 证明 $ET = e = 2ES_{T}$ .

4.2.9 设 $\{X_{n}\}$ 为 iid, 证明 $E\sup_{n}\left|\frac{X_n}{n}\right| < \infty$ 的充要条件是 $E|X_1|\log^+ |X_1| < \infty$ .

4.2.10 设 $\{X_{n}\}$ 为 iid, $EX_{1} = 1$ , $\{a_{n}\}$ 为实数列, 证明 $\frac{1}{n} \sum_{j=1}^{n} a_{j} \to 1$ 的充要条件是 $\frac{1}{n} \sum_{j=1}^{n} a_{j} X_{j} \to 1$ a.s.

4.2.11 设 $\{X_{n}\}$ 相互独立， $EX_{n} = 0, EX_{n}^{2} = \sigma_{n}^{2}, s_{n}^{2} \stackrel{\mathrm{def}}{=} \sum_{i=1}^{n} \sigma_{i}^{2} \to \infty$ 。证明对 $\alpha > \frac{1}{2}$ ， $s_{n}^{-1} (\log s_{n}^{2})^{-\alpha} \sum_{i=1}^{n} X_{i} \to 0$ a.s.

4.2.12 对任一随机变量列 $\{X_{n}\}$ , 证明必可找到常数列 $a_{n}, 0 < a_{n} \uparrow \infty$ 使 $X_{n} / a_{n} \xrightarrow[n \to \infty]{\longrightarrow}$ 0 a.s.
