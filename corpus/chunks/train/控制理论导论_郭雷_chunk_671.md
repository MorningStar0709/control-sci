$$\left[ \bar {y} _ {t + 1}, \bar {\phi} _ {t}, \bar {w} _ {t + 1} \right] \stackrel {{\mathrm{def}}} {{=}} \sqrt {\lambda_ {t}} \left[ y _ {t + 1}, \phi_ {t}, w _ {t + 1} \right],$$

则显然WLS算法是下列线性模型：

$$\bar {y} _ {t + 1} = \theta^ {\mathrm{T}} \bar {\phi} _ {t} + \bar {w} _ {t + 1} \tag {9.2.29}$$

的 LS 算法. 于是类似于定理 9.2.1 的证明 (见式 (9.2.14) 和式 (9.2.15)) 得

$$
\begin{array}{l} \tilde {\theta} _ {n + 1} ^ {\mathrm{T}} P _ {n + 1} ^ {- 1} \tilde {\theta} _ {n + 1} + (1 + o (1)) \sum_ {k = 0} ^ {n} a _ {k} \left(\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} \\ = O (1) + \sum_ {k = 0} ^ {n} \lambda_ {k} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} w _ {k + 1} ^ {2}, \tag {9.2.30} \\ \end{array}
$$

其中 $P_{k}, a_{k}$ 和 $\lambda_{k}$ 由式 (9.2.26)\~ 式 (9.2.28) 所定义.

利用式 (9.2.26) 易知

$$a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} = \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k + 1} \phi_ {k}.$$

于是

$$a _ {k} \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} = \lambda_ {k} \bar {\phi} _ {k} ^ {\mathrm{T}} P _ {k + 1} \bar {\phi} _ {k} = \lambda_ {k} \frac {| P _ {k + 1} ^ {- 1} | - | P _ {k} ^ {- 1} |}{| P _ {k + 1} ^ {- 1} |}.$$

但由于

$$\left| P _ {k + 1} ^ {- 1} \right| = \left| \sum_ {i = 0} ^ {k} \lambda_ {i} \phi_ {i} \phi_ {i} ^ {\mathrm{T}} + P _ {0} ^ {- 1} \right| \leqslant \left(\sum_ {i = 0} ^ {k} \lambda_ {i} \| \phi_ {i} \| ^ {2} + \| P _ {0} ^ {- 1} \|\right) ^ {d} \leqslant c _ {0} r _ {k} ^ {d}$$

其中 $d = \dim (\phi_i), c_0 > 0$ 是某常数．于是，我们知

$$\sum_ {k = 1} ^ {\infty} a _ {k} \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \leqslant d ^ {1 + \delta} \sum_ {k = 1} ^ {\infty} \frac {\left| P _ {k + 1} ^ {- 1} \right| - \left| P _ {k} ^ {- 1} \right|}{\left| P _ {k + 1} ^ {- 1} \right| \log^ {1 + \delta} \left\{c _ {0} ^ {- 1} \mid P _ {k + 1} ^ {- 1} \right| \}} < \infty , \tag {9.2.31}$$

注意到

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} a _ {k} \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} w _ {k + 1} ^ {2} \\ = \sum_ {k = 1} ^ {\infty} a _ {k} \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \left(w _ {k + 1} ^ {2} - E \left[ w _ {k + 1} ^ {2} \mid \mathcal {F} _ {k} \right]\right) + \sum_ {k = 1} ^ {\infty} a _ {k} \lambda_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} E \left[ w _ {k + 1} ^ {2} \mid \mathcal {F} _ {k} \right] \\ \end{array}
$$

由条件 (A1)( $\beta = 2$ 即可) 知第二个级数收敛，而根据第四章鞅收敛定理 4.2.11 知第一个级数也收敛。于是式 (9.2.30) 中右端的求和式当 $n \to \infty$ 时有极限，因而定理证毕。

利用定理9.2.2可直接得到如下推论：

推论9.2.3 在定理9.2.2的条件下，WLS算法有下列性质：

(i) $\| \tilde{\theta}_t\|^2 = O(\lambda_{\max}(P_t))$ a.s.
