# (3) 积分定理

设 $F(s) = \mathcal{A}[f(t)]$ ，则有

$$\mathcal {L} \left[ \int f (t) \mathrm{d} t \right] = \frac {1}{s} F (s) + \frac {1}{s} f ^ {(- 1)} (0)$$

式中， $f^{(-1)}(0)$ 是 $\int f(t)\mathrm{d}t$ 在 $t = 0$ 时的值。

证明 由式(A-11)有

$$\mathscr {L} \left[ \int f (t) \mathrm{d} t \right] = \int_ {0} ^ {\infty} \left[ \int f (t) \mathrm{d} t \right] \mathrm{e} ^ {- s t} \mathrm{d} t$$

用分部积分法，令 $u = \int f(t)\mathrm{d}t,\mathrm{d}v = \mathrm{e}^{-st}\mathrm{d}t$ ，则有

$$
\begin{array}{l} \mathscr {L} \left[ \int f (t) \mathrm{d} t \right] = \left[ - \frac {1}{s} \mathrm{e} ^ {- s t} \int f (t) \mathrm{d} t \right] \Big | _ {0} ^ {\infty} + \frac {1}{s} \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \frac {1}{s} f ^ {(- 1)} (0) + \frac {1}{s} F (s) \\ \end{array}
$$

同理,对于 $f(t)$ 的多重积分的拉氏变换,有

$$\mathscr {L} \left[ \underbrace {\int \cdots \int} _ {n} f (t) (\mathrm{d} t) ^ {n} \right] = \frac {1}{s ^ {n}} F (s) + \frac {1}{s ^ {n}} f ^ {(- 1)} (0) + \dots + \frac {1}{s} f ^ {(- n)} (0)$$

式中， $f^{(-1)}(0)$ ， $f^{(-2)}(0)$ ，…， $f^{(-n)}(0)$ 为 $f(t)$ 的各重积分在t=0时的值。如果 $f^{(-1)}(0)=f^{(-2)}(0)=\cdots=f^{(-n)}(0)=0$ ，则有

$$\mathcal {L} \left[ \underbrace {\int \cdots \int} _ {n} f (t) (\mathrm{d} t) ^ {n} \right] = \frac {1}{s ^ {n}} F (s)$$

即原函数 $f(t)$ 的 $\pmb{n}$ 重积分的拉氏变换等于其象函数 $F(s)$ 除以 $s^n$ 。
