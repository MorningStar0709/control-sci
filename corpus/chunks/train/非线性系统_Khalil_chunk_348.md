11. 19 对于奇异扰动系统 $\dot{x} = -x^{3} + \arctan (z)$ , $\varepsilon \dot{z} = -x - z$

重复习题 11.16。在(c)中设 $x(0) = -1, z(0) = 2$ ，且时间区间为 $[0, 2]$ 。

11.20 对于奇异扰动系统

$$\dot {x} = - x + z _ {1} + z _ {2} + z _ {1} z _ {2}, \quad \varepsilon \dot {z} _ {1} = - z _ {1}, \quad \varepsilon \dot {z} _ {2} = - z _ {2} - (x + z _ {1} + x z _ {1})$$

重复习题11.16。在(c)中设 $x(0) = z_{1}(0) = z_{2}(0) = 1$ ，且时间区间为[0,2]。

11.21 考虑习题 1.17 的场控直流电机, 设 $v_{a}=V_{a}$ , 为常数, $v_{f}=U$ , 为常数。

(a) 证明系统有唯一的平衡点

$$I _ {f} = \frac {U}{R _ {f}}, \quad I _ {a} = \frac {c _ {3} V _ {a}}{c _ {3} R _ {a} + c _ {1} c _ {2} U ^ {2} / R _ {f} ^ {2}}, \quad \Omega = \frac {c _ {2} V _ {a} U / R _ {f}}{c _ {3} R _ {a} + c _ {1} c _ {2} U ^ {2} / R _ {f} ^ {2}}$$

我们将用 $(I_{f},I_{a},\Omega)$ 作为标称工作点。

(b) 典型的电枢电路时间常数 $T_{a}=L_{a}/R_{a}$ 比励磁电路时间常数 $T_{f}=L_{f}/R_{f}$ 和机械时间常数小得多, 因此系统可由奇异扰动系统建模, 其中以 $i_{f}$ 和 $\omega$ 作为慢变量, 以 $i_{a}$ 作为快变量。取 $x_{1}=i_{f}/I_{f}, x_{2}=\omega/\Omega, z=i_{a}/I_{a}, u=v_{f}/U, \varepsilon=T_{a}/T_{f}$ , 并用 $t'=t/T_{f}$ 作为时间变量。证明奇异扰动模型是

$$\dot {x} _ {1} = - x _ {1} + u, \quad \dot {x} _ {2} = a (x _ {1} z - x _ {2}), \quad \varepsilon \dot {z} = - z - b x _ {1} x _ {2} + c$$

其中 $a = L_{f}c_{3}/R_{f}J, b = c_{1}c_{2}U^{2}/c_{3}R_{a}R_{f}^{2}, c = V_{a}/I_{a}R_{a}, (\cdot)$ 表示对 $t'$ 的导数。

(c) 求降阶模型和边界层模型。

(d) 分析边界层模型的稳定性。

(e) 求出关于 x 和 z 的 $O(\varepsilon)$ 逼近。

(f) 研究逼近在无限时间区间上的有效性。

(g) 若系统输入 u 为单位阶跃函数,且在时间区间 [0,10] 上的初始状态为零,运用数值算法计算当 $\varepsilon = 0.2$ 和 $\varepsilon = 0.1$ 时的精确解和近似解。已知数值数据 $c_{1} = c_{2} = \sqrt{2} \times 10^{-2} \, N \cdot m / A$ , $c_{3} = 6 \times 10^{-6} \, N \cdot m \cdot s / rad$ , $J = 10^{-6} \, N \cdot m \cdot s^{2} / rad$ , $R_{a} = R_{f} = 1 \, \Omega$ , $L_{f} = 0.2 \, H$ , $V_{a} = 1 \, V$ 和 U = 0.2 V。

11.22 （见文献[105]）考虑奇异扰动系统

$$\dot {x} = - \eta (x) + a z, \qquad \varepsilon \dot {z} = - \frac {x}{a} - z$$

其中 a 是正常数, $\eta$ 是一个光滑非线性函数, 且对于 b > 0 满足

$$\eta (0) = 0, \quad x \eta (x) > 0, \quad x \in (- \infty , b) - \{0 \}$$

用奇异扰动法研究当 $\varepsilon$ 较小时原点的稳定性。

11.23 （见文献[105]）奇异扰动系统 $\dot{x} = -2x^{3} + z^{2},$ $\varepsilon \dot{z} = x^3 -\tan z$

在原点有一个孤立平衡点。

(a) 证明用线性化不能证明原点的渐近稳定性。

(b) 用奇异扰动法证明, 对于 $\varepsilon \in (0, \varepsilon^{*})$ , 原点是渐近稳定的。估计 $\varepsilon^{*}$ 及吸引区。

11.24 （见文献[105]）设 $\psi_{1}(x) = \| x\| ,\psi_{2}(y) = \| y\|$ 时，定理11.3的假设条件成立，并假设 $\forall (x,y)\in D_x\times D_y$ ，存在 $V(x)$ 和 $W(x,y)$ ，满足

$$k _ {1} \| x \| ^ {2} \leqslant V (x) \leqslant k _ {2} \| x \| ^ {2}k _ {3} \| y \| ^ {2} \leqslant W (x, y) \leqslant k _ {4} \| y \| ^ {2}$$
