# 3. 拉普拉斯变换

工程实践中常用的一些函数,如阶跃函数,它们往往不能满足傅氏变换的条件,如果对这种函数稍加处理,一般都能进行傅氏变换,于是就引入了拉普拉斯变换。例如,对于单位阶跃函数 $f(t)=1(t)$ 的傅氏变换,由式(A-9)可求得为

$$F (\omega) = \mathcal {F} [ f (t) ] = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \frac {1}{\omega} (\sin \omega t + \cos \omega t) \Bigg | _ {0} ^ {\infty}$$

显然， $F(\omega)$ 无法计算出来，这是因为单位阶跃函数不满足狄利克雷的第三条件，即 $\int_{-\infty}^{\infty}|f(t)|dt$ 不存在。

为了解决这个困难,我们用指数衰减函数 $\mathrm{e}^{-\sigma t}1(t)$ 代替 $1(t)$ , 因为当 $\sigma \to 0$ 时, $\mathrm{e}^{-\sigma t}1(t)$ 趋于 $1(t)$ 。 $\mathrm{e}^{-\sigma t}1(t)$ 可用下式表示为

$$
\mathrm{e} ^ {- \sigma t} 1 (t) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- \sigma t}, & t > 0 (\sigma > 0) \\ 0, & t <   0 \end{array} \right.
$$

用这个函数代入式(A-9)，求得它的傅氏变换为

$$F _ {\sigma} (\omega) = \mathcal {F} [ \mathrm{e} ^ {- \sigma t} 1 (t) ] = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \sigma t} 1 (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \sigma t} \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \frac {1}{\sigma + \mathrm{j} \omega}$$

上式说明, 单位阶跃函数乘以因子 $e^{-\alpha t}$ 后, 便可以进行傅氏变换, 这时, 由于进行变换的函数已经过处理, 而且只考虑 t > 0 的时间区间, 因此称之为单边广义傅里叶变换。

对于任意函数 $f(t)$ , 如果不满足狄利克雷第三条件, 一般是因为当 $t \to \infty$ 时, $f(t)$ 衰减太慢。仿照单位阶跃函数的处理方法, 也用因子 $\mathrm{e}^{-\sigma t} (\sigma > 0)$ 乘以 $f(t)$ , 则当 $t \to \infty$ 时, 衰减就快得多。通常把 $\mathrm{e}^{-\sigma t}$ 叫做收敛因子。但由于它在 $t \to -\infty$ 时起相反作用, 为此, 假设 $t < 0$ 时, $f(t) = 0$ 。这个假设在实际上是可以做到的, 因为我们总可以把外作用加到系统上的开始瞬间选为 $t = 0$ , 而 $t < 0$ 时的行为, 即外作用加到系统之前的行为, 可以在初始条件内考虑。这样, 我们对函数 $f(t)$ 的研究, 就变为在时间 $t = 0 \to \infty$ 区间对函数 $f(t) \mathrm{e}^{-\sigma t}$ 的研究, 并称之为 $f(t)$ 的广义函数, 它的傅里叶变换为单边傅氏变换, 即

$$F _ {\sigma} (\omega) = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- \sigma t} \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- (\sigma + \mathrm{j} \omega) t} \mathrm{d} t$$

若令 $s = \sigma +\mathrm{j}\omega$ ，则上式可写为

$$F _ {\sigma} \left(\frac {s - \sigma}{\mathrm{j}}\right) = F (s) = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {A-11}$$

而 $F_{\sigma}(\omega)$ 的傅氏反变换则由式(A-10)有

$$f (t) \mathrm{e} ^ {- \sigma t} = \mathcal {F} ^ {- 1} [ F _ {\sigma} (\omega) ] = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F _ {\sigma} (\omega) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega$$

等式两边同乘以 $\mathrm{e}^{\sigma t}$ ，得
