# 2. 时延性质

假设函数 $f(t)$ 延迟了 $\lambda > 0$ 个时间单位。它的拉普拉斯变换为

$$F _ {1} (s) = \int_ {0} ^ {+ \infty} f (t - \lambda) \mathrm{e} ^ {- s t} \mathrm{d} t$$

定义 $t' = t - \lambda$ 那么 $\mathrm{dt}' = \mathrm{dt}$ ，因为 $\lambda$ 是一个常数，并且对于 $t < 0$ ， $f(t) = 0$ 。所以

$$F _ {1} (s) = \int_ {- \lambda} ^ {+ \infty} f (t ^ {\prime}) \mathrm{e} ^ {- s (t ^ {\prime} + \lambda)} \mathrm{d} t ^ {\prime} = \int_ {0} ^ {+ \infty} f (t ^ {\prime}) \mathrm{e} ^ {- s (t ^ {\prime} + \lambda)} \mathrm{d} t ^ {\prime}$$

因为 $e^{-s\lambda}$ 不依赖时间，可以将其拿到被积函数之外，所以，

$$F _ {1} (s) = \mathrm{e} ^ {- s \lambda} \int_ {0} ^ {+ \infty} f (t ^ {\prime}) \mathrm{e} ^ {- s t ^ {\prime}} \mathrm{d} t ^ {\prime} = \mathrm{e} ^ {- s \lambda} F (s) \tag {A.7}$$

从结果中可以看出时域上时滞 $\lambda$ 对应于频域上乘以 $e^{-s\lambda}$ 。
