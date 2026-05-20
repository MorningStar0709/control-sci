$$
\begin{array}{l} y _ {k + 1} ^ {2} \leqslant 3 \left(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} + 3 \left(\Delta \hat {b} _ {1 k}\right) ^ {2} u _ {k} ^ {2} + O \left(d _ {k}\right) \\ = 3 \alpha_ {k} \left\{1 + \varphi_ {k} ^ {\mathrm{T}} P _ {k + 1} \varphi_ {k} + \varphi_ {k} ^ {\mathrm{T}} \left(P _ {k} - P _ {k + 1}\right) \varphi_ {k} \right\} \\ + 3 \left(\Delta \hat {b} _ {1 k}\right) ^ {2} u _ {k} ^ {2} + O \left(d _ {k}\right) \\ \leqslant 3 \alpha_ {k} \left\{2 + \delta_ {k} \| \varphi_ {k} \| ^ {2} \right\} + 3 \left(\Delta \hat {b} _ {1 k}\right) ^ {2} u _ {k} ^ {2} + O \left(d _ {k}\right) \\ = 3 \alpha_ {k} \delta_ {k} \| \varphi_ {k} \| ^ {2} + 3 (\Delta \hat {b} _ {1 k}) ^ {2} u _ {k} ^ {2} + O (d _ {k} + \log r _ {k}). \tag {9.5.50} \\ \end{array}
$$

利用 $B(z)$ 的稳定性，从式(9.5.1)知存在常数 $\lambda \in (0,1)$ 使式(9.5.33)成立，故

$$[ \| \varphi_ {k} \| ^ {2} - u _ {k} ^ {2} ] = O \left(\sum_ {i = 0} ^ {k} \lambda^ {k - i} y _ {i} ^ {2}\right) + O (d _ {k}). \tag {9.5.51}$$

进一步，将式(9.5.33)代入式(9.5.47)易见

$$u _ {k} ^ {2} = O \left(\log^ {2} r _ {k - 1} \left\{\sum_ {i = 0} ^ {k} \lambda^ {k - i} y _ {i} ^ {2} + d _ {k} \right\}\right), \tag {9.5.52}$$

于是由式 (9.5.51) 与式 (9.5.52) 得

$$\left\| \varphi_ {k} \right\| ^ {2} = O \left(\left(\log^ {2} r _ {k - 1}\right) L _ {k}\right) + O \left(d _ {k} \log^ {2} r _ {k}\right), \tag {9.5.53}$$

其中 $L_{k}\stackrel {\mathrm{def}}{=}\sum_{i = 0}^{k}\lambda^{k - i}y_{i}^{2}.$

又注意到

$$b _ {1} u _ {k} = \varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} - (\Delta \hat {b} _ {1 k}) u _ {k} + y _ {k + 1} ^ {*} + (b _ {1} u _ {k} - \theta^ {\mathrm{T}} \varphi_ {k}),$$

故利用式 (9.5.51) 有

$$
\begin{array}{l} b _ {1} ^ {2} u _ {k} ^ {2} \leqslant 3 \left(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} + 3 \left(\Delta \hat {b} _ {1 k}\right) ^ {2} u _ {k} ^ {2} + O \left(1 + \left| b _ {1} u _ {k} - \tilde {\theta} ^ {\mathrm{T}} \varphi_ {k} \right| ^ {2}\right) \\ = 3 \left(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} + 3 \left(\Delta \hat {b} _ {1 k}\right) ^ {2} u _ {k} ^ {2} + O \left(L _ {k} + d _ {k}\right). \tag {9.5.54} \\ \end{array}
$$

类似于式 (9.5.50) 的证明知

$$(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2} \leqslant \alpha_ {k} \delta_ {k} \| \varphi_ {k} \| ^ {2} + 2 \alpha_ {k}.$$

将此式代入式 (9.5.54) 并注意到 $\Delta \hat{b}_{1k} \longrightarrow 0$ 知对充分大的 $k$

$$u _ {k} ^ {2} = O \left(\alpha_ {k} \delta_ {k} \| \varphi_ {k} \| ^ {2}\right) + O \left(L _ {k} + d _ {k} + \log r _ {k}\right).$$

将此式与式 (9.5.51) 相结合得
