$$
\begin{array}{l} \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \left\{\omega_ {k + 1} ^ {2} - E [ \omega_ {k + 1} ^ {2} | \mathcal {F} _ {k} ] \right\} \\ = O \left(S _ {n} \left(\frac {\alpha}{2}\right) \log^ {\frac {2}{\alpha} + \eta} \left(S _ {n} \left(\frac {\alpha}{2}\right) + e\right)\right) \quad \text { a.s. } \quad \forall \eta > 0, \\ \end{array}
$$

其中

$$S _ {n} \left(\frac {\alpha}{2}\right) \stackrel {\mathrm{dcf}} {=} \left\{\sum_ {k = 0} ^ {n} (a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k}) ^ {\frac {\alpha}{2}} \right\} ^ {\frac {2}{\alpha}}.$$

注意到 $a_{k}\phi_{k}^{\mathrm{T}}P_{k}\phi_{k}\leqslant 1$ 且 $2 / \alpha < 1$ ，利用式(9.2.16)有

$$S _ {n} \left(\frac {\alpha}{2}\right) = O (1) + o (\log | P _ {n + 1} ^ {- 1} |).$$

据此，从上式可得

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \omega_ {k + 1} ^ {2} \\ \leqslant \sigma_ {n} ^ {2} \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} + o (\log | P _ {n + 1} ^ {- 1} |) + O (1), \tag {9.2.17} \\ \end{array}
$$

其中

$$\sigma_ {n} \stackrel {\text { def }} {=} \max _ {k \leqslant n} E [ w _ {k + 1} ^ {2} | \mathcal {F} _ {k} ].$$

而根据条件(A1)知 $\{\sigma_{n}\}$ 是有界序列.

进一步，利用式(9.2.7)和式(9.2.9)可知

$$\log [ \det (P _ {t + 1} ^ {- 1}) ] \leqslant d \log \lambda_ {\max} (P _ {t + 1} ^ {- 1}) \leqslant d \log r _ {t} + O (1),$$

其中 $d \stackrel{\mathrm{def}}{=} \dim(\phi_k)$ .

于是，利用式(9.2.16)从式(9.2.17)可得

$$\sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} w _ {k + 1} ^ {2} = O (\log r _ {n}).$$

将此式与式 (9.2.15) 代入式 (9.2.14) 得

$$V _ {n + 1} + \sum_ {k = 0} ^ {n} a _ {k} (\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2} = O (\log r _ {n}).$$

因此定理的两个结论成立. 证毕.

利用上述定理的第一个结论 (i), 可直接得到如下推论:

推论9.2.1 在定理9.2.1的条件下，LS的估计误差 $\tilde{\theta}_t\stackrel {\mathrm{def}}{=} \theta -\theta_t$ 具有如下渐近上界：

$$\left\| \tilde {\theta} _ {t + 1} \right\| ^ {2} = O \left(\frac {\log r _ {t}}{\lambda_ {\min} (P _ {t + 1} ^ {- 1})}\right), \quad \text { a.s. } \tag {9.2.18}$$

其中 $\lambda_{\min}(\cdot)$ 表示矩阵的最小本征值.

我们看到，为了使LS估计具有强相容性，即当 $t \to \infty$ 时， $\theta_t \to \theta$ a.s.，只需随机回归向量序列 $\{\phi_k\}$ 满足如下条件即可：

$$\frac {\log r _ {t}}{\lambda_ {\min} \left(P _ {t + 1} ^ {- 1}\right)} \longrightarrow 0, \quad \text { a . s . } \tag {9.2.19}$$

这一基本结果是由黎和魏 $^{[31]}$ 首先得到的。他们还进一步举例说明了，在一定意义下，式(9.2.19)是LS估计强相容的最弱条件。尽管如此，在自适应系统分析中，如何验证或避开这一条件一般是理论分析的一个关键点，而形如定理9.2.1(ii)的结论对克服这一难点起重要作用 $^{[14,19]}$ 。
