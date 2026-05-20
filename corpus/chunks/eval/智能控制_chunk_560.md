$$\boldsymbol {e} _ {k + 1} (t) = \boldsymbol {e} _ {k} (t) - \int_ {0} ^ {t} \boldsymbol {C} (t) \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \left[ \boldsymbol {\Gamma} (\tau) \dot {\boldsymbol {e}} _ {k} (\tau) + \boldsymbol {L} (\tau) \boldsymbol {e} _ {k} (\tau) + \psi (\tau) \int_ {0} ^ {\tau} \boldsymbol {e} _ {k} (\delta) \mathrm{d} \delta \right] \mathrm{d} \tau \tag {11.15}$$

利用分部积分公式，令 $G(t,\tau) = C(t)B(\tau)\Gamma (\tau)$ ，有

$$
\begin{array}{l} \int_ {0} ^ {t} \boldsymbol {C} (t) \boldsymbol {B} (\tau) \boldsymbol {\Gamma} (\tau) \dot {\boldsymbol {e}} _ {k} (\tau) \mathrm{d} \tau = \boldsymbol {G} (t, \tau) \boldsymbol {e} _ {k} (\tau) \Big | _ {0} ^ {t} - \int_ {0} ^ {t} \frac {\partial}{\partial \tau} \boldsymbol {G} (t, \tau) \boldsymbol {e} _ {k} (\tau) \mathrm{d} \tau \\ = \boldsymbol {C} (t) \boldsymbol {B} (\tau) \boldsymbol {\Gamma} (\tau) \boldsymbol {e} _ {k} (\tau) - \int_ {0} ^ {t} \frac {\partial}{\partial \tau} \boldsymbol {G} (t, \tau) \boldsymbol {e} _ {k} (\tau) \mathrm{d} \tau \tag {11.16} \\ \end{array}
$$

将式(11.16)代入式(11.15)，得

$$
\begin{array}{l} \boldsymbol {e} _ {k + 1} (t) = [ \boldsymbol {I} - \boldsymbol {C} (t) \boldsymbol {B} (t) \boldsymbol {\Gamma} (t) ] \boldsymbol {e} _ {k} (t) + \int_ {0} ^ {t} \frac {\partial}{\partial \tau} \boldsymbol {G} (t, \tau) \boldsymbol {e} _ {k} (\tau) d \tau - \\ \int_ {0} ^ {t} \boldsymbol {C} (t) \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \boldsymbol {L} (\tau) \boldsymbol {e} _ {k} (\tau) \mathrm{d} \tau - \int_ {0} ^ {t} \int_ {0} ^ {\tau} \boldsymbol {C} (t) \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \psi (\tau) \boldsymbol {e} _ {k} (\sigma) \mathrm{d} \sigma \mathrm{d} \tau \tag {11.17} \\ \end{array}
$$

将式(11.17)两端取范数,有
