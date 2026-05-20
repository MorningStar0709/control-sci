# 4. 变分法解最优控制问题

在控制向量不受约束，且是时间的连续函数情况下，可用变分法导出最优控制解的必要条件。在变分法问题中，以复合型指标泛函、末端受约束的情况最有代表性。

设系统状态方程为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t), \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0} \tag {10-40}$$

性能指标泛函为

$$J = \varphi [ \pmb {x} (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} L (\pmb {x}, \pmb {u}, t) \mathrm{d} t \tag {10-41}$$

式中， $x \in R^{n}$ ; $u \in R^{m}$ ，无约束，且在 $[t_{0}, t_{f}]$ 上连续；在 $[t_{0}, t_{f}]$ 上，向量函数 $f(\cdot)$ 、标量函数 $\varphi(\cdot)$ 和 $L(\cdot)$ 连续且可微；末端时刻 $t_{f}$ 可以固定，也可以自由；末端状态 $x(t_{f})$ 受约束，其要求的目标集为

$$\psi [ \boldsymbol {x} (t _ {f}), t _ {f} ] = \mathbf {0} \tag {10-42}$$

其中 $\psi \in \mathbb{R}^r, r \leqslant n$ 。最优控制问题是: 确定最优控制 $u^*(t)$ 和最优轨线 $x^*(t)$ , 使系统(10-40)由已知初态 $x_0$ 转移到要求的目标集(10-42), 并使给定的指标泛函(10-41)达到极值。

显然,上述问题是一个有等式约束的泛函极值问题,可以采用拉格朗日乘子法,把有约束泛函极值问题化为无约束泛函极值问题。构造哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {\lambda}, t) = L (\boldsymbol {x}, \boldsymbol {u}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t) \tag {10-43}$$

式中， $\lambda \in \mathbf{R}^n$ 为拉格朗日乘子向量。则最优解的必要条件可以分别讨论如下。
