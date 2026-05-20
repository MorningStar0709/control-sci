# (3) 复数位移定理

如果函数 $e(t)$ 是可拉氏变换的，其 $\pmb{z}$ 变换为 $E(z)$ ，则有

$$\mathcal {L} \big [ \mathrm{e} ^ {\mp a t} e (t) \big ] = E (z \mathrm{e} ^ {\pm a T}) \tag {7-30}$$

证明 由 $z$ 变换定义

$$\mathcal {L} \big [ \mathrm{e} ^ {\mp a t} e (t) \big ] = \sum_ {n = 0} ^ {\infty} \mathrm{e} ^ {\mp a n T} e (n T) z ^ {- n} = \sum_ {n = 0} ^ {\infty} e (n T) (z \mathrm{e} ^ {\pm a T}) ^ {- n}$$

令 $z_{1} = z\mathrm{e}^{+aT}$

则有 $\mathcal{L}\big[\mathrm{e}^{\mp at}e(t)\big] = \sum_{n = 0}^{\infty}e(nT)z_1^{-n} = E(ze^{\pm aT})$

复数位移定理是仿照拉氏变换的复数位移定理导出的，其含意是函数 $e^{*}(t)$ 乘以指数序列

$e^{\mp amT}$ 的 z 变换，就等于在 $e^{*}(t)$ 的 z 变换表达式 $E(z)$ 中，以 $ze^{\pm aT}$ 取代原算子 z。

例 7-9 试用复数位移定理计算函数 $te^{-aT}$ 的 z 变换。

解 令 $e(t) = t$ ，由表7-2知

$$E (z) = \mathscr {L} [ t ] = \frac {T z}{(z - 1) ^ {2}}$$

根据复数位移定理(7-30)，有

$$
\begin{array}{l} E (z \mathrm{e} ^ {a T}) = \mathcal {L} [ t \mathrm{e} ^ {- a t} ] = \frac {T (z \mathrm{e} ^ {a T})}{(z \mathrm{e} ^ {a T} - 1) ^ {2}} \\ = \frac {T z e ^ {- a T}}{(z - e ^ {- a T}) ^ {2}} \\ \end{array}
$$
