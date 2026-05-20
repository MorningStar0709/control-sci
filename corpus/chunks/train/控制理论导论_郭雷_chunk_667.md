(i) $\tilde{\theta}_{t + 1}^{\mathbf{T}}P_{t + 1}^{-1}\tilde{\theta}_{t + 1} = O(\log r_t)$ a.s.;   
(ii) $\sum_{k=0}^{t} \frac{(\phi_k^{\mathrm{T}} \bar{\theta}_k)^2}{1 + \phi_k^{\mathrm{T}} P_k \phi_k} = O(\log r_t)$ , a.s.

其中 $\tilde{\theta}_t\stackrel {\mathrm{def}}{=}\theta -\theta_t$ ，“ $O$ ”常数是不依赖于 $t$ 变化的量，而

$$r _ {t} \stackrel {\text { def }} {=} 1 + \sum_ {i = 0} ^ {t} \| \phi_ {i} \| ^ {2}. \tag {9.2.9}$$

证明 将式 (9.2.1) 代入式 (9.2.6) 得

$$\tilde {\theta} _ {k + 1} = (I - a _ {k} P _ {k} \phi_ {k} \phi_ {k} ^ {\mathrm{T}}) \tilde {\theta} _ {k} - a _ {k} P _ {k} \phi_ {k} \omega_ {k + 1}. \tag {9.2.10}$$

对式 (9.2.5) 右乘 $P_{k}^{-1}$ 得

$$P _ {k + 1} P _ {k} ^ {- 1} = I - a _ {k} P _ {k} \phi_ {k} \phi_ {k} ^ {\mathrm{T}}. \tag {9.2.11}$$

又注意到 $P_{k + 1}^{-1} = P_k^{-1} + \phi_k\phi_k^{\mathrm{T}}$ ，从而

$$P _ {k + 1} ^ {- 1} P _ {k} = I + \phi_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k}. \tag {9.2.12}$$

于是利用式 (9.2.10) 及式 (9.2.11) 得

$$\tilde {\theta} _ {k + 1} = P _ {k + 1} P _ {k} ^ {- 1} \tilde {\theta} _ {k} - a _ {k} P _ {k} \phi_ {k} \omega_ {k + 1}$$

或

$$P _ {k + 1} ^ {- 1} \tilde {\theta} _ {k + 1} = P _ {k} ^ {- 1} \tilde {\theta} _ {k} - a _ {k} P _ {k + 1} ^ {- 1} P _ {k} \phi_ {k} \omega_ {k + 1}. \tag {9.2.13}$$

下面考虑 Lyapunov 函数

$$V _ {k} = \tilde {\theta} _ {k} ^ {\mathrm{T}} P _ {k} ^ {- 1} \tilde {\theta} _ {k}.$$

利用式 (9.2.10)\~ 式 (9.2.13) 得

$$
\begin{array}{l} V _ {k + 1} = \tilde {\theta} _ {k + 1} ^ {\mathrm{T}} P _ {k + 1} ^ {- 1} \tilde {\theta} _ {k + 1} \\ = \left[ \tilde {\theta} _ {k} ^ {\mathrm{T}} \left(I - a _ {k} \phi_ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k}\right) - a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \omega_ {k + 1} \right] \left[ P _ {k} ^ {- 1} \tilde {\theta} _ {k} - P _ {k + 1} ^ {- 1} a _ {k} P _ {k} \phi_ {k} \omega_ {k + 1} \right] \\ = \tilde {\theta} _ {k} ^ {\mathrm{T}} P _ {k} ^ {- 1} \tilde {\theta} _ {k} - a _ {k} \left(\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} - 2 a _ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \omega_ {k + 1} + a _ {k} ^ {2} \phi_ {k} ^ {\mathrm{T}} P _ {k} P _ {k + 1} ^ {- 1} P _ {k} \phi_ {k} \omega_ {k + 1} ^ {2} \\ = V _ {k} - a _ {k} \left(\phi_ {k} ^ {\mathrm{T}} \bar {\theta} _ {k}\right) ^ {2} - 2 a _ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \omega_ {k + 1} + a _ {k} \phi_ {k} ^ {\mathrm{T}} P _ {k} \phi_ {k} \omega_ {k + 1} ^ {2}. \\ \end{array}
$$

将此式从 $k = 0$ 到 $\pmb{n}$ 求和得
