# 1.6.1 已知系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) + u _ {1} (t), \\ \dot {x} _ {2} (t) = 2 x _ {1} (t) + u _ {2} (t), \\ y (t) = x _ {1} (t) - x _ {2} (t). \end{array} \right.
$$

证明：在状态反馈

$$
\left\{ \begin{array}{l} u _ {1} (t) = - 2 x _ {2} (t) + v _ {1} (t), \\ u _ {2} (t) = - 3 x _ {1} (t) + v _ {2} (t), \end{array} \right.
$$

下，闭环系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = - x _ {2} (t) + v _ {1} (t) \\ \dot {x} _ {2} (t) = - x _ {1} (t) + v _ {2} (t) \\ y (t) = x _ {1} (t) - x _ {2} (t) \end{array} \right.
$$

是能控的，但不能观测.

1.6.2 证明定理 1.6.2.

1.6.3 设系统

$$\dot {x} = A x + B u$$

是能控的．证明：对任意的 T > 0，状态反馈控制

$$u = - B ^ {T} W ^ {- 1} (0, T) x$$

使闭环系统

$$\dot {\boldsymbol {x}} = \left[ \boldsymbol {A} - \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {W} ^ {- 1} (\boldsymbol {0}, \boldsymbol {T}) \right] \boldsymbol {x}$$

具有稳定极点. 这里,

$$\boldsymbol {W} (0, \boldsymbol {T}) = \int_ {0} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} (\mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B}) ^ {\mathrm{T}} \mathrm{d} t.$$
