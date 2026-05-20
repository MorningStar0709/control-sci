# 11) 拉普拉斯变换的积分下限

在某些情况下,若函数 $f(t)$ 在 t=0 处有一个脉冲函数,这时必须明确指出拉普拉斯积分下限是 $0_{-}$ 还是 $0_{+}$ ,因为对这两种下限, $f(t)$ 的拉普拉斯变换是不同的。设

$$\mathcal {L} _ {+} [ f (t) ] = \int_ {0 _ {+}} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t\mathcal {L} _ {-} [ f (t) ] = \int_ {0 _ {-}} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathcal {L} _ {+} [ f (t) ] + \int_ {0 _ {-}} ^ {0 _ {+}} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

如果 $f(t)$ 在 t=0 处包含一个脉冲函数，则因 $\int_{0}^{0+}f(t)e^{-st}dt\neq0$ ，故有

$$\mathcal {L} _ {+} [ f (t) ] \neq \mathcal {L} _ {-} [ f (t) ]$$

显然,如果在 t=0 处不具有脉冲函数,则有

$$\mathcal {L} _ {+} [ f (t) ] = \mathcal {L} _ {-} [ f (t) ]$$

常用函数的拉普拉斯变换对照表,如表 1-1 所示。

表 1-1 常用函数拉普拉斯变换对照表
