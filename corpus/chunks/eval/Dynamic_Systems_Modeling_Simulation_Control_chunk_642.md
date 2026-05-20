# Mathematical Model

As we have seen throughout this textbook, developing an appropriate mathematical model is always the first step in analysis and design of dynamic systems. We developed the mathematical modeling equations of the seat-suspension system in Chapter 2, which are

$$m _ {1} \ddot {z} _ {1} + b _ {1} \dot {z} _ {1} + b _ {2} (\dot {z} _ {1} - \dot {z} _ {2}) + k _ {1} z _ {1} + k _ {2} (z _ {1} - z _ {2}) = b _ {1} \dot {z} _ {0} (t) + k _ {1} z _ {0} (t) \tag {11.1a}m _ {2} \ddot {z} _ {2} + b _ {2} (\dot {z} _ {2} - \dot {z} _ {1}) + k _ {2} (z _ {2} - z _ {1}) = 0 \tag {11.1b}$$

Because we assumed ideal damping and stiffness elements, the system is linear. A state-space representation (SSR) approach is likely best suited for system analysis as the two second-order linear ordinary differential equations (ODEs) are coupled, which presents a challenge to developing transfer functions. In Chapter 5 we derived the SSR, which is composed of the state equation

![](image/64fe159a288999edd2c39cc8b7e77fc7b3b18ec86b62643dc943c4de7753d428.jpg)

<details>
<summary>text_image</summary>

Driver mass, m₂
Seat mass, m₁
z₂ Driver displacement
k₂ b₂
z₁ Seat displacement
k₁ b₁
Seat suspension
z₀(t) Cabin floor displacement
</details>

(a)

![](image/fa920e3debb62ee05295d24edca6c608aef67aaab01f974f9c2b0b7ee2bb100c.jpg)

<details>
<summary>text_image</summary>

Driver mass
m₂
k₂
b₂
Seat mass
m₁
k₁
b₁
z₂
z₁
z₀(t)
</details>

(b)   
Figure 11.1 (a) Schematic diagram of the seat-suspension system and (b) mechanical model for the seat-suspension system.

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - \left(k _ {1} + k _ {2}\right) / m _ {1} & - \left(b _ {1} + b _ {2}\right) / m _ {1} & k _ {2} / m _ {1} & b _ {2} / m _ {1} \\ 0 & 0 & 0 & 1 \\ k _ {2} / m _ {2} & b _ {2} / m _ {2} & - k _ {2} / m _ {2} & - b _ {2} / m _ {2} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} 0 & 0 \\ k _ {1} / m _ {1} & b _ {1} / m _ {1} \\ 0 & 0 \\ 0 & 0 \end{array} \right] \mathbf {u} \tag {11.2}
$$

and the output equation

$$
\mathbf {y} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ k _ {2} / m _ {2} & b _ {2} / m _ {2} & - k _ {2} / m _ {2} & - b _ {2} / m _ {2} \end{array} \right] \mathbf {x} + \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \mathbf {u} \tag {11.3}
$$
