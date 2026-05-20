# EXAMPLE PROBLEMS AND SOLUTIONS

A–3–1. Figure 3–20(a) shows a schematic diagram of an automobile suspension system.As the car moves along the road, the vertical displacements at the tires act as the motion excitation to the automobile suspension system. The motion of this system consists of a translational motion of the center of mass and a rotational motion about the center of mass. Mathematical modeling of the complete system is quite complicated.

A very simplified version of the suspension system is shown in Figure 3–20(b). Assuming that the motion $x _ { i }$ at point P is the input to the system and the vertical motion $x _ { o }$ of the body is the output, obtain the transfer function $X _ { o } ( s ) / X _ { i } ( s )$ (Consider the motion of the body only in the ver-. tical direction.) Displacement $x _ { o }$ is measured from the equilibrium position in the absence of input $x _ { i }$ .

Solution. The equation of motion for the system shown in Figure 3–20(b) is

$$m \ddot {x} _ {o} + b (\dot {x} _ {o} - \dot {x} _ {i}) + k (x _ {o} - x _ {i}) = 0$$

or

$$m \ddot {x} _ {o} + b \dot {x} _ {o} + k x _ {o} = b \dot {x} _ {i} + k x _ {i}$$

Taking the Laplace transform of this last equation, assuming zero initial conditions, we obtain

$$\left(m s ^ {2} + b s + k\right) X _ {o} (s) = (b s + k) X _ {i} (s)$$

Hence the transfer function $X _ { o } ( s ) / X _ { i } ( s )$ is given by

$$\frac {X _ {o} (s)}{X _ {i} (s)} = \frac {b s + k}{m s ^ {2} + b s + k}$$

![](image/95ced2d6c4d75cc50e1c6fef1ff644dc8ce62f7843f7eee83c308d89d313585b.jpg)

<details>
<summary>natural_image</summary>

Side view of a sedan car on water surface with two upward arrows indicating motion (no text or symbols)
</details>

![](image/256c1915c8955d7653d28048fee35d2421951c328437bbea59598b5f19e69661.jpg)

<details>
<summary>text_image</summary>

m
k
b
x₀
P
xᵢ
</details>

![](image/a4d735952a615bdd09559a249f0dc5bcc76cb47a99759e39b61f55f0326371e8.jpg)

<details>
<summary>text_image</summary>

Center of mass
Auto body
</details>

(a)   
(b)   
Figure 3–20 (a) Automobile suspension system; (b) simplified suspension system.

A–3–2. Obtain the transfer function $Y ( s ) / U ( s )$ of the system shown in Figure 3–21. The input u is a displacement input. (Like the system of Problem A–3–1, this is also a simplified version of an automobile or motorcycle suspension system.)
