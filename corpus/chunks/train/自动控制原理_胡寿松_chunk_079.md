在零初始条件下，即 $\omega_{m}(0) = \omega_{m}^{\prime}(0) = 0$ 时，对上式各项求拉氏变换，并令 $\Omega_{m}(s) = \mathcal{L}[\omega_{m}(t)]$ $U_{a}(s) = \mathcal{L}[u_{a}(t)]$ ，则得 $s$ 的代数方程为 $(T_{m}s + 1)\Omega_{m}(s) = K_{m}U_{a}(s)$ ，由传递函数定义，于是有

$$G (s) = \frac {\Omega_ {m} (s)}{U _ {a} (s)} = \frac {K _ {m}}{T _ {m} s + 1} \tag {2-39}$$

$G(s)$ 便是电枢电压 $u_{a}(t)$ 到转速 $\omega_{m}(t)$ 的传递函数。令 $u_{a}(t) = 0$ 时，用同样方法可求得负载扰动转矩 $M_{c}(t)$ 到转速的传递函数为

$$G _ {m} (s) = \frac {\Omega_ {m} (s)}{M _ {c} (s)} = \frac {- K _ {2}}{T _ {m} s + 1} \tag {2-40}$$

由式(2-39)和式(2-40)可求得电动机转速 $\omega_{m}(t)$ 在电枢电压 $u_{a}(t)$ 和负载转矩 $M_{c}(t)$ 同时作用下的响应特性为

$$
\begin{array}{l} \omega_ {m} (t) = \mathscr {L} ^ {- 1} [ \Omega_ {m} (s) ] = \mathscr {L} ^ {- 1} \left[ \frac {K _ {m}}{T _ {m} s + 1} U _ {a} (s) - \frac {K _ {c}}{T _ {m} s + 1} M _ {c} (s) \right] \\ = \mathscr {L} ^ {- 1} \left[ \frac {K _ {m}}{T _ {m} s + 1} U _ {a} (s) \right] + \mathscr {L} ^ {- 1} \left[ \frac {- K _ {c}}{T _ {m} s + 1} M _ {c} (s) \right] \\ = \omega_ {1} (t) + \omega_ {2} (t) \\ \end{array}
$$

式中， $\omega_{1}(t)$ 是 $u_{a}(t)$ 作用下的转速特性； $\omega_{2}(t)$ 是 $M_{c}(t)$ 作用下的转速特性。
