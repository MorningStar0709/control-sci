$$\boldsymbol {x} (t) = \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {x} (0) + \int_ {0} ^ {t} \mathrm{e} ^ {\boldsymbol {A} (t - \tau)} \boldsymbol {B u} (\tau) \mathrm{d} \tau = \boldsymbol {\Phi} (t) \boldsymbol {x} (0) + \int_ {0} ^ {t} \boldsymbol {\Phi} (t - \tau) \boldsymbol {B u} (\tau) \mathrm{d} \tau$$

结果与式(9-43)相同。上式又可表示为

$$\boldsymbol {x} (t) = \boldsymbol {\Phi} (t) \boldsymbol {x} (0) + \int_ {0} ^ {t} \boldsymbol {\Phi} (\tau) \boldsymbol {B u} (t - \tau) \mathrm{d} \tau \tag {9-45}$$

有时利用式(9-45)求解更为方便。

例 9-5 系统状态方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u
$$

且 $\boldsymbol{x}(0)=[x_{1}(0)\quad x_{2}(0)]^{\mathrm{T}}$ 。试求在 $u(t)=1(t)$ 作用下状态方程的解。

解 由于 $u(t) = 1, u(t - \tau) = 1$ ，根据式(9-45)可得

$$\boldsymbol {x} (t) = \boldsymbol {\Phi} (t) \boldsymbol {x} (0) + \int_ {0} ^ {t} \boldsymbol {\Phi} (\tau) \boldsymbol {B} \mathrm{d} \tau$$

由例9-4已求得

$$
\boldsymbol {\Phi} (t) = \left[ \begin{array}{c c} 2 \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} & \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} \\ - 2 \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} & - \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} \end{array} \right]

\begin{array}{l} \int_ {0} ^ {t} \boldsymbol {\Phi} (\tau) \boldsymbol {B} \mathrm{d} \tau = \int_ {0} ^ {t} \left[ \begin{array}{c} \mathrm{e} ^ {- \tau} - \mathrm{e} ^ {- 2 \tau} \\ - \mathrm{e} ^ {- \tau} + 2 \mathrm{e} ^ {- 2 \tau} \end{array} \right] \mathrm{d} \tau = \left[ \begin{array}{c} - \mathrm{e} ^ {- \tau} + \frac {1}{2} \mathrm{e} ^ {- 2 \tau} \\ \mathrm{e} ^ {- \tau} - \mathrm{e} ^ {- 2 \tau} \end{array} \right] \Bigg | _ {0} ^ {t} \\ = \left[ \begin{array}{c} - \mathrm{e} ^ {- t} + \frac {1}{2} \mathrm{e} ^ {- 2 t} + \frac {1}{2} \\ \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

故 $\boldsymbol{x}(t)=\begin{bmatrix}x_{1}(t)\\x_{2}(t)\end{bmatrix}=\begin{bmatrix}2e^{-t}-e^{-2t}&e^{-t}-e^{-2t}\\-2e^{-t}+2e^{-2t}&-e^{-t}+2e^{-2t}\end{bmatrix}\begin{bmatrix}x_{1}(0)\\x_{2}(0)\end{bmatrix}$

$$
+ \left[ \begin{array}{c} - \mathrm{e} ^ {- t} + \frac {1}{2} \mathrm{e} ^ {- 2 t} + \frac {1}{2} \\ \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} \end{array} \right]
$$
