# 6. 积分性质

假设希望求一个时间函数积分的拉普拉斯变换：

$$F _ {1} (s) = \mathcal {L} \left\{\int_ {0} ^ {t} f (\xi) \mathrm{d} \xi \right\} = \int_ {0} ^ {+ \infty} \left[ \int_ {0} ^ {t} f (\xi) \mathrm{d} \xi \right] \mathrm{e} ^ {- s t} \mathrm{d} t$$

对上式应用分步积分，其中

$$u = \int_ {0} ^ {t} f (\xi) \mathrm{d} \xi \quad \text {和} \quad \mathrm{d} v = \mathrm{e} ^ {- s t} \mathrm{d} t$$

我们得到

$$F _ {1} (s) = \left[ - \frac {1}{s} \mathrm{e} ^ {- s t} \left(\int_ {0} ^ {t} f (\xi) \mathrm{d} \xi\right) \right] _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} - \frac {1}{s} \mathrm{e} ^ {- s t} f (t) \mathrm{d} t = \frac {1}{s} F (s) \tag {A.14}$$
