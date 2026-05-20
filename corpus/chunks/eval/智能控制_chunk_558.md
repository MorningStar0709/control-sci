# 11.5.1 系统描述

Arimoto 等人 $^{[25]}$ 给出了线性时变连续系统

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t) + \boldsymbol {B} (t) \boldsymbol {u} (t) \\ \boldsymbol {y} (t) = \boldsymbol {C} (t) \boldsymbol {x} (t) \end{array} \right. \tag {11.13}
$$

的开环 PID 型迭代学习控制律为

$$\pmb {u} _ {k + 1} (t) = \pmb {u} _ {k} (t) + \Big (\pmb {\Gamma} \frac {\mathrm{d}}{\mathrm{d} t} + \pmb {L} + \pmb {\Psi} \int \mathrm{d} t \Big) \pmb {e} _ {k} (t) \tag {11.14}$$

式中， $\Gamma,L,\Psi$ 为学习增益矩阵。
