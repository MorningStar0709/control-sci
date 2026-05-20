$$
L _ {d} \bigg (y - \left[ \begin{array}{c c} C & C _ {d} \end{array} \right] \left[ \begin{array}{c} \hat {x} \\ \hat {d} \end{array} \right] \bigg) = 0
$$

But notice this condition merely restricts the output prediction error to lie in the nullspace of the matrix $L _ { d }$ , which is an $n _ { d } \times p$ matrix. If we choose $n _ { d } = n _ { c } < p$ , then the number of columns of $L _ { d }$ is greater than the number of rows and $L _ { d }$ has a nonzero nullspace.8 In general, we require the output prediction error to be zero to achieve zero offset independently of the regulator tuning. For $L _ { d }$ to have only the zero vector in its nullspace, we require $n _ { d } \geq p$ . Since we also know $n _ { d } \leq p$ from Corollary 1.9, we conclude $n _ { d } = p$ .

![](image/510e5a5b3314b34490788e8d2f62bdd8f3215c8d0b56b866cba2bd266889f61a.jpg)

<details>
<summary>text_image</summary>

F₀, T₀, c₀
Tc
h
r
F
T, c
</details>

Figure 1.6: Schematic of the well-stirred reactor.

<table><tr><td>Parameter</td><td>Nominal value</td><td>Units</td></tr><tr><td> $F_0$ </td><td>0.1</td><td>m3/min</td></tr><tr><td> $T_0$ </td><td>350</td><td>K</td></tr><tr><td> $c_0$ </td><td>1</td><td>kmol/m3</td></tr><tr><td>r</td><td>0.219</td><td>m</td></tr><tr><td> $k_0$ </td><td>7.2 × 1010</td><td>min-1</td></tr><tr><td>E/R</td><td>8750</td><td>K</td></tr><tr><td>U</td><td>54.94</td><td>kJ/min·m2·K</td></tr><tr><td>ρ</td><td>1000</td><td>kg/m3</td></tr><tr><td> $C_p$ </td><td>0.239</td><td>kJ/kg·K</td></tr><tr><td>ΔH</td><td>-5 × 104</td><td>kJ/kmol</td></tr></table>

Table 1.1: Parameters of the well-stirred reactor.
