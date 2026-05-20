| Real Axis | Imag Axis |
| --- | --- |
| -8.0 | 0.0 |
| -7.0 | 0.0 |
| -6.0 | 0.0 |
| -5.0 | 0.0 |
| -4.0 | 0.0 |
| -3.0 | 0.0 |
| -2.0 | 0.0 |
| -1.0 | 1.0 |
| -0.5 | 2.0 |
| 0.0 | 3.0 |
| 0.5 | 4.0 |
| 1.0 | 5.0 |
| 1.5 | 4.5 |
| 1.8 | 4.0 |
| 1.9 | 3.5 |
| 1.95 | 3.0 |
| 1.98 | 2.5 |
| 1.99 | 2.0 |
| 1.995 | 1.5 |
| 1.998 | 1.0 |
| 1.999 | 0.5 |
| 1.9995 | 0.0 |
| 1.9998 | -0.5 |
| 1.9999 | -1.0 |
| 1.99995 | -1.5 |
| 1.99998 | -2.0 |
| 1.99999 | -2.5 |
| 1.999995 | -3.0 |
| 1.999998 | -3.5 |
| 1.999999 | -4.0 |
| 1.9999995 | -4.5 |
| 1.9999998 | -5.0 |
</details>

A–6–11. Obtain the transfer function of the mechanical system shown in Figure 6–74. Assume that the displacement $x _ { i }$ is the input and displacement $x _ { o }$ is the output of the system.

Solution. From the diagram we obtain the following equations of motion:

![](image/ff1f0f9b04b656cbe3b5b6b97b376f2fda640ccaa02a181f0253d84b1112e7bd.jpg)

<details>
<summary>text_image</summary>

b₂
xᵢ
b₁
xₒ
k
y
</details>

Figure 6–74 Mechanical system.

$$b _ {2} \left(\dot {x} _ {i} - \dot {x} _ {o}\right) = b _ {1} \left(\dot {x} _ {o} - \dot {y}\right)b _ {1} \left(\dot {x} _ {o} - \dot {y}\right) = k y$$

Taking the Laplace transforms of these two equations, assuming zero initial conditions, and then eliminating $Y ( s )$ , we obtain

$$\frac {X _ {o} (s)}{X _ {i} (s)} = \frac {b _ {2}}{b _ {1} + b _ {2}} \frac {\frac {b _ {1}}{k} s + 1}{\frac {b _ {2}}{b _ {1} + b _ {2}} \frac {b _ {1}}{k} s + 1}$$

This is the transfer function between $X _ { o } ( s )$ and $X _ { i } ( s )$ By defining.

$$\frac {b _ {1}}{k} = T, \quad \frac {b _ {2}}{b _ {1} + b _ {2}} = \alpha < 1$$

we obtain

$$\frac {X _ {o} (s)}{X _ {i} (s)} = \alpha \frac {T s + 1}{\alpha T s + 1} = \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}}$$

This mechanical system is a mechanical lead network.

A–6–12. Obtain the transfer function of the mechanical system shown in Figure 6–75.Assume that the displacement $x _ { i }$ is the input and displacement $x _ { o }$ is the output.

![](image/8c07c2e58e3e211a82fe59018e62e8eca6a69c014d6945dd9cc1073af14ea899.jpg)

<details>
<summary>text_image</summary>

b₂
k₂
xᵢ
b₁
xₒ
k₁
y
</details>

Figure 6–75 Mechanical system.

Solution. The equations of motion for this system are

$$b _ {2} \left(\dot {x} _ {i} - \dot {x} _ {o}\right) + k _ {2} \left(x _ {i} - x _ {o}\right) = b _ {1} \left(\dot {x} _ {o} - \dot {y}\right)b _ {1} \left(\dot {x} _ {o} - \dot {y}\right) = k _ {1} y$$

By taking the Laplace transforms of these two equations, assuming zero initial conditions, we obtain
