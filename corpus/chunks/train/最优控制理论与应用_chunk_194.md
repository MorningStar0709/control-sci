p 方选择 $\boldsymbol{u}(t)$ 使 $J(\boldsymbol{u},\boldsymbol{v})$ 达到极小，而 e 方选择 $\boldsymbol{v}(t)$ 使 $J(\boldsymbol{u},\boldsymbol{v})$ 达到极大。上述问题称为线性二次微分对策问题。为了求解此问题，首先从 p、e 双方的状态方程获得他们之间的相对运动方程。定义相对运动 $\boldsymbol{x}(t)$ 为

$$\boldsymbol {x} (t) = \boldsymbol {F} \left[ \boldsymbol {\Phi} _ {\mathrm{p}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {x} _ {\mathrm{p}} (t) - \boldsymbol {\Phi} _ {\mathrm{e}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {x} _ {\mathrm{e}} (t) \right] \tag {10-94}$$

其中， $F$ 是性能指标中的加权阵的因子， $\Phi_{\mathrm{p}}(t_{\mathrm{f}},t)$ 和 $\Phi_{\mathrm{e}}(t_{\mathrm{f}},t)$ 分别为 $A_{\mathrm{p}}(t)$ 和 $A_{\mathrm{e}}(t)$ 的基本解阵，故满足

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} \boldsymbol {\Phi} _ {\mathrm{p}} \left(t _ {\mathrm{f}} , t\right)}{\mathrm{d} t} = - \boldsymbol {\Phi} _ {\mathrm{p}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {A} _ {\mathrm{p}} (t) \\ \frac {\mathrm{d} \boldsymbol {\Phi} _ {\mathrm{e}} \left(t _ {\mathrm{f}} , t\right)}{\mathrm{d} t} = - \boldsymbol {\Phi} _ {\mathrm{e}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {A} _ {\mathrm{e}} (t) \end{array} \right. \tag {10-95}
$$

式(10-94)对 $t$ 求导, 并注意到状态方程式(10-88)和(10-89)以及式(10-94), 可得

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {u} (t) - \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {v} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-96}$$

式中，

$$
\left\{ \begin{array}{l} \boldsymbol {G} _ {\mathrm{p}} (t) = \boldsymbol {F} \boldsymbol {\Phi} _ {\mathrm{p}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {B} _ {\mathrm{p}} (t) \\ \boldsymbol {G} _ {\mathrm{e}} (t) = \boldsymbol {F} \boldsymbol {\Phi} _ {\mathrm{e}} \left(t _ {\mathrm{f}}, t\right) \boldsymbol {B} _ {\mathrm{e}} (t) \end{array} \right. \tag {10-97}
$$

于是,性能指标可变为

$$J (\boldsymbol {u}, \boldsymbol {v}) = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {x} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{p}} (t) \boldsymbol {u} (t) -\left. \boldsymbol {v} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{e}} (t) \boldsymbol {v} (t) \right] \mathrm{d} t \tag {10-98}$$

下面来求解此线性二次微分对策问题。为此引入哈密顿函数 $H$
