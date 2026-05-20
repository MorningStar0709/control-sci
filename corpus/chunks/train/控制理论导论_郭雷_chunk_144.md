$$\varphi (t) \leqslant \xi (t) + \int_ {t _ {0}} ^ {t} \lambda (\tau) \xi (\tau) \mathrm{e} ^ {\int_ {\tau} ^ {t} \lambda (s) \mathrm{d} s} \mathrm{d} \tau , \quad \forall t \in [ t _ {0}, t _ {1} ].$$

证明 令 $f(t,x) = \lambda (t)x + \xi '(t)$ ，那么

$$\varphi (t) \leqslant \int_ {t _ {0}} ^ {t} f (\tau , \varphi (\tau)) \mathrm{d} \tau + \xi (t _ {0}), \quad \forall t \in [ t _ {0}, t _ {1} ],$$

从而 $\varphi(t)$ 满足定理2.2.4的条件(2.2.14).于是根据定理2.2.4, $\varphi(t) \leqslant \psi(t), \forall t \in [t_0, t_1]$ , 其中 $\psi(t)$ 是方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = \lambda (t) x + \xi^ {\prime} (t), \quad x (t _ {0}) = \xi (t _ {0})$$

的最大解．但在目前情况下，上述线性方程的唯一解是

$$\psi (t) = \mathrm{e} ^ {\int_ {t _ {0}} ^ {t} \lambda (s) \mathrm{d} s} \xi (t _ {0}) + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {\int_ {\tau} ^ {t _ {0}} \lambda (s) \mathrm{d} s} \xi^ {\prime} (\tau) \mathrm{d} \tau ,$$

因此定理得证.

利用分部积分，我们可以将定理中 Gronwall 不等式改写成

$$\varphi (t) \leqslant \xi (t) + \int_ {t _ {0}} ^ {t} \lambda (\tau) \xi (\tau) \mathrm{e} ^ {\int_ {\tau} ^ {t _ {0}} \lambda (s) \mathrm{d} s} \mathrm{d} \tau , \quad \forall t \in [ t _ {0}, t _ {1} ].$$

在这种形式的 Gronwall 不等式中，我们并不要求 $\xi(t)$ 绝对连续，而只要求它可积就够了.

为方便读者阅读，这里我们还给出一种直接的证明方法。令

$$h (t) = \int_ {t _ {0}} ^ {t} \lambda (\tau) \varphi (\tau) \mathrm{d} \tau ,$$

则有

$$\frac {\mathrm{d} h (t)}{\mathrm{d} t} = \lambda (t) \varphi (t), \quad h (t _ {0}) = 0.$$

于是

$$\frac {\mathrm{d}}{\mathrm{d} t} \left(h (t) \mathrm{e} ^ {- \int_ {t _ {0}} ^ {t} \lambda (s) \mathrm{d} s}\right) = (\lambda (t) \varphi (t) - \lambda (t) h (t)) \mathrm{e} ^ {- \int_ {t _ {0}} ^ {t} \lambda (s) \mathrm{d} s}.$$

由假设条件和 $\lambda(t)$ 的非负性知

$$\lambda (t) \varphi (t) \leqslant \lambda (t) \Big (h (t) + \xi (t) \Big), \quad \forall t \in [ t _ {0}, t _ {1} ],$$

所以

$$\frac {\mathrm{d}}{\mathrm{d} t} \left(h (t) \mathrm{e} ^ {- \int_ {t _ {0}} ^ {t} \lambda (s) \mathrm{d} s}\right) \leqslant \lambda (t) \xi (t) \mathrm{e} ^ {- \int_ {t _ {0}} ^ {t} \lambda (s) \mathrm{d} s}.$$

从 $t_0$ 到 $t$ 积分上式，并注意到 $h(t_0) = 0$ 可得

$$h (t) \leqslant \int_ {t _ {0}} ^ {t} \lambda (\tau) \xi (\tau) \mathrm{e} ^ {\int_ {\tau} ^ {t} \lambda (s) \mathrm{d} s} \mathrm{d} \tau .$$

于是从 $\varphi(t) \leqslant h(t) + \xi(t)$ 即得 Gronwall 不等式.

现在讨论标准一阶微分方程组的解的性质，着重讨论其解的存在、唯一性，解对初值和参数的连续依赖性等问题。形如

$$\frac {\mathrm{d} x}{\mathrm{d} t} = f (t, x), \quad x \in \mathbb {R} ^ {n} \tag {2.2.19}$$
