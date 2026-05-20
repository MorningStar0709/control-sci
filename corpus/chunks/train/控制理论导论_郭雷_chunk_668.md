$$
\begin{array}{l} V _ {n + 1} + \sum_ {k = 0} ^ {n} a _ {k} \left(\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} \\ = V _ {0} - 2 \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \omega_ {k + 1} + \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \omega_ {k + 1} ^ {2}. \tag {9.2.14} \\ \end{array}
$$

下面分别估计上式最后两项．注意到 $a_{k} \leqslant 1$ 且 $a_{k}\phi_{k}^{\mathrm{T}}\tilde{\theta}_{k} \in \mathcal{F}_{k}$ ，因此利用鞅估计定理4.2.13知，对任意 $\delta > 0$ 有

$$\sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \omega_ {k + 1} = O \left(\left\{\sum_ {k = 0} ^ {n} a _ {k} (\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2} \right\} ^ {\frac {1}{2} + \delta}\right).$$

取 $0 < \delta < \frac{1}{2}$ , 有

$$\sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \omega_ {k + 1} = O (1) + o \left(\sum_ {k = 0} ^ {n} a _ {k} (\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2}\right). \tag {9.2.15}$$

为估第二项，注意到

$$P _ {k + 1} ^ {- 1} = P _ {k} ^ {- 1} + \phi_ {k} \phi_ {k} ^ {\mathrm{T}} = P _ {k} ^ {- 1} (I + P _ {k} \dot {\phi} _ {k} \phi_ {k} ^ {\mathrm{T}}),$$

取行列式 $|\cdot|$ 得

$$\mid P _ {k + 1} ^ {- 1} \mid = \mid P _ {k} ^ {- 1} \mid (1 + \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k}).$$

故

$$\phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} = \frac {| P _ {k + 1} ^ {- 1} | - | P _ {k} ^ {- 1} |}{| P _ {k} ^ {- 1} |},$$

进而

$$a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} = \frac {| P _ {k + 1} ^ {- 1} | - | P _ {k} ^ {- 1} |}{| P _ {k + 1} ^ {- 1} |}.$$

于是

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} = \sum_ {k = 0} ^ {n} \frac {\left| P _ {k + 1} ^ {- 1} \right| - \left| P _ {k} ^ {- 1} \right|}{\left| P _ {k + 1} ^ {- 1} \right|} \\ \leqslant \sum_ {k = 0} ^ {n} \int_ {\left| P _ {k} ^ {- 1} \right|} ^ {\left| P _ {k + 1} ^ {- 1} \right|} \frac {\mathrm{d} x}{x} = \log | P _ {n + 1} ^ {- 1} | + \log | P _ {0} |. \tag {9.2.16} \\ \end{array}
$$

利用 $c_{\tau}$ 不等式 (4.1.14) 及 Lyapunov 不等式易知，对任何 $\alpha \in (2, \min(\beta, 4)]$ 有

$$
\begin{array}{l} \sup _ {k} E \left[ \left| \omega_ {k + 1} ^ {2} - E \left(\omega_ {k + 1} ^ {2} \mid \mathcal {F} _ {k}\right) \right| ^ {\frac {\alpha}{2}} \mid \mathcal {F} _ {k} \right] \\ \leqslant 4 \sup _ {k} E \left[ | \omega_ {k + 1} | ^ {\alpha} \mid \mathcal {F} _ {k} \right] <   \infty , \quad \text { a.s. } \\ \end{array}
$$

于是利用鞅估计定理4.2.13得
