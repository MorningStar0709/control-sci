# Riesz 基方法

如果 Hilbert 空间 $H$ 中某个 $C_0$ 半群 $T(t)$ 的生成算子 $A$ 的广义本征元全体构成 $H$ 的 Riesz 基，则该半群满足谱确定增长假设，从而其指数稳定性由算子 $A$ 的谱决定。Riesz 基方法的特点是它能提供比稳定性更多的信息，如解的 Fourier 展开，谱确定增长假设等。设 $\{e_n \mid n \geqslant 1\}$ 是 $H$ 的规范直交基。 $H$ 中的序列 $\{\varphi_n \mid n \geqslant 1\}$ 叫做 $H$ 的 Riesz 基，是指存在 $H$ 中的一有界可逆线性算子 $T$ ，使得 $\varphi_n = Te_n, \forall n \geqslant 1$ 。根据 Bari 定理（见文献 [15])，如果 $H$ 中 $\omega-$ 线性无关序列 $\{\psi_n \mid n \geqslant 1\}$ 满足

$$\sum_ {n = 1} ^ {\infty} \left\| \psi_ {n} - e _ {n} \right\| ^ {2} < \infty ,$$

则 $\{\psi_n \mid n \geqslant 1\}$ 是 $H$ 的 Riesz 基，这里线性空间中一子集称为 $\omega-$ 线性无关的，是指其任意有穷个向量均为线性无关的。本小节就是给出验证系统 Riesz 基性质的具体方法，从而达到研究系统指数稳定性的目的，详见文献 [17], [18], [19].

先给出一个引理.

引理10.4.3 设 $\{\varphi_n | n \geqslant 1\}$ 是 $H$ 的Riesz基. 设 $\{\psi_n | n > N_1\}$ 是 $H$ 中一 $\omega-$ 线性无关序列, $N_1$ 为一非负整数. 如果

$$\sum_ {n = N _ {1} + 1} ^ {\infty} \left\| \varphi_ {n} - \psi_ {n} \right\| ^ {2} < \infty , \tag {10.4.56}$$

则存在一自然数 $N \geqslant N_1$ 使得 $\{\varphi_n \mid 1 \leqslant n \leqslant N\} \cup \{\psi_n \mid n > N\}$ 是 $H$ 的一Riesz基.

证明 由于 $\{\varphi_n \mid n \geqslant 1\}$ 是 $H$ 的 Riesz 基, 故存在有界可逆线性算子 $T \in \mathcal{L}(H)$ 得 $T\varphi_n = e_n$ , 其中 $\{e_n \mid n \geqslant 1\}$ 为 $H$ 的直交规范基. 依据假设, 存在 $N \geqslant N_1$ 使得

$$\delta^ {2} \stackrel {\mathrm{def}} {=} \| T \| ^ {2} \sum_ {n = N + 1} ^ {\infty} \| \varphi_ {n} - \psi_ {n} \| ^ {2} < 1.$$

定义线性算子 $Q$

$$Q = \sum_ {n = 1} ^ {N} a _ {n} \varphi_ {n} + \sum_ {n = N + 1} ^ {\infty} a _ {n} \psi_ {n}, \quad \forall x = \sum_ {n = 1} ^ {\infty} a _ {n} \varphi_ {n} \in H.$$

于是对于任意 $x = \sum_{n=1}^{\infty} a_n \varphi_n \in H$ ,

$$
\begin{array}{l} \left\| (I - Q) x \right\| = \left\| \sum_ {n = N + 1} ^ {\infty} a _ {n} \left(\varphi_ {n} - \psi_ {n}\right) \right\| ^ {2} \leqslant \sum_ {n = N + 1} ^ {\infty} \left| a _ {n} \right| ^ {2} \sum_ {n = N + 1} ^ {\infty} \left\| \varphi_ {n} - \psi_ {n} \right\| ^ {2} \\ \leqslant \| T \| ^ {2} \sum_ {n = N + 1} ^ {\infty} \| \varphi_ {n} - \psi_ {n} \| ^ {2} \| x \| ^ {2} = \delta^ {2} \| x \| ^ {2}. \\ \end{array}
$$

这表明 $Q \in \mathcal{L}(H)$ , 并且 $\|I - Q\| \leqslant \delta < 1$ . 因此, $Q^{-1} \in \mathcal{L}(H)$ . 注意到 $Q\varphi_n = \varphi_n$ $\forall 1 \leqslant n \leqslant N$ 和 $Q\varphi_n = \psi_n \forall n > N$ , 从 Bari 定理可知引理结论成立. 证毕.

定理10.4.4 设 $A$ 是Hilbert空间 $H$ 中的稠定、离散（即具有紧豫解式的）线性算子，设 $\{\varphi_n | n \geqslant 1\}$ 是 $H$ 的Riesz基。如果存在非负整数 $N_1$ 和 $A$ 的一列广义本征元 $\{\psi_n | n > N_1\}$ ，使得
