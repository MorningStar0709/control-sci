$$\sum_ {j = 0} ^ {\infty} \delta_ {j} = \sum_ {j = 0} ^ {\infty} (\operatorname{tr} P _ {j} - \operatorname{tr} P _ {j + 1}) \leqslant \operatorname{tr} P _ {0} < \infty , \tag {9.5.36}$$

可知 $\delta_{j} \longrightarrow 0$ ，于是利用定理9.2.1(ii)知，对任何 $\epsilon > 0$ ，存在充分大的 $i_{0}$ 使

$$\lambda^ {- 1} C \sum_ {j = i} ^ {n} \delta_ {j} \alpha_ {j} \leqslant \epsilon \log r _ {n}, \quad \forall n \geqslant i \geqslant i _ {0}. \tag {9.5.37}$$

据此及不等式 $1 + x \leqslant \mathrm{e}^x, x \geqslant 0$ ，得

$$
\begin{array}{l} \prod_ {j = i} ^ {\infty} \left(1 + \lambda^ {- 1} C \delta_ {j} \alpha_ {j}\right) \leqslant \exp \left\{\lambda^ {- 1} C \sum_ {j = i} ^ {n} \alpha_ {j} \delta_ {j} \right\} \\ \leqslant \exp \left\{\epsilon \log r _ {n} \right\} = r _ {n} ^ {\epsilon}, \quad \forall n \geqslant i \geqslant i _ {0}. \tag {9.5.38} \\ \end{array}
$$

将此式代入式 (9.5.35) 并利用式 (9.5.30) 得

$$L _ {n + 1} = O (r _ {n} ^ {\epsilon} d _ {n} \log r _ {n}), \quad \forall \epsilon > 0.$$

从而利用 $\epsilon$ 的任意性从式 (9.5.28) 得

$$y _ {n + 1} ^ {2} = O (r _ {n} ^ {\epsilon} d _ {n}), \quad \forall \epsilon > 0.$$

据此利用式 (9.5.33) 又可得

$$u _ {n} ^ {2} = O (r _ {n} ^ {\epsilon} d _ {n}), \quad \forall \epsilon > 0.$$

故引理得证.

定理 9.5.1 考虑自适应控制系统式 (9.5.19)\~(9.5.23) 并设条件 (A1)\~(A3) 满足，则闭环系统具有稳定性与最优性，且

$$R _ {n} = O (n ^ {\epsilon} d _ {n}) \quad \text { a.s. } \quad \forall \epsilon > 0, \tag {9.5.39}$$

其中 $R_{n}, d_{n}$ 分别由式 (9.5.16) 及式 (9.5.26) 定义.

证明 首先注意到若式 (9.5.39) 成立，则据式 (9.5.27)，最优性 $R_{n} = o(n)$ 显然成立。进一步，据最优性及 (A1) 和 (A3) 立即看出

$$\sum_ {i = 0} ^ {n} y _ {i} ^ {2} = O (n) \quad \text { a.s. }$$

进而利用式 (9.5.1) 的最小相位假设又可得

$$\sum_ {i = 0} ^ {n} u _ {i} ^ {2} = O (n) \quad \text { a.s. }$$

因此稳定性也成立.

所以，我们仅需证明式(9.5.39).

利用式 (9.5.24), 定理 9.2.1 及引理 9.5.2 从式 (9.5.31) 得

$$
\begin{array}{l} R _ {n + 1} = \sum_ {i = 0} ^ {n} (y _ {i + 1} - y _ {i + 1} ^ {*} - w _ {i + 1}) ^ {2} \\ = \sum_ {i = 0} ^ {n} \left(\varphi_ {i} ^ {\mathrm{T}} \tilde {\theta} _ {i}\right) ^ {2} = \sum_ {i = 0} ^ {n} \alpha_ {i} \left(1 + \varphi_ {i} ^ {\mathrm{T}} P _ {i} \varphi_ {i}\right) \\ = O \left(\log r _ {n}\right) + O \left(\sum_ {i = 0} ^ {n} \alpha_ {i} \| \varphi_ {i} \| ^ {2}\right) \\ = O \left(\log r _ {n}\right) + O \left(r _ {n} ^ {\epsilon} d _ {n} \log r _ {n}\right) \\ = O (r _ {n} ^ {\epsilon} d _ {n}), \quad \forall \epsilon > 0. \tag {9.5.40} \\ \end{array}
$$

因此，为证式(9.5.39)，只需证明

$$r _ {n} = O (n). \tag {9.5.41}$$

利用式 (9.5.40) 及 $\{y_i^*\}$ 与 $\{w_i\}$ 的性质易见
