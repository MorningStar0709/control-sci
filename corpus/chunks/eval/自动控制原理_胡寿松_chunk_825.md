# (2) 里卡蒂方程解的若干性质

在式(10-97)中，令反馈增益矩阵

$$\boldsymbol {K} (t) = \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathbf {T}} (t) \boldsymbol {P} (t) \tag {10-110}$$

则最优控制可表示为

$$\boldsymbol {u} ^ {*} (t) = - \boldsymbol {K} (t) \boldsymbol {x} (t) \tag {10-111}$$

将上式代入式(10-96)，得最优闭环系统方程

$$\dot {\boldsymbol {x}} (t) = [ \boldsymbol {A} (t) - \boldsymbol {B} (t) \boldsymbol {K} (t) ] \boldsymbol {x} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-112}$$

因为矩阵 $A(t)$ , $B(t)$ 及 $R(t)$ 已知, 故闭环系统的性质与 $K(t)$ 密切相关, 而 $K(t)$ 的性质又取决于里卡蒂方程(10-99)在边界条件(10-100)下的解 $P(t)$ 。

1) $P(t)$ 是唯一的。矩阵 $P(t)$ 是里卡蒂方程(10-99)在边界条件(10-100)下的解。而方程(10-99)实质上是 $n(n + 1) / 2$ 个非线性标量微分方程组，当矩阵 $\mathbf{A}(t),\mathbf{B}(t),\mathbf{R}(t)$ 和 $Q(t)$ 满足问题10-2的假设条件时，根据微分方程理论中解的存在性与唯一性定理知，在区间 $[t_0,t_f]$ 上， $P(t)$ 唯一存在。
