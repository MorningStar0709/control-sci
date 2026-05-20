$$G _ {1} (z) G _ {2} (z) \neq G _ {1} G _ {2} (z)$$

从这种意义上说，z 变换无串联性。下例可以说明这一点。

例 7-18 设开环离散系统如图 7-23(a) 及 (b) 所示, 其中 $G_{1}(s)=1/s$ , $G_{2}(s)=a/(s+a)$ , 输入信号 $r(t)=1(t)$ , 试求系统 (a) 和 (b) 的脉冲传递函数 $G(z)$ 和输出的 z 变换 $C(z)$ 。

解 查 z 变换表, 输入 $r(t)=1(t)$ 的 z 变换为

$$R (z) = \frac {z}{z - 1}$$

对于系统(a)

$$G _ {1} (z) = \mathcal {L} \left[ \frac {1}{s} \right] = \frac {z}{z - 1}, \quad G _ {2} (z) = \mathcal {L} \left[ \frac {a}{s + a} \right] = \frac {a z}{z - e ^ {- a T}}$$

有 $G(z) = G_{1}(z)G_{2}(z) = \frac{az^{2}}{(z - 1)(z - \mathrm{e}^{-aT})}$

$$C (z) = G (z) R (z) = \frac {a z ^ {3}}{(z - 1) ^ {2} (z - e ^ {- a T})}$$

对于系统(b)

$$G _ {1} (s) G _ {2} (s) = \frac {a}{s (s + a)}$$

有 $G(z) = G_{1}G_{2}(z) = \mathcal{L}\left[\frac{a}{s(s + a)}\right] = \frac{z(1 - \mathrm{e}^{-aT})}{(z - 1)(z - \mathrm{e}^{-aT})}$

$$C (z) = G (z) R (z) = \frac {z ^ {2} (1 - \mathrm{e} ^ {- a T})}{(z - 1) ^ {2} (z - \mathrm{e} ^ {- a T})}$$

显然，在串联环节之间有无同步采样开关隔离时，其总的脉冲传递函数和输出 $z$ 变换是不相同的。但是，不同之处仅表现在其零点不同，极点仍然一样。这也是离散系统特有的现象。
