# 5. 非线性微分方程的线性化

严格地说, 实际物理元件或系统都是非线性的。例如, 弹簧的刚度与其形变有关系, 因此弹簧系数 K 实际上是其位移 x 的函数, 而非常值; 电阻、电容、电感等参数值与周围环境(温度、湿度、压力等)及流经它们的电流有关, 也非常值; 电动机本身的摩擦、死区等非线性因素会使其运

动方程复杂化而成为非线性方程。当然，在一定条件下，为了简化数学模型，可以忽略它们的影响，将这些元件视为线性元件，这就是通常使用的一种线性化方法。此外，还有一种线性化方法，称为切线法或小偏差法，这种线性化方法特别适合于具有连续变化的非线性特性函数，其实质是在一个很小的范围内，将非线性特性用一段直线来代替，具体方法如下所述。

设连续变化的非线性函数为 $y = f(x)$ ，如图2-6所示。取某平衡状态 $A$ 为工作点，对应有 $y_0 = f(x_0)$ 。当 $x = x_0 + \Delta x$ 时，有 $y = y_0 + \Delta y$ 。设函数 $y = f(x)$ 在$(x_{0},y_{0})$ 点连续可微，则将它在该点附近用泰勒级数展开为

![](image/7497ac8f55a78a5500f42f6262da89b6f7720727f737641e2471fbe14bdf4d98.jpg)

<details>
<summary>line</summary>

| x | y = f(x) |
| --- | --- |
| 0 | y₀ |
| x₀ | y₀ |
</details>

图 2-6 小偏差线性化示意图

$$y = f (x) = f \left(x _ {0}\right) + \left(\frac {\mathrm{d} f (x)}{\mathrm{d} x}\right) _ {x _ {0}} \left(x - x _ {0}\right) + \frac {1}{2 !} \left(\frac {\mathrm{d} ^ {2} f (x)}{\mathrm{d} x ^ {2}}\right) _ {x _ {0}} \left(x - x _ {0}\right) ^ {2} + \dots$$

当增量 $x - x_0$ 很小时，略去其高次幂项，则有

$$y - y _ {0} = f (x) - f \left(x _ {0}\right) = \left(\frac {\mathrm{d} f (x)}{\mathrm{d} x}\right) _ {x _ {0}} \left(x - x _ {0}\right)$$

令 $\Delta y = y - y_0 = f(x) - f(x_0),\Delta x = x - x_0,K = (\mathrm{df}(x) / \mathrm{dx})_{x_0}$ ，则线性化方程可简记为 $\Delta y = K\Delta x$ 。略去增量符号 $\Delta$ ，便得函数 $y = f(x)$ 在工作点A附近的线性化方程为 $y = Kx$ 。式中， $K = (\mathrm{df}(x) / \mathrm{dx})_{x_0}$ 是比例系数，它是函数 $f(x)$ 在A点的切线斜率。

对于有两个自变量 $x_{1}, x_{2}$ 的非线性函数 $f(x_{1}, x_{2})$ ，同样可在某工作点 $(x_{10}, x_{20})$ 附近用泰勒级数展开为

$$
\begin{array}{l} y = f \left(x _ {1}, x _ {2}\right) = f \left(x _ {1 0}, x _ {2 0}\right) + \left[ \left(\frac {\partial f}{\partial x _ {1}}\right) _ {x _ {1 0}, x _ {2 0}} \left(x _ {1} - x _ {1 0}\right) + \left(\frac {\partial f}{\partial x _ {2}}\right) _ {x _ {1 0}, x _ {2 0}} \left(x _ {2} - x _ {2 0}\right) \right] \\ + \frac {1}{2 !} \left[ \left(\frac {\partial^ {2} f}{\partial x _ {1} ^ {2}}\right) _ {x _ {1 0}, x _ {2 0}} (x _ {1} - x _ {1 0}) ^ {2} + 2 \left(\frac {\partial^ {2} f}{\partial x _ {1} \partial x _ {2}}\right) _ {x _ {1 0}, x _ {2 0}} (x _ {1} - x _ {1 0}) (x _ {2} - x _ {2 0}) \right. \\ \end{array}
\left. + \left(\frac {\partial^ {2} f}{\partial x _ {2} ^ {2}}\right) _ {x _ {1 0}, x _ {2 0}} (x _ {2} - x _ {2 0}) ^ {2} \right] + \dots
$$

略去二阶以上导数项，并令 $\Delta y = y - f(x_{10}, x_{20}), \Delta x_1 = x_1 - x_{10}, \Delta x_2 = x_2 - x_{20}$ ，可得增量线性化方程
