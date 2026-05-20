(b) 利用 $V_{0}(\eta) = \frac{(m + M)k_{1}}{2mL}\left(\eta_{1} - \frac{mL}{m + M}\sin \eta_{3}\right)^{2} + \frac{(m + M)^{2}k_{1}}{2kmL}\eta_{2}^{2} + \frac{k_{2}}{2}\eta_{3}^{2}$

其中 $k_{1}$ 和 $k_{2}$ 是正常数，证明

$$\xi = \phi (\eta) \stackrel {\mathrm{def}} {=} k _ {1} \left(\eta_ {1} - \frac {m L}{m + M} \sin \eta_ {3}\right) \cos \eta_ {3} - k _ {2} \eta_ {3}$$

使

$$\dot {\eta} = \eta_ {2}, \quad \dot {\eta} _ {2} = - \frac {k}{m + M} \left(\eta_ {1} - \frac {m L}{m + M} \sin \eta_ {3}\right), \quad \dot {\eta} _ {3} = \xi$$

的原点全局稳定。

验证滑动曲面可取为

$$s = \dot {\theta} + k _ {2} \theta - k _ {1} x _ {c} \cos \theta = 0$$

注意 $s$ 与系统参数无关。

(c) 选择 $\beta(x)$ ，使得当 $\mu$ 足够小时， $u = -\beta(x)\mathrm{sat}(s/\mu)$ 使原点全局稳定。

(d) (c) 中 $\beta(x)$ 的表达式可能比较复杂, 为简化控制律, 取 $\beta$ 为常数, 并把控制律写为

$$u = - \beta \operatorname{sat} \left(\frac {\dot {\theta} + k _ {2} \theta - k _ {1} x _ {c} \cos \theta}{\mu}\right)$$

其中正常数 $k_{1}, k_{2}, \beta$ 和 $\mu$ 都是设计参数。证明对于足够小的 $\mu$ ，该控制律可稳定原点，并保证吸引区包含围绕原点的一个紧集。

(e) 设系统参数与习题 14.56(d) 的参数相同, 通过仿真和局部分析选择设计参数, 以减小稳定时间。通过对闭环系统在原点线性化, 证明闭环特征方程为

$$1 + \gamma_ {0} \frac {s ^ {3} + \gamma_ {1} s ^ {2} + \gamma_ {2} s + \gamma_ {3}}{s ^ {2} (s ^ {2} + \gamma_ {4})} = 0$$

其中

$$\gamma_ {0} = \frac {\beta (m + M)}{\mu \Delta_ {0}}, \quad \gamma_ {1} = k _ {2} + \frac {m L k _ {1}}{m + M}, \quad \gamma_ {2} = \frac {k}{m + M}\gamma_ {3} = \frac {k k _ {2}}{m + M}, \quad \gamma_ {4} = \frac {k (I + m L ^ {2})}{\Delta_ {0}}, \quad \Delta_ {0} = \Delta (0)$$

验证特征多项式是赫尔维茨的,并构造当 $\gamma_{0}$ 从零变化到无穷时的根轨线,把该根轨线与习题 14.56 中得到的根轨线相比较,并讨论 $-k_{1}x_{c}\cos\theta$ 一项在选择 s 时的作用。

(f) 通过对初始状态为 $\theta(0) = \pi, \dot{\theta}(0) = 0, x_c(0) = 0.025$ 和 $\dot{x}_c(0) = 0$ 的闭环系统进行仿真，并利用(e)中的根轨线分析，选择常数 $k_1, k_2, \beta$ 和 $\mu$ ，使系统的稳定时间尽可能短，应能使该稳定时间达到大约 $4\mathrm{~s}$ 。将结果与习题14.56比较。

(g) 现在假设只能测量 $\theta$ 和 $x_{c}$ ，利用 14.5 节中的分析证明，对于足够小的 $\mu$ 和 $\varepsilon$ ，输出反馈控制器

$$u = - \beta \operatorname{sat} \left(\frac {z + k _ {2} \theta - k _ {1} x _ {c} \cos \theta}{\mu}\right)$$

使原点稳定,其中 z 是传递函数 $s/(\varepsilon s+1)$ 的输出, $\theta$ 是其驱动,该传递函数即为降阶高增益观测器的传递函数。验证当 $\varepsilon$ 趋于零时,输出反馈控制器可重现状态反馈控制器的性能。当 $\varepsilon$ 取不同值时,对闭环系统进行仿真,并与状态反馈控制下的性能进行比较。
