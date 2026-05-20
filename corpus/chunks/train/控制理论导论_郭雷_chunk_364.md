$$\gamma [ A ] \leqslant \| A \|, \tag {5.2.9}\gamma [ A B ] \leqslant \gamma [ A ] \gamma [ B ], \tag {5.2.10}\gamma [ A + B ] \leqslant \gamma [ A ] + \gamma [ B ], \tag {5.2.11}\gamma [ A ] = 0 \Longleftrightarrow A \text {是紧算子.} \tag {5.2.12}$$

类似于式 (5.2.7), 我们有

$$r _ {e} (A) = \lim _ {n \rightarrow \infty} (\gamma [ A ^ {n} ]) ^ {1 / n}. \tag {5.2.13}$$

式 (5.2.13) 的证明见文献 [10].

定理5.2.3 设 $A$ 是Banach空间 $X$ 中一闭线性算子，并设 $\mu \in \sigma(A) \backslash \sigma_e(A)$ . 那么 $N_{\mu}(A) = \mathcal{R}(A_{-1})$ . 其中 $A_{-1}$ 定义见式(5.2.5)， $\mu$ 是 $R(\lambda; A)$ 的极点，并且 $\mu \in \sigma_p(A)$ .

证明 根据定理5.2.2, 由于 $N_{\mu}(A)$ 是有穷维的, 并且 $\mu$ 是 $\sigma(A)$ 中的孤立点, 故只需证明 $N_{\mu}(A) = \mathcal{R}(A_{-1})$ . 但从 $N_{\mu}(A)$ 的有穷维性可知 $\mu$ 有有穷指标 $m$ , 从而 $N_{\mu}(A) = \mathcal{N}((\mu I - A)^m)$ .

我们首先用归纳法证明 $N_{\mu}(A) \subset \mathcal{R}(A_{-1})$ 。假定对于 $1 \leqslant k \leqslant m$ ， $\mathcal{N}((\mu I - A)^{k-1}) \subset \mathcal{R}(A_{-1})$ 。设 $x \in \mathcal{N}((\mu I - A)^k)$ ，并令 $y_0 \stackrel{\text{def}}{=} (\mu I - A)x$ 。由于 $(\mu I - A)^{k-1} y_0 = 0$ ，依归纳假设有 $y_0 \in \mathcal{R}(A_{-1})$ 。设 $\lambda \in \Gamma$ ，其中 $\Gamma$ 与式 (5.2.5) 中的一样。我们把 $y_0$ 写成

$$y _ {0} = \mu I x - A x = (\mu - \lambda) x + (\lambda I - A) x.$$

于是

$$R (\lambda ; A) x = (\mu - \lambda) ^ {- 1} R (\lambda ; A) y _ {0} - (\mu - \lambda) ^ {- 1} x.$$

由于 $y_0 \in \mathcal{R}(A_{-1})$ , 故存在某个 $x_0 \in X$ , 使得 $y_0 = A_{-1}x_0$ , 从而

$$R (\lambda ; A) y _ {0} = R (\lambda ; A) A _ {- 1} x _ {0} = A _ {- 1} R (\lambda ; A) x _ {0} \in \mathcal {R} (A _ {- 1}).$$

因此

$$A _ {- 1} x = \frac {1}{2 \pi \mathrm{i}} \left[ \int_ {\Gamma} (\mu - \lambda) ^ {- 1} R (\lambda ; A) y _ {0} \mathrm{d} \lambda - \int_ {\Gamma} (\mu - \lambda) ^ {- 1} x \mathrm{d} \lambda \right],$$

这表明

$$x = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} (\lambda - \mu) ^ {- 1} R (\lambda ; A) y _ {0} \mathrm{d} \lambda + A _ {- 1} x.$$

由于 $A_{-1}$ 是 $X$ 中的投影，故 $\mathcal{R}(A_{-1})$ 是闭的。但对所有 $\lambda \in \Gamma, R(\lambda; A)y_0 \in \mathcal{R}(A_{-1})$ 从而 $x \in \mathcal{R}(A_{-1})$ 。于是 $\mathcal{N}((\mu I - A)^k) \subset \mathcal{R}(A_{-1})$ 。根据归纳法，我们得证 $\mathcal{N}((\mu I - A)^m) = N_\mu(A) \subset \mathcal{R}(A_{-1})$ 。
