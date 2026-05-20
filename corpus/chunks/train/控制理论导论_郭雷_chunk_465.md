$$\frac {\partial V}{\partial x} f (x) + \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g (x) g ^ {T} (x) \frac {\partial^ {T} V}{\partial x} + \frac {1}{2} h ^ {T} (x) h (x) \leqslant \frac {1}{2} \left\| \gamma^ {- 1} g ^ {T} (x) \frac {\partial^ {T} V}{\partial x} - \gamma u \right\| ^ {2}. \tag {6.7.8}$$

因此当 $u = \gamma^{-2}g^{\mathbf{T}}(x)\frac{\partial^{\mathbf{T}}V}{\partial x}$ 时，不等式(6.7.5)成立.

现在我们来证明 $\gamma-$ 耗散性与 $L^{2}$ 增益条件的等价性.

定义6.7.3 设系统(6.7.1)对应于初始状态 $x(0) = x_0$ 和输入 $u$ 的解为 $x(t) = \psi (t,x_0,u)$ . 给定初始状态 $x_0$ , 若对于任意 $x_{1}$ , 一定存在 $t_1\geqslant 0$ 和 $u_{1}(t)$ 使得

$$x _ {1} = x (t _ {1}) = \psi (t _ {1}, x _ {0}, u _ {1}),$$

则称该系统在状态 $x_0$ 是能达的.

定理 6.7.2 设系统 (6.7.1) 在原点 $x_{0}=0$ 是能达的，并且对于任意给定的 $t_{0}\geqslant0$ ，如下定义的函数 $V(x)$ ：

$$
V (x) = - \lim _ {T \rightarrow \infty} \inf _ {\substack {u \in L ^ {2} (t _ {0}, T)\\x (t _ {0}) = x}} \frac {1}{2} \int_ {t _ {0}} ^ {T} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) d t \tag{6.7.9}
$$

存在且可微，则该系统是 $\gamma-$ 耗散的充分必要条件是该系统具有小于 $\gamma$ 的 $L^2$ 增益.

证明 如前所述，必要性显然成立，下面证明充分性．设系统(6.7.1)具有小于 $\gamma$ 的 $L_{2}$ 增益．由于该系统原点是能达的，所以对于任意给定的 $x\in \mathbf{R}^n$ ，一定存在 $t_0\geqslant 0$ 和输入信号 $u_{0}(t)(t\in [0,t_{0}])$ 使得

$$x = \psi (t _ {0}, 0, u _ {0}).$$

因此对于如下定义的任意输入信号：

$$
u (t) = \left\{ \begin{array}{l l} u _ {0} (t), & 0 \leqslant t \leqslant t _ {0}, \\ v (t), & t _ {0} <   t \leqslant T, \end{array} \right. \tag {6.7.10}
$$

其中 $v \in L^2[t_0, T]$ 是任意信号，有

$$\int_ {0} ^ {\mathrm{T}} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) \mathrm{d} t \geqslant 0. \tag {6.7.11}$$

即

$$\int_ {0} ^ {t _ {0}} \left(\gamma^ {2} \| u _ {0} \| ^ {2} - \| y \| ^ {2}\right) \mathrm{d} t + \int_ {t _ {0}} ^ {\mathrm{T}} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) \geqslant 0, \quad \forall T \geqslant t _ {0}. \tag {6.7.12}$$

因此

$$- \frac {1}{2} \int_ {t _ {0}} ^ {\mathrm{T}} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) \leqslant \frac {1}{2} \int_ {0} ^ {t _ {0}} (\gamma^ {2} \| u _ {0} \| ^ {2} - \| y \| ^ {2}) \mathrm{d} t < \infty . \tag {6.7.13}$$

上式表明，由式(6.7.9)定义的 $V(x)$ 是有界的，且 $V(x) \geqslant 0$ 。又因为当 $x_0 = 0$ 时可取 $t_0 = 0$ ，所以 $V(0) = 0$ 。

同时，若考虑在状态方程 $\dot{x}=f(x)+g(x)u$ 约束下的如下最优化问题：

$$
\Phi (x) = \inf_ {\substack {u \in L ^ {2} [ t _ {0}, T ] \\ x (t _ {0}) = x}} \frac {1}{2} \int_ {t _ {0}} ^ {\mathbf {T}} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) \mathrm{d} t, \tag{6.7.14}
$$

那么根据最优化理论 [1] 可知，其最优值函数 $\Phi(x(t), t)$ 满足
