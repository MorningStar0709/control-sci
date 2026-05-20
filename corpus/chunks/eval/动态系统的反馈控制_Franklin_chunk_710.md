# 8. 频域卷积性质

在时域中进行乘积运算相当于在频域中进行卷积运算：

$$\mathcal {L} \left\{f _ {1} (t) f _ {2} (t) \right\} = \frac {1}{2 \pi \mathrm{j}} \int_ {\sigma_ {\mathrm{c}} - \mathrm{j} \infty} ^ {\sigma_ {\mathrm{c}} + \mathrm{j} \infty} F _ {1} (\xi) F _ {2} (s - \xi) \mathrm{d} \xi$$

分析如下关系式

$$\mathcal {L} \left\{f _ {1} (t) f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} f _ {1} (t) f _ {2} (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

用式(3.33)代替 $f_{1}(t)$ 得

$$\mathcal {L} \left\{f _ {1} (t) f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} \left[ \frac {1}{2 \pi \mathrm{j}} \int_ {\sigma_ {\mathrm{c}} - \mathrm{j} \infty} ^ {\sigma_ {\mathrm{c}} + \mathrm{j} \infty} F _ {1} (\xi) \mathrm{e} ^ {\xi t} \mathrm{d} \xi \right] f _ {2} (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

变换积分顺序

$$\mathcal {L} \left\{f _ {1} (t) f _ {2} (t) \right\} = \frac {1}{2 \pi \mathrm{j}} \int_ {\sigma_ {c} + \mathrm{j} \infty} ^ {\sigma_ {c} + \mathrm{j} \infty} F _ {1} (\xi) \int_ {0} ^ {+ \infty} f _ {2} (t) ^ {\mathrm{e} - (s - \xi) t} \mathrm{d} t \mathrm{d} \xi$$

用式(A.9)，我们得到

$$\mathcal {L} \left\{f _ {1} (t) f _ {2} (t) \right\} = \frac {1}{2 \pi \mathrm{j}} \int_ {\sigma_ {\mathrm{c}} - \mathrm{j} \infty} ^ {\sigma_ {\mathrm{c}} + \mathrm{j} \infty} F _ {1} (\xi) F _ {2} (s - \xi) \mathrm{d} \xi = \frac {1}{2 \pi \mathrm{j}} F _ {1} (s) * F _ {2} (s) \tag {A.16}$$
