# 9.9.1 问题的提出

设 n 关节机械手方程为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\dot {\boldsymbol {q}}) + \tau_ {\mathrm{d}} = \tau \tag {9.64}$$

式中， $D(q)$ 为 $n \times n$ 阶正定惯性矩阵， $C(q, \dot{q})$ 为 $n \times n$ 阶惯性矩阵， $G(q)$ 为 $n \times 1$ 阶惯性向量， $F(\ddot{q})$ 为摩擦力， $\tau_{d}$ 为未知外加干扰， $\tau$ 为控制输入。

跟踪误差为

$$\boldsymbol {e} (t) = \boldsymbol {q} _ {\mathrm{d}} (t) - \boldsymbol {q} (t)$$

定义误差函数为

$$\boldsymbol {r} = \dot {\boldsymbol {e}} + \boldsymbol {\Lambda} \boldsymbol {e} \tag {9.65}$$

式中， $\Lambda=\Lambda^{T}>0$ ，则当 $r\rightarrow0$ 时， $e\rightarrow0,\dot{e}\rightarrow0$ 。

由于 $\dot{q}=-r+\dot{q}_{d}+\Lambda e$

则

$$
\begin{array}{l} \boldsymbol {D} \dot {\boldsymbol {r}} = \boldsymbol {D} \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \ddot {\boldsymbol {q}} + \boldsymbol {\Lambda} \dot {\boldsymbol {e}}\right) = \boldsymbol {D} \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} + \boldsymbol {\Lambda} \dot {\boldsymbol {e}}\right) - \boldsymbol {D} \ddot {\boldsymbol {q}} \\ = D \left(\ddot {q} _ {\mathrm{d}} + \Lambda \dot {e}\right) + C \dot {q} + G + F + \tau_ {\mathrm{d}} - \tau \\ = D \left(\ddot {q} _ {\mathrm{d}} + \Lambda \dot {e}\right) - C r + C \left(\dot {q} _ {\mathrm{d}} + \Lambda e\right) + G + F + \tau_ {\mathrm{d}} - \tau \\ = - \boldsymbol {C r} - \tau + f + \tau_ {\mathrm{d}} \tag {9.66} \\ \end{array}
$$

式中， $f(x)=D(\ddot{q}_{\mathrm{d}}+\Lambda\dot{e})+C(\dot{q}_{\mathrm{d}}+\Lambda e)+G+F$ 。

在实际工程中,模型不确定项 f 为未知,为此,需要对不确定项 f 进行逼近。采用 RBF 网络逼近 f,根据 $f(x)$ 的表达式,网络输入取

$$
\boldsymbol {x} = \left[ \begin{array}{l l l l l} \boldsymbol {e} ^ {\mathrm{T}} & \dot {\boldsymbol {e}} ^ {\mathrm{T}} & \boldsymbol {q} _ {\mathrm{d}} ^ {\mathrm{T}} & \dot {\boldsymbol {q}} _ {\mathrm{d}} ^ {\mathrm{T}} & \ddot {\boldsymbol {q}} _ {\mathrm{d}} ^ {\mathrm{T}} \end{array} \right]
$$

设计控制律为

$$\boldsymbol {\tau} = \hat {\boldsymbol {f}} + \mathbf {K} _ {\mathrm{v}} \boldsymbol {r} \tag {9.67}$$

式中， $f(x)$ 为针对 f 进行逼近的 RBF 网络输出值。

将控制律式(9.67)代入式(9.66)，得
