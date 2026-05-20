# (1) 状态调节器问题

在系统方程(10-92)和二次型性能指标(10-93)中,如果 $C(t)=I,z(t)=0$ ,则有

$$\pmb {e} (t) = - \pmb {y} (t) = - \pmb {x} (t)$$

从而性能指标(10-93)演变为

$$J = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} (t _ {f}) \boldsymbol {F} \boldsymbol {x} (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {u} (t) ] \mathrm{d} t \tag {10-94}$$

这时，线性二次型最优控制问题为：当系统(10-92)受扰偏离原零平衡状态时，要求产生一控制向量，使系统状态 $x(t)$ 恢复到原平衡状态附近，并使性能指标(10-94)极小。因而，称为状态调节器问题。
