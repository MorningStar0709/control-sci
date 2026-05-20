# EXAMPLE 3–6

Consider the inverted-pendulum system shown in Figure 3–6. Since in this system the mass is concentrated at the top of the rod, the center of gravity is the center of the pendulum ball. For this case, the moment of inertia of the pendulum about its center of gravity is small, and we assume I=0 in Equation (3–17). Then the mathematical model for this system becomes as follows:

$$(M + m) \ddot {x} + m l \ddot {\theta} = u \tag {3-18}m l ^ {2} \ddot {\theta} + m l \ddot {x} = m g l \theta \tag {3-19}$$

Equations (3–18) and (3–19) can be modified to

$$M l \ddot {\theta} = (M + m) g \theta - u \tag {3-20}M \ddot {x} = u - m g \theta \tag {3-21}$$

Figure 3–6 Inverted-pendulum system.   
![](image/9ec034cdd5c629a5a5e7f1a2df6e8059ccd4a0d6d74d17cea51b7d3a4b80e0e1.jpg)

<details>
<summary>text_image</summary>

z
x → ℓ sin θ
ℓ cos θ
θ
mg
ℓ
m
ℓ
0 → x
P
u → M
</details>

Equation (3–20) was obtained by eliminating from Equations (3–18) and (3–19). Equation\$ x (3–21) was obtained by eliminating from Equations (3–18) and (3–19). From Equation (3–20)u we obtain the plant transfer function to be

$$
\begin{array}{l} \frac {\Theta (s)}{- U (s)} = \frac {1}{M l s ^ {2} - (M + m) g} \\ = \frac {1}{M l \left(s + \sqrt {\frac {M + m}{M l} g}\right) \left(s - \sqrt {\frac {M + m}{M l} g}\right)} \\ \end{array}
$$

The inverted-pendulum plant has one pole on the negative real axis $\left[ s = - ( \sqrt { M + m } / \sqrt { M l } ) \sqrt { g } \right]$ and another on the positive real axis $\left[ s = ( \sqrt { M + m } / \sqrt { M l } ) \sqrt { g } \right]$ Hence,the plant is open-loop unstable.. Define state variables $x _ { 1 } , x _ { 2 } , x _ { 3 }$ , and $x _ { 4 }$ by

$$x _ {1} = \thetax _ {2} = \dot {\theta}x _ {3} = xx _ {4} = \dot {x}$$

Note that angle u indicates the rotation of the pendulum rod about point P, and x is the location of the cart. If we consider u and x as the outputs of the system, then

$$
\mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c} \theta \\ x \end{array} \right] = \left[ \begin{array}{c} x _ {1} \\ x _ {3} \end{array} \right]
$$

(Notice that both u and x are easily measurable quantities.) Then, from the definition of the state variables and Equations (3–20) and (3–21), we obtain

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \frac {M + m}{M l} g x _ {1} - \frac {1}{M l} u \\ \dot {x} _ {3} = x _ {4} \\ \dot {x} _ {4} = - \frac {m}{M} g x _ {1} + \frac {1}{M} u \\ \end{array}
$$

In terms of vector-matrix equations, we have
