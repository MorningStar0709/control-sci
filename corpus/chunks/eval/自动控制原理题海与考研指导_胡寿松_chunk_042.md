# 1. $z$ 变换定义

设连续函数 $e(t)$ 是可拉普拉斯变换的，则

$$E (s) = \int_ {0} ^ {\infty} e (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

由于 $t < 0$ ，有 $e(t) = 0$ ，故上式又可表示为

$$E (s) = \int_ {- \infty} ^ {\infty} e (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

对于 $e(t)$ 的采样信号

$$e ^ {*} (t) = \sum_ {n = 0} ^ {\infty} e (n T) \delta (t - n T)$$

其拉普拉斯变换为

$$E ^ {*} (s) = \int_ {- \infty} ^ {\infty} e ^ {*} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \sum_ {n = 0} ^ {\infty} e (n T) \left[ \int_ {- \infty} ^ {\infty} \delta (t - n T) \mathrm{e} ^ {- s t} \mathrm{d} t \right]$$

由广义脉冲函数的筛选性质

$$\int_ {- \infty} ^ {\infty} \delta (t - n T) f (t) \mathrm{d} t = f (n T)$$

故有 $\int_{-\infty}^{\infty}\delta (t - nT)\mathrm{e}^{-st}\mathrm{d}t = \mathrm{e}^{-snT}$

于是采样拉普拉斯变换可表示为

$$E ^ {*} (s) = \sum_ {n = 0} ^ {\infty} e (n T) \mathrm{e} ^ {- s n T}$$

令 $z=e^{sT}$ ，其中 T 为采样周期，z 是复平面上定义的一个复变量，称为 z 变换算子。则采样信号 $e^{*}(t)$ 的 z 变换定义为

$$E (z) = E ^ {*} (s) \mid_ {s = \frac {1}{T} \ln z} = \sum_ {n = 0} ^ {\infty} e (n T) z ^ {- n}$$

记作 $E(z) = \mathcal{L}[e^{*}(t)] = \mathcal{L}[e(t)]$

注意,定义式中后一记号是为了书写方便,并不意味是连续信号 $e(t)$ 的 z 变换,而仍指采样信号 $e^{*}(t)$ 的 z 变换。
