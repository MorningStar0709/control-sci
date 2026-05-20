14.56 考虑习题 1.16 的 TORA 系统。本题要求设计一个基于无源的控制律 [146]，以全局稳定原点。

(a) 用势能 $(1/2)kx_{c}^{2}$ 与动能 $(1/2)v^{\mathrm{T}}D(\theta)v$ 之和作为存储函数, 其中 $v = [\dot{\theta}, \dot{x}_{c}]^{\mathrm{T}}$ 。证明该输入为 $u$ , 输出为 $\dot{\theta}$ 的系统是无源的。该系统是零状态可观测的吗?

(b) 设 $u = -\phi_{1}(\theta) + w$ ，其中 $\phi_{1}$ 是局部利普希茨的， $\phi_{1}(0) = 0$ ，且对于所有 $y \neq 0$ ，有 $y \phi_{1}(y) > 0$ 和 $\lim_{|y| \to \infty} \int_{0}^{y} \phi_{1}(\lambda) d\lambda = \infty$ 。用

$$
V = \frac {1}{2} v ^ {\mathrm{T}} D (\theta) v + \frac {1}{2} k x _ {c} ^ {2} + \int_ {0} ^ {\theta} \phi_ {1} (\lambda) d \lambda , \quad v = \left[ \begin{array}{l} \dot {\theta} \\ \dot {x} _ {c} \end{array} \right]
$$

作为存储函数,证明该输入为 w, 输出为 $\dot{\theta}$ 的系统是无源的,并证明系统是零状态可观测的。

(c) 设 $\phi_{2}$ 是任意局部利普希茨函数, 满足 $\phi_{2}(0)=0$ , 且对于所有 $y\neq0$ , 有 $y\phi_{2}(y)>0$ 。

证明 $u = -\phi_{1}(\theta) - \phi_{2}(\dot{\theta})$ 使原点全局稳定。

(d) 设 M=1.3608 Kg, m=0.096 Kg, L=0.0592 m, I=0.000 217 5 K gm $^{2}$ , k=186.3 N/m。
验证对正常数 $U_{P}, U_{v}, K_{p}$ 和 $K_{v}$ ,

$$u = - U _ {p} \operatorname{sat} (K _ {p} \theta) - U _ {v} \operatorname{sat} (K _ {v} \dot {\theta})$$

是全局稳定的。选择 $U_{P}$ 和 $U_{v}$ 满足 $U_{P} + U_{v} \leqslant 0.1$ ，以保证 $u$ 满足约束 $|u| \leqslant 0.1$ 。我们想要设计这四个参数，以减小稳定时间。本题要求用仿真和局部分析选择这些参数。通过在原点对闭环系统线性化，证明闭环特征方程为

$$1 + \beta_ {0} \frac {(s ^ {2} + \beta_ {2}) (s + \beta_ {1})}{s ^ {2} (s ^ {2} + \beta_ {3})} = 0$$

其中 $\beta_0 = \frac{U_vK_v(m + M)}{\Delta_0},\beta_1 = \frac{U_pK_p}{U_vK_v},\beta_2 = \frac{k}{m + M},\beta_3 = \frac{k(I + mL^2)}{\Delta_0}$

且 $\Delta_{0}=\Delta(0)$ ，验证特征多项式是赫尔维茨的，并构造当 $\beta_{0}$ 从零变化到无穷时的根轨线。

(e) 对初始状态为 $\theta(0)=\pi,\dot{\theta}(0)=0,x_{c}(0)=0.025$ 和 $\dot{x}_{c}(0)=0$ 的闭环系统进行仿真，并利用(d)中的根轨线分析，选择常数 $U_{P},U_{v},K_{p}$ 和 $K_{v}$ ，使系统的稳定时间尽可能短，使该稳定时间大约达到 30 s。

(f) 现在假设只能测量 $\theta$ ，利用习题 14.48 证明输出反馈控制器

$$u = - U _ {p} \operatorname{sat} (K _ {p} \theta) - U _ {v} \operatorname{sat} (K _ {v} z)$$

可使原点全局稳定,其中 z 是传递函数 $s/(\varepsilon s + 1)$ 的输出,该传递函数由 $\theta$ 驱动, $\varepsilon$ 是任意正常数。将该传递函数作为降阶高增益观测器的传递函数,利用 14.5 节的分析,证明当 $\varepsilon$ 趋于零时,输出反馈控制器可重现状态反馈控制器的性能。当 $\varepsilon$ 取不同值时,对闭环系统进行仿真,并与状态反馈控制下的性能进行比较。

14.57 考虑习题 1.16 中的 TORA 系统。本题将设计一个滑模控制器 $^{①}$ 以稳定原点。

(a) 证明变量代换

$$\eta_ {1} = x _ {c} + \frac {m L \sin \theta}{m + M}, \quad \eta_ {2} = \dot {x} _ {c} + \frac {m L \dot {\theta} \cos \theta}{m + M}, \quad \eta_ {3} = \theta , \quad \xi = \dot {\theta}$$

使系统转换为式(14.4)和式(14.5)的规则形式。
