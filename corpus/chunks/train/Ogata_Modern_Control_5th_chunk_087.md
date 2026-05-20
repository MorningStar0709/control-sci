Consider the spring-mass-dashpot system mounted on a massless cart as shown in Figure 3–3. Let us obtain mathematical models of this system by assuming that the cart is standing still for $t < 0$ and the spring-mass-dashpot system on the cart is also standing still for $t < 0 .$ . In this system, $u ( t )$ is the displacement of the cart and is the input to the system. $\mathbf { A } \mathrm { t } t = 0 ,$ , the cart is moved at a constant speed, or constant. The displacementu = $y ( t )$ of the mass is the output. (The displacement is relative to the ground.) In this system, m denotes the mass, b denotes the viscous-friction coefficient, and k denotes the spring constant.We assume that the friction force of the dashpot is proportional to $\dot { y } \mathrm { ~ - ~ } \dot { u }$ and that the spring is a linear spring; that is, the spring force is proportional to $y \mathrm { ~ - ~ } u .$ .

For translational systems, Newton’s second law states that

$$m a = \sum F$$

where m is a mass, a is the acceleration of the mass, and $\Sigma F$ is the sum of the forces acting on the mass in the direction of the acceleration a. Applying Newton’s second law to the present systemg and noting that the cart is massless, we obtain

$$m \frac {d ^ {2} y}{d t ^ {2}} = - b \left(\frac {d y}{d t} - \frac {d u}{d t}\right) - k (y - u)$$

or

$$m \frac {d ^ {2} y}{d t ^ {2}} + b \frac {d y}{d t} + k y = b \frac {d u}{d t} + k u$$

This equation represents a mathematical model of the system considered. Taking the Laplace transform of this last equation, assuming zero initial condition, gives

$$(m s ^ {2} + b s + k) Y (s) = (b s + k) U (s)$$

Taking the ratio of $Y ( s )$ to $U ( s )$ , we find the transfer function of the system to be

$$\text { Transfer function } = G (s) = \frac {Y (s)}{U (s)} = \frac {b s + k}{m s ^ {2} + b s + k}$$

Such a transfer-function representation of a mathematical model is used very frequently in control engineering.

![](image/173f726ebae792cb09edf02cf023f9677dc8227568c0d1ae4508754b2a97db11.jpg)

<details>
<summary>text_image</summary>

Massless cart
u
k
b
m
y
</details>

Figure 3–3 Spring-massdashpot system mounted on a cart.

Next we shall obtain a state-space model of this system. We shall first compare the differential equation for this system

$$\ddot {y} + \frac {b}{m} \dot {y} + \frac {k}{m} y = \frac {b}{m} \dot {u} + \frac {k}{m} u$$

with the standard form

$$\ddot {y} + a _ {1} \dot {y} + a _ {2} y = b _ {0} \ddot {u} + b _ {1} \dot {u} + b _ {2} u$$
