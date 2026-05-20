# 5.1.3 两个线性跟踪微分器来改造的“线性PID”

在算法(5.1.11)中的非线性跟踪微分器改换成线性跟踪微分器来改造上述PID算法得

$$
\left\{ \begin{array}{l} \mathrm{fh} = - r _ {0} \left(r _ {0} \left(v _ {1} - v\right) + \sqrt {3} v _ {2}\right) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \\ \mathrm{fh} = - r _ {1} \left(r _ {1} \left(z _ {1} - v\right) + \sqrt {3} z _ {2}\right) \\ z _ {1} = z _ {1} + h z _ {2} \\ z _ {2} = z _ {2} + h \mathrm{fh} \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2}, e _ {0} = \int_ {0} ^ {t} e _ {1} (\tau) d \tau \\ u = \beta_ {0} e _ {0} + \beta_ {1} e _ {1} + \beta_ {2} e _ {2} \end{array} \right. \tag {5.1.13}
$$

现在取参数 $r_0 = 1.0, r_1 = 100$ ，误差反馈增益取成 $\beta_0 = 30, \beta_1 = 50, \beta_2 = 20$ 时，不稳定对象（5.1.12）的控制效果显示于图5.1.6.

![](image/b4e92bdd3f14d428b749846150bc7760d7a739f47ed9ac74b29c4142536af6fa.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1 |
| 2 | 1 |
| 4 | 1 |
| 6 | 1 |
| 8 | 1 |
| 10 | 1 |
| 12 | 1 |
| 14 | 1 |
| 16 | 1 |
| 18 | 1 |
| 20 | 1 |

The chart displays two labeled segments: v₁ and u. The x-axis ranges from 0 to 20, and the y-axis ranges from 0 to 3. The function value is defined as r₀ = 2, r₁ = 100, h₀ = h₁ = h, β₀ = 30, β₁ = 50, β₂ = 20. The function value is calculated as f = x₁ + x₂ + sign(sin(t/2)).
</details>

图5.1.6
