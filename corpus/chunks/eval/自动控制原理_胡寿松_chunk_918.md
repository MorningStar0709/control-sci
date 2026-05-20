$$
\left[ \begin{array}{c} \dot {\boldsymbol {x}} _ {o} \\ \dot {\boldsymbol {x}} _ {o} \end{array} \right] = \left[ \begin{array}{c c} \overline {{\boldsymbol {A}}} _ {1 1} & \overline {{\boldsymbol {A}}} _ {1 2} \\ \boldsymbol {0} & \overline {{\boldsymbol {A}}} _ {2 2} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {x} _ {o} \\ \boldsymbol {x} _ {o} \end{array} \right] + \left[ \begin{array}{c} \overline {{\boldsymbol {B}}} _ {1} \\ \overline {{\boldsymbol {B}}} _ {2} \end{array} \right] \boldsymbol {u}, \quad \boldsymbol {y} = [ \overline {{\boldsymbol {C}}} _ {1} \quad \boldsymbol {0} ] \left[ \begin{array}{c} \boldsymbol {x} _ {o} \\ \boldsymbol {x} _ {o} \end{array} \right]
$$

式中，可观测子系统动态方程为

$$\dot {\boldsymbol {x}} _ {o} = \overline {{{\boldsymbol {A}}}} _ {2 2} \boldsymbol {x} _ {o} + \overline {{{\boldsymbol {B}}}} _ {2} \boldsymbol {u}, \boldsymbol {y} _ {2} = \boldsymbol {0}$$

不可观测子系统动态方程为

$$\dot {\boldsymbol {x}} _ {o} = \bar {\boldsymbol {A}} _ {1 1} \boldsymbol {x} _ {o} + \bar {\boldsymbol {A}} _ {1 2} \boldsymbol {x} _ {o} + \bar {\boldsymbol {B}} _ {1} \boldsymbol {u}, \boldsymbol {y} _ {1} = \bar {\boldsymbol {C}} _ {1} \boldsymbol {x} _ {o} = \boldsymbol {y}$$

命令格式： $[Ac,Bc,Cc,T] = \mathrm{ctrbf}(A,B,C)$

$$[ \mathrm{Ao}, \mathrm{Bo}, \mathrm{Co}, \mathrm{T} ] = \text { o b s v f } (\mathrm{A}, \mathrm{B}, \mathrm{C})$$

其中，Ac, Bc, Cc 为可控性分解后的系数矩阵；Ao, Bo, Co 为可观测性分解后的系数矩阵；T 为变换矩阵。
