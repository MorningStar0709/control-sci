# 7.3.1 问题的提出

设 $n$ 关节机械手方程为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) = \tau - d (\dot {\boldsymbol {q}}) \tag {7.9}$$

式中， $D(q)$ 为 $n \times n$ 阶正定惯性矩阵； $C(q, \dot{q})$ 为 $n \times n$ 阶离心和哥氏力项； $G(q)$ 为 $n \times 1$ 阶重力项； $d(\dot{q})$ 为摩擦力矩。

在实际控制中， $D(q)$ 、 $C(q,\dot{q})$ 和 $G(q)$ 为未知，取

$$\boldsymbol {D} (\boldsymbol {q}) = \boldsymbol {D} _ {0} (\boldsymbol {q}) + \boldsymbol {E} _ {\mathrm{D}}\boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) + \boldsymbol {E} _ {\mathrm{C}}\boldsymbol {G} (\boldsymbol {q}) = \boldsymbol {G} _ {0} (\boldsymbol {q}) + \boldsymbol {E} _ {\mathrm{G}}$$

式中， $E_{D}$ 、 $E_{C}$ 和 $E_{G}$ 分别为 $D(q)$ 、 $C(q,\dot{q})$ 和 $G(q)$ 的建模误差，则

$$D (q) \ddot {q} _ {\mathrm{r}} + C (q, \dot {q}) \dot {q} _ {\mathrm{r}} + G (q) \tag {7.10}= \boldsymbol {D} _ {0} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) + \boldsymbol {E} _ {\mathrm{M}}$$

式中， $E_{M}=E_{D}\ddot{q}_{r}+E_{C}\dot{q}_{r}+E_{G}$ 。

![](image/fc70b3b0f12c49b63c02cc680f7dd4af91d2762a9c85a1b76365c503ec5f6a81.jpg)
