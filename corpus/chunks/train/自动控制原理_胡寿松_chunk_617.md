# (3) 非奇次状态方程的解

状态方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t) \tag {9-42}$$

称为非奇次状态方程，有如下两种解法。

1）积分法。由式(9-42)可得

$$\mathrm{e} ^ {- A t} (\dot {\boldsymbol {x}} (t) - \boldsymbol {A x} (t)) = \mathrm{e} ^ {- A t} \boldsymbol {B u} (t)$$

由于 $\frac{\mathrm{d}}{\mathrm{d}t} (\mathrm{e}^{-A^t}\pmb {x}(t)) = -\pmb {A}\mathrm{e}^{-A^t}\pmb {x}(t) + \mathrm{e}^{-A^t}\dot{\pmb{x}}(t) = \mathrm{e}^{-A^t}[\dot{\pmb{x}} (t) - \pmb {A}\pmb {x}(t)]$

积分可得

$$\mathrm{e} ^ {- A t} \boldsymbol {x} (t) - \boldsymbol {x} (0) = \int_ {0} ^ {t} \mathrm{e} ^ {- A \tau} \boldsymbol {B u} (\tau) \mathrm{d} \tau\boldsymbol {x} (t) = \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {x} (0) + \int_ {0} ^ {t} \mathrm{e} ^ {\boldsymbol {A} (t - \tau)} \boldsymbol {B u} (\tau) \mathrm{d} \tau= \boldsymbol {\Phi} (t) \boldsymbol {x} (0) + \int_ {0} ^ {t} \boldsymbol {\Phi} (t - \tau) \boldsymbol {B u} (\tau) \mathrm{d} \tau \tag {9-43}$$

式中第一项是对初始状态的响应,第二项是对输入作用的响应。

若取 $t_0$ 作为初始时刻，则有

$$\mathrm{e} ^ {- A t} \boldsymbol {x} (t) - \mathrm{e} ^ {- A t _ {0}} \boldsymbol {x} \left(t _ {0}\right) = \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {- A \tau} \boldsymbol {B u} (\tau) \mathrm{d} \tau\boldsymbol {x} (t) = \mathrm{e} ^ {\boldsymbol {A} (t - t _ {0})} \boldsymbol {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {\boldsymbol {A} (t - \tau)} \boldsymbol {B u} (\tau) \mathrm{d} \tau= \boldsymbol {\Phi} (t - t _ {0}) \boldsymbol {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} \boldsymbol {\Phi} (t - \tau) \boldsymbol {B u} (\tau) \mathrm{d} \tau \tag {9-44}$$

2) 拉普拉斯变换法。将式(9-42)两端取拉氏变换，有

$$s \boldsymbol {X} (s) - \boldsymbol {x} (0) = \boldsymbol {A} \boldsymbol {X} (s) + \boldsymbol {B} \boldsymbol {U} (s)$$

则 $(sI - A)X(s) = x(0) + BU(s)$

$$\boldsymbol {X} (s) = (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {x} (0) + (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B U} (s)$$

进行拉氏反变换，有

$$\boldsymbol {x} (t) = \mathscr {L} ^ {- 1} \left[ (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \right] \boldsymbol {x} (0) + \mathscr {L} ^ {- 1} \left[ (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B U} (s) \right]$$

由拉氏变换卷积定理

$$\mathcal {L} ^ {- 1} \left[ F _ {1} (s) F _ {2} (s) \right] = \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau = \int_ {0} ^ {t} f _ {1} (\tau) f _ {2} (t - \tau) \mathrm{d} \tau$$

在此将 $(sI - A)^{-1}$ 视为 $F_{1}(s)$ ，将 $\pmb{BU}(s)$ 视为 $F_{2}(s)$ ，则有
