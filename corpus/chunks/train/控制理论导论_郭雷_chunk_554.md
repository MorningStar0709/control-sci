# 定量微分对策问题

最优控制问题处理的是对系统施加控制，使它从一个状态转移到某目标集，并使某性能指标达到极小，这可视为单方控制问题。定量微分对策问题处理双方控制问题，即系统中有甲，乙两方，双方都有刻划各自动态特征的状态方程，各自的控制和目标集，虽有共同的性能指标，但各自的控制目标不同，甲方施加控制欲使性能指标取极小，而乙方施加控制欲使性能指标取极大。令 $x_{z}, x_{d}$ 和 $u, v$ 分别是甲，乙方的状态变量和控制变量。甲方的状态方程，控制约束，目标集分别为

$$\dot {x} _ {z} = f _ {z} (x _ {z}, u, t), \quad x _ {z} (t _ {0}) = x _ {z _ {0}}, \tag {7.4.1}u \in \mathbb {U} _ {r _ {1}} \subseteq \mathbb {R} ^ {r _ {1}}, \tag {7.4.2}\mathcal {S} _ {z} \stackrel {\text { def }} {=} \left\{x _ {z} \mid g _ {z} (x _ {z}, t _ {f}) = 0 \right\}, \tag {7.4.3}$$

性能指标为

$$J [ u, v ] = k (x _ {z} (t _ {f}), x _ {d} (t _ {f}), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} l (x _ {z} (t), x _ {d} (t), u (t), v (t), t) \mathrm{d} t. \tag {7.4.4}$$

乙方的状态方程，控制约束和目标集分别为

$$\dot {x} _ {d} = f _ {d} (x _ {d}, v, t), \quad x _ {d} (t _ {0}) = x _ {d 0}, \tag {7.4.5}v \in \mathbb {V} _ {r _ {2}} \subseteq \mathbb {R} ^ {r _ {2}}, \tag {7.4.6}\mathcal {S} _ {d} \stackrel {\text { def }} {=} \left\{x _ {d} \mid g _ {d} (x _ {d}, t _ {f}) = 0 \right\}. \tag {7.4.7}$$

上列诸式中， $x_{z}, x_{d}, u, v$ 皆为适当维数的向量， $f_{z}, f_{d}, g_{z}, g_{d}$ 皆为相应维数的向量值函数，且它们使式(7.4.1)，(7.4.5)的解在所论区间上存在唯一。 $k$ 和 $l$ 为标量函数．下面引入记号 $x = \left[x_{z}^{\mathrm{T}}, x_{d}^{\mathrm{T}}\right]^{\mathrm{T}}$ ， $x(t_0) = \left[x_{z}^{\mathrm{T}}(t_0), x_{d}^{\mathrm{T}}(t_0)\right]^{\mathrm{T}} = x_0$ ， $f(x, u, v, t) = \left[f_{z}^{\mathrm{T}}(x_{z}, u, t), f_{d}^{\mathrm{T}}(x_{d}, v, t)\right]^{\mathrm{T}}$ ， $g(x(t_f), t_f) = \left[g_{z}^{\mathrm{T}}(x_{z}(t_f), t_f), g_{d}^{\mathrm{T}}(x_{d}(t_f), t_f)\right]^{\mathrm{T}}$ ．于是定量微分对策问题可的状态方程，初始条件，目标集，性能指标表示为

$$\dot {x} = f (x, u, v), \quad x \left(t _ {0}\right) = x _ {0}, \tag {7.4.8}(u, v) \in \mathbb {U} _ {r _ {1}} \times \mathbb {V} _ {r _ {2}} \subseteq \mathbb {R} ^ {r _ {1}} \times \mathbb {R} ^ {r _ {2}}, \tag {7.4.9}S \stackrel {\text { def }} {=} \left\{x \mid g (x, t _ {f}), t _ {f}\right) = 0 \}, \tag {7.4.10}J [ u, v ] = k (x (t _ {f}), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} l (x (t), u (t), v (t), t) \mathrm{d} t, \tag {7.4.11}$$
