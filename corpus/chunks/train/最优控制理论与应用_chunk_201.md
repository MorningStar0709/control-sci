式中， $r_{p}$ 、 $r_{e}$ 分别为导弹与目标的位置向量； $v_{p}$ 、 $v_{e}$ 分别为导弹与目标的速度向量； $a_{p}$ 、 $a_{e}$ 分别为到导弹与目标的控制加速度向量； $f_{p}$ 、 $f_{e}$ 分别为导弹与目标的固有加速度，它们是由重力和气动力引起的，通常可认为 $f_{p}=f_{e}$ 。两维情况下导弹与目标的几何关系可用图10-6表示。图中pe连线称为视线，q称为视线角。考虑性能指标

$$
\begin{array}{l} J \left(\boldsymbol {a} _ {\mathrm{p}}, \boldsymbol {a} _ {\mathrm{e}}\right) = \frac {k}{2} \left[ \boldsymbol {r} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {r} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] ^ {\mathrm{T}} \left[ \boldsymbol {r} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {r} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] + \\ \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {c} _ {\mathrm{p}} \boldsymbol {a} _ {\mathrm{p}} ^ {\mathrm{T}} (t) \boldsymbol {a} _ {\mathrm{p}} (t) - \boldsymbol {c} _ {\mathrm{e}} \boldsymbol {a} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \boldsymbol {a} _ {\mathrm{e}} (t) \right] \mathrm{d} t \tag {10-111} \\ \end{array}
$$

这是一个线性二次微分对策问题。利用本节的结果可求解为下：

因为我们仅对相对运动 $r_{\mathrm{p}}(t) - r_{\mathrm{e}}(t)$ 感兴趣，故可忽略 $f_{\mathrm{p}}, f_{\mathrm{e}}$ 。定义 $\pmb{x}_{\mathrm{p}} = \begin{bmatrix} \pmb{r}_{\mathrm{p}} \\ \pmb{v}_{\mathrm{p}} \end{bmatrix}, \pmb{x}_{\mathrm{e}} = \begin{bmatrix} r_{\mathrm{e}} \\ v_{\mathrm{e}} \end{bmatrix}$ ，由式（10-109）、（10-110）可得出系统矩阵和控制矩阵为

$$
\boldsymbol {A} _ {\mathrm{p}} (t) = \boldsymbol {A} _ {\mathrm{e}} (t) = \left[ \begin{array}{l l} \boldsymbol {O} _ {3} & \boldsymbol {I} _ {3} \\ \boldsymbol {O} _ {3} & \boldsymbol {O} _ {3} \end{array} \right] \tag {10-112}

\boldsymbol {B} _ {\mathrm{p}} (t) = \boldsymbol {B} _ {\mathrm{e}} (t) = \left[ \begin{array}{l} \boldsymbol {O} _ {3} \\ \boldsymbol {I} _ {3} \end{array} \right]
$$

于是

$$
\boldsymbol {\Phi} _ {\mathrm{p}} \left(t _ {\mathrm{f}} - t\right) = \boldsymbol {\Phi} _ {\mathrm{e}} \left(t _ {\mathrm{f}} - t\right) = \left[ \begin{array}{c c} \boldsymbol {I} _ {3} & \left(t _ {\mathrm{f}} - t\right) \boldsymbol {I} _ {3} \\ \boldsymbol {O} _ {3} & \boldsymbol {I} _ {3} \end{array} \right] \tag {10-113}
$$

因为性能指标式(10-108)中
