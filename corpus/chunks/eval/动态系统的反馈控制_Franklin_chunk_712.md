# 10. 频域微分性质

时域上函数乘以时间对应于频域上函数的微分：

$$\frac {\mathrm{d}}{\mathrm{d} s} F (s) = \frac {\mathrm{d}}{\mathrm{d} s} \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- s t} f (t) \mathrm{d} t = \int_ {0} ^ {+ \infty} - t \mathrm{e} ^ {- s t} f (t) \mathrm{d} t = - \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- s t} [ t f (t) ] \mathrm{d} t = - \mathscr {L} \{t f (t) \}$$

那么

$$\mathcal {L} \{t f (t) \} = - \frac {\mathrm{d}}{\mathrm{d} s} F (s) \tag {A.22}$$

结果与分析相同。
