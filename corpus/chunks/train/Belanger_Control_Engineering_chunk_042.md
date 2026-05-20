# Example 2.5 (Pendulum on a Cart)

Description: An inverted pendulum of mass m and length $\ell$ moves in the vertical plane, about a horizontal axis fixed on a cart. The cart, of mass M, moves horizontally in one dimension, under the influence of a force F. (See Fig. 2.13). The pendulum rod is assumed to have zero mass. There is no friction in the system. The force F is to be manipulated to keep the pendulum vertical.

Inputs and Outputs: The input is the force F, and the outputs are the angle $\theta$ and the distance x.

Objective: Write the equations, and simulate under given conditions.

Solution The generalized coordinates are x and $\theta$ . The velocity of m has two components, one due to the motion of the cart and the other due to the angular motion of the pendulum. The velocity of the cart is $\dot{x}$ in the horizontal direction.

The horizontal position of the mass m is $x + \ell \sin \theta$ , and its vertical position is $\ell \cos \theta$ . Therefore, the total kinetic energy is

$$
\begin{array}{l} T = \frac {1}{2} M \dot {x} ^ {2} + \frac {1}{2} m \left[ \left\{\frac {d}{d t} (x + \ell \sin \theta) \right\} ^ {2} + \left\{\frac {d}{d t} (\ell \cos \theta) \right\} ^ {2} \right] \\ = \frac {1}{2} M \dot {x} ^ {2} + \frac {1}{2} m [ (\dot {x} + \ell \dot {\theta} \cos \theta) ^ {2} + (- \ell \dot {\theta} \sin \theta) ^ {2} ]. \\ \end{array}
$$

![](image/cc9062230b856c173e777ab3153c18bbccc328af4c47519fde21f2f65480d9f6.jpg)

<details>
<summary>text_image</summary>

m
θ
ℓ
F
x
</details>

Figure 2.13 Pendulum on a cart

The potential energy of $m$ varies with height. If $V_{0}$ is the potential energy of $m$ for $\theta = 90^{\circ}$ , then

$$V = V _ {0} + m g \ell \cos \theta .$$

Thus,

$$L = \frac {1}{2} M (\dot {x}) ^ {2} + \frac {1}{2} m [ (\dot {x} + \ell \dot {\theta} \cos \theta) ^ {2} + (\ell \dot {\theta} \sin \theta) ^ {2} ] - V _ {0} - m g \ell \cos \theta .$$

The only nonconservative force is F. If x is held fixed and $\theta$ is changed to $\theta + d\theta$ , F does no work: the generalized force associated with $\theta$ is zero. If $\theta$ is held fixed and x changes to $x + dx$ , the work done is Fdx; therefore, F is the generalized force associated with x.

We may now write Lagrange's equations:
