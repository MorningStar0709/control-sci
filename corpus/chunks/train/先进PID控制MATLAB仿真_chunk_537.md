$$\dot {E} _ {1} = - \mathrm{EIy} _ {x x x} (L) \dot {z} (L) - \mathrm{EIy} _ {x x} (0) \dot {\theta}\dot {E} _ {2} = I _ {\mathrm{h}} \dot {e} \ddot {e} + k _ {\mathrm{p}} e \dot {e} + M _ {\mathrm{t}} \dot {z} (L) \ddot {z} (L) = \dot {e} \left(I _ {\mathrm{h}} \ddot {e} + k _ {\mathrm{p}} e\right) + \dot {z} (L) m \ddot {z} (L)$$

则

$$
\begin{array}{l} \dot {V} = \dot {E} _ {1} + \dot {E} _ {2} \\ = - \mathrm{EI} y _ {x x x} (L) \dot {z} (L) - \mathrm{EI} y _ {x x} (0) \dot {\theta} + \dot {e} \left(I _ {\mathrm{h}} \ddot {e} + k _ {\mathrm{p}} e\right) + \dot {z} (L) m \ddot {z} (L) \\ = \dot {e} \left(I _ {\mathrm{h}} \cdot \frac {1}{I _ {\mathrm{h}}} (\tau + \operatorname{EIy} _ {x x} (0)) + k _ {\mathrm{p}} e - \operatorname{EIy} _ {x x} (0)\right) + \dot {z} (L) \left(- \operatorname{EIy} _ {x x x} (L) + m \frac {1}{m} (\operatorname{EIy} _ {x x x} (L) + F)\right) \\ = \dot {e} (\tau + k _ {\mathrm{p}} e) + \dot {z} (L, t) F \\ \end{array}
$$

设计控制律为

$$\tau = - k _ {\mathrm{p}} e - k _ {\mathrm{d}} \dot {e} \tag {13.44}F = - k \dot {z} (L) \tag {13.45}$$

式中， $k_{p}>0$ ； $k_{d}>0$ ；k>0；F为边界控制，则

$$\dot {V} = - k _ {\mathrm{d}} \dot {e} ^ {2} - k \dot {z} ^ {2} (L) \leqslant 0$$

将闭环系统进行空间转换，采用半群和紧凑性分析方法，可证明本闭环系统的稳定性分析可采用无穷维 LaSalle 不变集定理方法 $^{[10]}$ 。

下面针对在 $\dot{V}\equiv0$ 条件下进行闭环系统的收敛性分析：

当 $\dot{V} \equiv 0$ 时，有 $\dot{e} \equiv \dot{z}(L) \equiv 0$ ， $\ddot{e} \equiv \ddot{z}(L) \equiv 0$ 。由于 $\theta_{\mathrm{d}}$ 为常数，则 $\dot{\theta} \equiv 0$ ， $\ddot{\theta} \equiv 0$ ，代入式 $\rho(x\ddot{\theta} + \ddot{y}(x)) = \rho\ddot{z}(x) = -\mathrm{EI}y_{xxxx}(x)$ 中，可得

$$\rho \ddot {y} (x) = - \operatorname{EI} y _ {x x x x} (x),\rho \ddot {z} (L) = - \operatorname{EIy} _ {x x x x} (L) = 0$$

从而 $y_{xxx}(L)=0$ 。

根据变量分离技术 $^{[11]}$ ，可取

$$y (x) = X (x) \cdot T (t) \tag {13.46}$$

式中， $X(x)$ 和 $T(t)$ 都是未知函数。

由式 $\rho\ddot{y}(x,t)=-\mathrm{EI}y_{xxxx}(x,t)$ 可得

$$y _ {x x x x} (x) = - \frac {\rho}{E I} \ddot {y} (x)$$

由式（13.46）可知 $y_{xxxx}(x) = X^{(4)}(x)\cdot T(t), - \ddot{y} (x) = X(x)\cdot T^{(2)}(t)$ ，代入上式，则

$$\frac {X ^ {(4)} (x)}{X (x)} = - \frac {\rho}{\mathrm{EI}} \frac {T ^ {(2)} (t)}{T (t)} = \mu$$

即

$$X ^ {(4)} (x) - \mu X (x) = 0$$

取 $\mu = \beta^4$ ，求解上式，可得

$$X (x) = c _ {1} \cosh \beta x + c _ {2} \sinh \beta x + c _ {3} \cos \beta x + c _ {4} \sin \beta x \tag {13.47}$$

式中， $c_{i}\in R,\ i=1,2,3,4$ 为未知实数。

由于 $y(0)=0,\quad y_{x}(0)=0,\quad y_{xx}(L)=0$ ，考虑 $y_{xxxx}(L)=0$ ，结合式（13.46），可得 $X(0)=X'(0)=X''(L)=X^{(4)}(L)=0$ ，则由式（13.47）可得
