# 5.6.1 系统描述

机器人的动态方程为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) = \tau \tag {5.67}$$

式中， $D(q)$ 为惯性力矩， $C(q,\dot{q})$ 是向心力和哥氏力， $G(q)$ 是重力项， $F(q,\dot{q},\ddot{q})$ 是由摩擦 $F_{r}$ 、扰动 $\tau_{d}$ 、负载变化的不确定项组成的。
