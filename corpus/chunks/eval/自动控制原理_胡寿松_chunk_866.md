# (6) 位移定理

设 $F(s) = \mathcal{L}[f(t)]$ ，则有

$$\mathcal {L} [ f (t - \tau_ {0}) ] = \mathrm{e} ^ {- \tau_ {0} s} F (s)\mathcal {L} [ \mathrm{e} ^ {\alpha} f (t) ] = F (s - \alpha)$$

它们分别表示实域中的位移定理和复域中的位移定理。

证明 由式(A-11)得

$$\mathcal {L} [ f (t - \tau_ {0}) ] = \int_ {0} ^ {\infty} f (t - \tau_ {0}) \mathrm{e} ^ {- s t} \mathrm{d} t$$

令 $t - \tau_0 = \tau$ ，则有

$$\mathcal {L} [ f (t - \tau_ {0}) ] = \int_ {- \tau_ {0}} ^ {\infty} f (\tau) \mathrm{e} ^ {- s (\tau + \tau_ {0})} \mathrm{d} \tau = \mathrm{e} ^ {- \tau_ {0} s} \int_ {- \tau_ {0}} ^ {\infty} f (\tau) \mathrm{e} ^ {- v s} \mathrm{d} \tau = \mathrm{e} ^ {- \tau_ {0} s} F (s)$$

上式表示实域中的位移定理, 即当原函数 $f(t)$ 沿时间轴平移 $\tau_{0}$ 时, 相应于其象函数 $F(s)$ 乘以 $e^{-\tau_{0}s}$ 。

同样，由式(A-11)，有

$$\mathcal {L} [ \mathrm{e} ^ {\alpha t} f (t) ] = \int_ {0} ^ {\infty} \mathrm{e} ^ {\alpha t} f (t) \mathrm{e} ^ {- s} \mathrm{d} t = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- (s - \alpha) t} \mathrm{d} t = F (s - \alpha)$$

上式表示复域中的位移定理, 即当象函数 $F(s)$ 的自变量 $s$ 位移 $\alpha$ 时, 相应于其原函数 $f(t)$ 乘以 $\mathbf{e}^{\alpha}$ 。

位移定理在工程上很有用，可方便地求一些复杂函数的拉氏变换，例如由

$$\mathcal {L} [ \sin \omega t ] = \frac {\omega}{s ^ {2} + \omega^ {2}}$$

可直接求得

$$\mathcal {L} [ \mathrm{e} ^ {- \alpha} \sin \omega t ] = \frac {\omega}{(s + \alpha) ^ {2} + \omega^ {2}}$$
