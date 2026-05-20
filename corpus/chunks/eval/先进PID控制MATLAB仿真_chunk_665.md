# 17.7.2 自适应控制律的设计

定义滑模函数为

$$s = \dot {e} + c e = x _ {2} - \dot {x} _ {\mathrm{d}} + c e \tag {17.37}$$

式中， $x_{d}$ 为位置指令； $e=x_{1}-x_{d}$ 为位置跟踪误差；c>0 。则

$$\theta \dot {s} = \theta \left(\dot {x} _ {2} - \ddot {x} _ {\mathrm{d}} + c \dot {e}\right) \tag {17.38}$$

定义 Lyapunov 函数为

$$V = \frac {1}{2} \theta s ^ {2} + \frac {1}{2 \gamma} \tilde {\theta} ^ {2} \tag {17.39}$$

式中， $\tilde{\theta}=\hat{\theta}-\theta;\gamma>0$ 。则

$$\dot {V} = \theta s \dot {s} + \frac {1}{\gamma} \tilde {\theta} \dot {\tilde {\theta}} = s \left(\theta \dot {x} _ {2} - \theta \ddot {x} _ {\mathrm{d}} + \theta c \dot {e}\right) + \frac {1}{\gamma} \tilde {\theta} \dot {\hat {\theta}} \tag {17.40}= s \left(u + \Delta - \theta \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right)\right) + \frac {1}{\gamma} \tilde {\theta} \dot {\hat {\theta}}$$

控制律设计为

$$u = \hat {\theta} \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) - k _ {\mathrm{s}} s - \eta \operatorname{sgn} (s) \tag {17.41}$$

式中， $k_{s}>0$ ； $\eta>D$ ，则

$$
\begin{array}{l} \dot {V} = s \left(\hat {\theta} \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) - k _ {\mathrm{s}} s - \eta \operatorname{sgn} (s) + \Delta - \theta \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right)\right) + \frac {1}{\gamma} \tilde {\theta} \dot {\hat {\theta}} \\ = s \left(\tilde {\theta} \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) - k _ {\mathrm{s}} s - \eta \operatorname{sgn} (s) + \Delta\right) + \frac {1}{\gamma} \tilde {\theta} \dot {\hat {\theta}} \\ = s \left(\tilde {\theta} \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) - k _ {\mathrm{s}} s - \eta \operatorname{sgn} (s) + \Delta\right) + \frac {1}{\gamma} \tilde {\theta} \dot {\hat {\theta}} \\ = - k _ {s} s ^ {2} - \eta | s | + \Delta \cdot s + \tilde {\theta} \left(s \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) + \frac {1}{\gamma} \dot {\hat {\theta}}\right) \\ \end{array}
$$

取自适应律为

$$\dot {\hat {\theta}} = - \gamma s \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right) \tag {17.42}$$

则

$$\dot {V} = - k _ {\mathrm{s}} s ^ {2} - \eta | s | + \Delta \cdot s \leqslant - k _ {\mathrm{s}} s ^ {2} \leqslant 0$$

由于且当且仅当 s=0 时， $\dot{V}=0$ 。即当 $\dot{V}\equiv0$ 时， $s\equiv0$ 。根据 LaSalle 不变性原理 $^{[2]}$ ，闭环系统为渐进稳定，即当 $t\to\infty$ 时， $s\to0$ 。系统的收敛速度取决于 $k_{s}$ 。

由于 $V\geqslant0,\quad\dot{V}\leqslant0$ ，则当 $t\to\infty$ 时，V有界，因此，可以证明 $\hat{\theta}$ 有界，但无法保证 $\hat{\theta}$ 收敛于 $\theta$ 。
