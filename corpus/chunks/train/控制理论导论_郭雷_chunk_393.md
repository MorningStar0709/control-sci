今证式 (5.3.43) 中的积分当 $t > 2 / b$ 时是有意义的。为此只需对 $S_{1}(t)$ 和 $S_{3}(t)$ 进行证明。现在我们估计 $S_{1}(t)$ 和 $S_{3}(t)$ 中的被积函数。当 $\lambda = \sigma + \mathrm{i}\tau \in \Gamma_{j}, j = 1,3$ 时，我们有

$$\left\| \mathrm{e} ^ {\lambda t} R (\lambda ; A) \right\| = \left| \mathrm{e} ^ {\lambda t} \right| \| R (\lambda ; A) \| \leqslant C \mathrm{e} ^ {2 a t} | \tau | ^ {1 - b t}.$$

因此，

$$\| S _ {j} (t) \| \leqslant C \mathrm{e} ^ {2 a t} \left(1 + \frac {b}{L}\right) \int_ {L} ^ {\infty} | \tau | ^ {1 - b t} \mathrm{d} \tau , \quad j = 1, 3.$$

这表明当 $t > 2 / b$ 时积分是收敛的.

类似地可以证明积分

$$S ^ {\prime} (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \lambda \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda ,$$

当 $t > 3 / b$ 时在 $\mathcal{L}(X)$ 中是收敛的。于是 $S(t)$ 当 $t > 2 / b$ 时存在并且当 $t > 3 / b$ 时可微。

剩下证明 $T(t) = S(t)$ . 对于 $x \in \mathcal{D}(A^2)$ , 我们有

$$T (t) x = \lim _ {| \tau | \rightarrow \infty} \frac {1}{2 \pi \mathrm{i}} \int_ {\gamma + \mathrm{i} \tau} ^ {\gamma - \mathrm{i} \tau} \mathrm{e} ^ {\lambda t} R (\lambda ; A) x \mathrm{d} \lambda , \tag {5.3.44}$$

这里 $\gamma > \max \{0, \omega\}$ . 上述结论的证明可以在文献 [32] 中找到. 注意当 $x \in \mathcal{D}(A^2)$ 时, 有

$$R (\lambda ; A) x = \frac {x}{\lambda} + \frac {A x}{\lambda^ {2}} + \frac {R (\lambda ; A) A ^ {2} x}{\lambda^ {2}}. \tag {5.3.45}$$

于是从式 (5.3.41) 可得，对于任意 $x \in X$ 和 $t > 2 / b,$

$$S (t) x = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \mathrm{e} ^ {\lambda t} R (\lambda ; A) x \mathrm{d} \lambda . \tag {5.3.46}$$

在式 (5.3.46) 中取 $x \in \mathcal{D}(A^2)$ . 从式 (5.3.42) 和式 (5.3.45) 可见, 我们可以把式 (5.3.46) 中的积分路径从 $\Gamma$ 移到直线 $\gamma + \mathrm{i}\tau, -\infty < \tau < \infty$ . 因此 $T(t)x = S(t)x, \forall x \in \mathcal{D}(A^2), t > 2 / b$ . 但是, 当 $t > 2 / b$ 时 $S(t)$ 和 $T(t)$ 都是有界算子, 并且 $\mathcal{D}(A^2)$ 在 $X$ 中稠, 从而当 $t > 2 / b$ 时 $S(t) = T(t)$ . 证毕.

例5.3.12 Hilbert空间 $H$ 上任意紧自伴 $C_0$ 半群 $T(t)$ 都是可微的.

实际上，从定理5.3.18的证明可知，如果 $C_0$ 半群 $T(t)$ 满足式(5.3.41）和式(5.3.42)，则 $T(t)$ 对于 $t > t_0 = 3 / b$ 是可微的。因此当 $t_1 > t_0$ 时，式(5.3.41）中的常数 $b$ 可以选择为 $b = 1 / t_{1}$ 。在目前情形下，设 $A$ 是 $T(t)$ 的生成算子。考虑到 $A$ 的自伴性，式(5.3.41）实际上对于任意 $b > 0$ 成立，即

$$\rho (A) \supset \Sigma_ {b} = \left\{\lambda \mid \operatorname{Re} \lambda > - b \log | \operatorname{Im} \lambda | \right\}.$$

此外，对于任意自伴算子 $\pmb{A}$ ，我们有

$$\| R (\lambda ; A) \| \leqslant 1 / \operatorname{Im} \lambda |, \quad \forall \lambda \in \mathbb {C}, \operatorname{Im} \lambda \neq 0,\left| \operatorname{Im} \lambda \right| \geqslant \mathrm{e} ^ {- \omega / b}, \quad \forall \lambda \in \Sigma_ {b}, \operatorname{Re} \lambda \leqslant \omega ,$$

从而

$$\| R (\lambda ; A) \| \leqslant 1 / | \operatorname{Im} \lambda | \leqslant \mathrm{e} ^ {2 \omega / b} | \operatorname{Im} \lambda |, \quad \forall \in \Gamma_ {b}, \operatorname{Re} \lambda \leqslant \omega ,$$

即式 (5.3.42) 成立。因此由于 $b > 0$ 的任意性，从式 (5.3.41) 可知 $T(t)$ 是可微半群。
