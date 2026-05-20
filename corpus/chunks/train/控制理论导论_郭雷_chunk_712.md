$$\tau_ {n} = \inf \{k > \tau_ {n - 1}: | b _ {1} (k + 1) | < a \}, \quad \tau_ {0} = 0. \tag {9.5.69}$$

显然，在 $D_{1}$ 的余集 $D_{1}^{c}$ 上有 $\tau_{n} < \infty, \forall n,$ 因此若定义

$$
\sigma_ {n} = \left\{ \begin{array}{l l} n, & \omega \in D _ {1}, \\ \tau_ {n}, & \omega \in D _ {1} ^ {c}, \end{array} \right. \tag {9.5.70}
$$

则 $\sigma_{n} < \infty, \forall n,$ 且 $\sigma_{n\overline{n - \infty}} \propto \infty, \text{a.s.}$

定理 9.5.5 对系统 (9.5.1) 设条件 (A1)\~(A3) 成立，且 LS-STR 由式 (9.5.15) 所定义，则下述结果成立：

(i) 对由式 (9.5.69)\~ 式 (9.5.70) 定义的 $\sigma_{n}$ 有

$$r _ {\sigma_ {n}} = O \left(\sigma_ {n}\right) \quad \text { a . s . }R _ {\sigma_ {n} + 1} = O \left(\sigma_ {n} ^ {\epsilon} d _ {\sigma_ {n}}\right), \quad \text { a . s . } \quad \forall \epsilon > 0, \tag {9.5.71}$$

其中 $R_{n}, r_{n}$ 和 $d_{n}$ 分别由式 (9.5.16), 式 (9.5.25) 及式 (9.5.26) 定义;

(ii) 设 $D_{1}$ 和 $\tau_{n}$ 分别由式 (9.5.68) 和式 (9.5.69) 定义. 记

$$D = D _ {1} \bigcup D _ {2}, \tag {9.5.72}D _ {2} = \left\{\omega \in D _ {1} ^ {\mathrm{c}}: \sup _ {n} \tau_ {n + 1} / \tau_ {n} < \infty \right\}, \tag {9.5.73}$$

则在 $D$ 上几乎处处有

$$R _ {n} = O (n ^ {\delta}), \quad \forall \delta \in \left(\frac {2}{\beta}, 1\right), \tag {9.5.74}$$

其中 $\beta$ 由条件 (A1) 给出.

证明 (i) 在 $D_{1}$ 上利用定理9.5.4知结论成立，故只需考虑 $D_{1}^{c}$ . 据 $\tau_{n}$ 的定义有

$$\inf _ {n} \left| b _ {1} (\tau_ {n} + 1) - b _ {1} \right| \geqslant | b _ {1} | - a > 0, \quad \omega \in D _ {1} ^ {c}.$$

故据引理9.5.5知在 $D_{1}^{c}$ 上，对 $\forall \epsilon >0$ 有

$$r _ {\tau_ {n}} = O (\tau_ {n}), \quad \sup _ {i \leqslant \tau_ {n}} \| \varphi_ {i} \| ^ {2} = O (\tau_ {n} ^ {\epsilon} d _ {\tau_ {n}}).$$

故由式 (9.5.14), 式 (9.5.4) 及定理 9.2.1 知

$$
\begin{array}{l} R _ {\tau_ {n} + 1} = \sum_ {i = 0} ^ {\tau_ {n}} (y _ {i + 1} - y _ {i + 1} ^ {*} - w _ {i + 1}) ^ {2} \\ = \sum_ {i = 0} ^ {\tau_ {n}} (\tilde {\theta} _ {i} ^ {\mathrm{T}} \varphi_ {i}) ^ {2} = \sum_ {i = 0} ^ {\tau_ {n}} \alpha_ {i} (1 + \varphi_ {i} ^ {\mathrm{T}} P _ {i} \varphi_ {i}) \\ = O \left(\tau_ {n} ^ {\epsilon} d _ {\tau_ {n}} \sum_ {i = 0} ^ {\tau_ {n}} \alpha_ {i}\right) = O \left(\tau_ {n} ^ {\epsilon} d _ {\tau_ {n}} \log \tau_ {\tau_ {n}}\right), \quad \forall \epsilon > 0 \\ \end{array}
$$

因此在 $D_{1}^{c}$ 上式(9.5.71)也成立；

(ii) 首先在 $D_{1}$ 上利用定理9.5.4并注意 $d_{n}$ 可取为

$$d _ {n} = O (n ^ {\delta}), \quad \forall \delta \in \left(\frac {2}{\beta}, 1\right)$$

可知式 (9.5.74) 成立.

在 $D_{2} \subset D_{1}^{c}$ 上利用式 (9.5.71) 可知

$$R _ {\tau_ {n}} = O (\tau_ {n} ^ {\delta}), \quad \forall \delta \in \left(\frac {2}{\beta}, 1\right).$$

于是
