# 11.4.1 控制器设计

考虑一个 $N$ 关节的机器人, 其动态性能可以由以下二阶非线性微分方程描述

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) = \tau - \tau_ {\mathrm{d}} \tag {11.9}$$

式中， $q\in R^n$ 为关节角位移量， $D(q)\in R^{n\times n}$ 为机器人的惯性矩阵， $C(\pmb {q},\dot{\pmb{q}})\in R^n$ 表示离心力和哥氏力， $G(q)\in R^n$ 为重力项， $\tau \in R^n$ 为控制力矩， $\pmb{\tau}_{\mathrm{d}}\in R^{n}$ 为各种误差和扰动。

设系统所要跟踪的期望轨迹为 $\mathbf{y}_{\mathrm{d}}(t), t \in [0, T]$ 。系统第 k 次输出为 $\mathbf{y}_{k}(t)$ ，令 $\mathbf{e}_{k}(t) = \mathbf{y}_{\mathrm{d}}(t) - \mathbf{y}_{k}(t)$ 。

在学习开始时,系统的初始状态为 $x_{0}(0)$ 。学习控制的任务为通过学习控制律设计 $\boldsymbol{u}_{k+1}(t)$ ，使第 $k+1$ 次运动误差 $\boldsymbol{e}_{k+1}(t)$ 减少。

采用 3 种基于反馈的迭代学习控制律。

(1) 闭环 D 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \mathbf {K} _ {\mathrm{d}} (\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)) \tag {11.10}$$

(2) 闭环 PD 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \mathbf {K} _ {\mathrm{p}} \left(\boldsymbol {q} _ {\mathrm{d}} (t) - \boldsymbol {q} _ {k + 1} (t)\right) + \mathbf {K} _ {\mathrm{d}} \left(\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)\right) \tag {11.11}$$

(3) 指数变增益闭环 D 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {K} _ {\mathrm{d}} (\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)) \tag {11.12}$$

式中， $K_{d}$ 以指数形式变化。

本书只给出上述3种控制律的仿真实现方法，未讨论控制律的收敛性。
