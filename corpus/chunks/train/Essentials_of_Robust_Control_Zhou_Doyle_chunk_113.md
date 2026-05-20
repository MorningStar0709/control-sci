$$y (t) = U | G (j \omega_ {0}) | \sin (\omega_ {0} t + \phi + \angle G (j \omega_ {0}))$$

and thus the maximum possible amplification factor is $\operatorname* { s u p } _ { \omega _ { 0 } } | G ( j \omega _ { 0 } )$ ω0 |, which is precisely the $\mathcal { H } _ { \infty }$ norm of the transfer function.

In the multiple-input and multiple-output case, the $\mathcal { H } _ { \infty }$ norm of a transfer matrix $G \in \mathcal { R } \mathcal { H } _ { \infty }$ can also be regarded as the largest possible amplification factor of the system’s steady-state response to sinusoidal excitations in the following sense: Let the sinusoidal inputs be

$$
u (t) = \left[ \begin{array}{c} u _ {1} \sin (\omega_ {0} t + \phi_ {1}) \\ u _ {2} \sin (\omega_ {0} t + \phi_ {2}) \\ \vdots \\ u _ {q} \sin (\omega_ {0} t + \phi_ {q}) \end{array} \right], \quad \hat {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ \vdots \\ u _ {q} \end{array} \right].
$$

Then the steady-state response of the system can be written as

$$
y (t) = \left[ \begin{array}{c} y _ {1} \sin (\omega_ {0} t + \theta_ {1}) \\ y _ {2} \sin (\omega_ {0} t + \theta_ {2}) \\ \vdots \\ y _ {p} \sin (\omega_ {0} t + \theta_ {p}) \end{array} \right], \quad \hat {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {p} \end{array} \right]
$$

for some $y _ { i }$ , $\theta _ { i } , ~ i = 1 , 2 , \ldots , p ,$ and furthermore,

$$\| G \| _ {\infty} = \sup _ {\phi_ {i}, \omega_ {o}, \hat {u}} \frac {\| \hat {y} \|}{\| \hat {u} \|}$$

where $\left\| \cdot \right\|$ is the Euclidean norm. The details are left as an exercise.

Example 4.2 Consider a mass/spring/damper system as shown in Figure 4.2.

![](image/6128af471ade4e5b5bde31d2323a1ff272ed9a95803ef34b3778f9c1a4767841.jpg)

<details>
<summary>text_image</summary>

F₁
m₁
k₁ b₁
F₂
m₂
k₂ b₂
x₁
x₂
</details>

Figure 4.2: A two-mass/spring/damper system

The dynamical system can be described by the following differential equations:

$$
{\left[ \begin{array}{l} {\dot {x}} _ {1} \\ {\dot {x}} _ {2} \\ {\dot {x}} _ {3} \\ {\dot {x}} _ {4} \end{array} \right]} = A {\left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right]} + B {\left[ \begin{array}{l} F _ {1} \\ F _ {2} \end{array} \right]}
$$

![](image/a2dd90e0ae8ab1ffe0dde6688ccaf537a972a53c5680984540b400ce8789a18d.jpg)

<details>
<summary>line</summary>
