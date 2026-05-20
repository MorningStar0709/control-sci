(2) 在区间 $[t, t + \Delta t]$ 上，以 $x^{*}(t)$ 为初值按 $(u^{*}(s), \bar{v})$ 进行对策，则有

$$\dot {\bar {x}} (s) = f (\bar {x} (s), u ^ {*} (s), \bar {v}), \quad s \in [ t, t + \Delta t ], \quad \bar {x} (t) = x ^ {*} (t).$$

其对策值为 $\int_{t}^{t + \Delta t}l(\bar{x} (s),u^{*}(s),\bar{v})\mathrm{d}s,$ 并且

$$\bar {x} (t + \Delta t) = x ^ {*} (t) + \int_ {t} ^ {t + \Delta t} f (\bar {x} (s), u ^ {*} (s), \bar {v}) \mathrm{d} s;$$

(3) 在区间 $[t + \Delta t, t_f]$ 上，以 $\bar{x}(t + \Delta t)$ 为初值按最优方式进行对策，其最优对策过程为 $(u_1^*(s), v_1^*(t), x_1^*(t))$ ，即

$$\dot {x} _ {1} ^ {*} (s) = f \left(x _ {1} ^ {*} (s), u _ {1} ^ {*} (s), v _ {1} ^ {*} (s)\right), \quad s \in [ t + \Delta t, t _ {f} ], \quad x _ {1} ^ {*} (t + \Delta t) = \bar {x} (t + \Delta t),$$

其对策值为

$$J ^ {*} (x _ {1} ^ {*} (t + \Delta t), t + \Delta t) \stackrel {\text { def }} {=} J [ u _ {1} ^ {*}, v _ {1} ^ {*} ] = \int_ {t + \Delta t} ^ {t _ {f}} l (x _ {1} ^ {*} (s), u _ {1} ^ {*} (s), v _ {1} ^ {*} (s)) d s.$$

而若在区间 $[t + \Delta t, t_f]$ 上，以 $\bar{x}(t + \Delta t)$ 为初值，按 $(u^{*}(t), v_{1}^{*}(t))$ 进行对策时，则有

$$\dot {x} _ {1} (s) = f \left(x _ {1} (s), u ^ {*} (s), v _ {1} ^ {*} (s)\right), \quad s \in [ t + \Delta t, t _ {f} ], \quad x _ {1} (t + \Delta t) = \bar {x} (t + \Delta t),$$

其对策值为

$$J [ u ^ {*}, v _ {1} ^ {*} ] = \int_ {t + \Delta t} ^ {t _ {f}} l (x _ {1} (s), u ^ {*} (s), v _ {1} ^ {*} (s)) \mathrm{d} s.$$

这时显然有

$$J ^ {*} (x _ {1} ^ {*} (t + \Delta t), t + \Delta t) \leqslant \int_ {t + \Delta t} ^ {t _ {f}} l (x _ {1} (s), u ^ {*} (s), v _ {1} ^ {*} (s)) \mathrm{d} s. \tag {7.4.36}$$

令

$$
\tilde {v} (s) \stackrel {\mathrm{def}} {=} \left\{ \begin{array}{l l} {v ^ {*} (s),} & {\text {当} s \in [ 0, t) \text {时},} \\ {\bar {v},} & {\text {当} s \in [ t, t + \Delta t) \text {时},} \\ {v _ {1} ^ {*} (s),} & {\text {当} s \in [ t + \Delta t, t _ {f} ] \text {时}.} \end{array} \right.
$$

在区间 $[0, t_f]$ 上，系统 (7.4.30) 以 $x(0) = x_0$ 为初值，按 $(u^*(s), \tilde{v}(s))$ 进行对策时，相应的轨线 $\tilde{x}(s)$ 为

$$
\tilde {x} (s) = \left\{ \begin{array}{l l} {x ^ {*} (s),} & {\text {当} s \in [ 0, t) \text {时},} \\ {\bar {x} (s),} & {\text {当} s \in [ t, t + \Delta t) \text {时},} \\ {x _ {1} (s),} & {\text {当} s \in [ t + \Delta t, t _ {f} ] \text {时},} \end{array} \right.
$$

而其对策值为

$$
\begin{array}{l} J [ u ^ {*}, \tilde {v} ] = \int_ {0} ^ {t} l (x ^ {*} (s), u ^ {*} (s), v ^ {*} (s)) \mathrm{d} s + \int_ {t} ^ {t + \Delta t} l (\bar {x} (s), u ^ {*} (s), \bar {v}) \mathrm{d} s \\ + \int_ {t + \Delta t} ^ {t _ {f}} l (x _ {1} (s), u ^ {*} (s), v _ {1} ^ {*} (s)) d s. \\ \end{array}
$$

我们有
