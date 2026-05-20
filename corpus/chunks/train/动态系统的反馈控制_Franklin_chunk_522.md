# 7.10.3节习题

△7.62 考虑希望跟踪一个斜坡参考输入的伺服机构问题，被控对象和理想模型方程如下：

$$
\dot {x} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 1 \end{array} \right] x + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] x

\dot {\boldsymbol {x}} _ {\mathrm{m}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} _ {\mathrm{m}}

y _ {\mathrm{m}} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] x _ {\mathrm{m}}
$$

设计一个模型跟踪控制律并证明其跟踪性能。将闭环极点配置到 $s = -2 \pm j2$ 上。

△7.63 假设希望闭环系统的表现与一个期望模型相似，该期望模型称为隐式模型：

$$\dot {z} = A _ {\mathrm{m}} z$$

可以最小化线性二次调节器的性能指标：

$$\mathcal {J} = \int_ {0} ^ {+ \infty} \left\{\left(\dot {y} - A _ {\mathrm{m}} y\right) ^ {\mathrm{T}} Q _ {1} \left(\dot {y} - A _ {\mathrm{m}} y\right) + u ^ {\mathrm{T}} R u \right\} \mathrm{d} t$$

证明此性能指标等价于标准的 LQR 性能指标加上一个控制和状态形式的交叉权重项：

$$\mathcal {J} = \int_ {0} ^ {+ \infty} \left\{\boldsymbol {x} ^ {\mathrm{T}} \hat {\boldsymbol {Q}} \boldsymbol {x} + 2 u ^ {\mathrm{T}} \hat {\boldsymbol {S}} \boldsymbol {x} + u ^ {\mathrm{T}} \hat {\boldsymbol {R}} u \right\} \mathrm{d} t$$

其中：

$$\hat {Q} = \left(\boldsymbol {C A} - \boldsymbol {A} _ {\mathrm{m}} \boldsymbol {C}\right) ^ {\mathrm{T}} Q _ {1} \left(\boldsymbol {C A} - \boldsymbol {A} _ {\mathrm{m}} \boldsymbol {C}\right)\hat {\boldsymbol {S}} = \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {Q} _ {1} (\boldsymbol {C A} - \boldsymbol {A} _ {\mathrm{m}} \boldsymbol {C})\hat {\boldsymbol {R}} = \boldsymbol {R} + \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {Q} _ {1} \boldsymbol {C B}$$

△7.64 在显式模型跟踪中，假设在 LQR 问题中，我们期望闭环系统的表现尽可能的接近形如下式的系统：

$$\dot {z} = A _ {\mathrm{m}} z$$

这代表了理想的动力学模型。我们选择一个形如下式的性能指标：

$$\mathcal {J} = \int_ {0} ^ {+ \infty} \left\{\left(y - z\right) ^ {\mathrm{T}} Q _ {1} (y - z) + u ^ {\mathrm{T}} R u \right\} \mathrm{d} t$$

(a) 证明该性能指标可以通过扩展被控对象和模型的状态转化为标准的性能指标。选择增广状态变量 $\xi = [x^{T} z^{T}]^{T}$ 并写下系统方程来验证：

$$\mathcal {J} = \int_ {0} ^ {+ \infty} \left\{\boldsymbol {\xi} ^ {\mathrm{T}} Q _ {1} \boldsymbol {\xi} + \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R u} \right\} \mathrm{d} t$$

其中：

$$
Q = \left[ \begin{array}{c c} C ^ {\mathrm{T}} Q _ {1} C & - C ^ {\mathrm{T}} Q _ {1} \\ - Q _ {1} C & Q _ {1} \end{array} \right]
$$

(b) 系统的哪个状态变量是不可控的？结果是否令人惊讶？

(c) 最优控制的形式：

$$u = - K _ {1} x - K _ {2} z$$

意味着模型的方程必须作为控制律的一部分来实现。假设控制的模型如下式：
