# 6) 卷积定理

考虑下列卷积函数

$$f _ {1} (t) * f _ {2} (t) = \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau$$

由于 $\tau > t$ 时，有 $f_{1}(t - \tau)1(t - \tau) = 0$ ，因此

$$\int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau = \int_ {0} ^ {\infty} f _ {1} (t - \tau) 1 (t - \tau) f _ {2} (\tau) \mathrm{d} \tau$$

于是 $\mathcal{L}\left[\int_{0}^{t}f_{1}(t - \tau)f_{2}(\tau)\mathrm{d}\tau \right] = \mathcal{L}\left[\int_{0}^{\infty}f_{1}(t - \tau)1(t - \tau)f_{2}(\tau)\mathrm{d}\tau \right]$

$$= \int_ {0} ^ {\infty} \mathrm{e} ^ {- s t} \left[ \int_ {0} ^ {\infty} f _ {1} (t - \tau) 1 (t - \tau) f _ {2} (\tau) \mathrm{d} \tau \right] \mathrm{d} t$$

令 $t-\tau=\lambda$ ，并改变积分次序，可得

$$
\begin{array}{l} \mathcal {L} \left[ \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau \right] = \int_ {0} ^ {\infty} f _ {1} (t - \tau) 1 (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{d} \tau \\ = \int_ {0} ^ {\infty} f _ {1} (\lambda) \mathrm{e} ^ {- s (\lambda + \tau)} \mathrm{d} \lambda \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{d} \tau \\ = \int_ {0} ^ {\infty} f _ {1} (\lambda) \mathrm{e} ^ {- s \lambda} \mathrm{d} \lambda \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau \\ = F _ {1} (s) F _ {2} (s) \\ \end{array}
$$

式中

$$F _ {1} (s) = \int_ {0} ^ {\infty} f _ {1} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathscr {L} [ f _ {1} (t) ], \quad F _ {2} (s) = \int_ {0} ^ {\infty} f _ {2} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathscr {L} [ f _ {2} (t) ]$$

拉普拉斯变换的基本性质,如表 1-2 所示。

表 1-2 拉普拉斯变换的基本性质
