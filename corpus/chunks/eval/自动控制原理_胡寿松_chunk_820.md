# (2) 输出调节器问题

对于系统方程(10-92)和性能指标(10-93)，如果理想输出向量 $z(t)=0$ ，则有 $e(t)=-y(t)$ 。从而，性能指标(10-93)演变为

$$J = \frac {1}{2} \mathbf {y} ^ {\mathrm{T}} (t _ {f}) \mathbf {F} \mathbf {y} (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} [ \mathbf {y} ^ {\mathrm{T}} (t) \mathbf {Q} (t) \mathbf {y} (t) + \mathbf {u} ^ {\mathrm{T}} (t) \mathbf {R} (t) \mathbf {u} (t) ] \mathrm{d} t \tag {10-95}$$

这时，线性二次型最优控制问题为：当系统(10-92)受扰偏离原输出平衡状态时，要求产生一控制向量，使系统输出 $y(t)$ 保持在原零平衡状态附近，并使性能指标(10-95)极小。因而，称为输出调节器问题。
