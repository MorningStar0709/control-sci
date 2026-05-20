# Exercise 1.2: Distributed systems and time delay

We assume familiarity with the transfer function of a time delay from an undergraduate systems course

$$\overline {{y}} (s) = e ^ {- \theta s} \overline {{u}} (s)$$

Let’s see the connection between the delay and the distributed systems, which give rise to it. A simple physical example of a time delay is the delay caused by transport in a flowing system. Consider plug flow in a tube depicted in Figure 1.11.

(a) Write down the equation of change for moles of component j for an arbitrary volume element and show that

$$\frac {\partial c _ {j}}{\partial t} = - \nabla \cdot (c _ {j} \pmb {v} _ {j}) + R _ {j}$$

![](image/37428cbed376592dd40e3d7da3929d387118ce6caa911cc171ef5766c43f8018.jpg)

<details>
<summary>text_image</summary>

c_j(0,t) = u(t)
v
z = 0
c_j(L,t) = y(t)
z = L
</details>

Figure 1.11: Plug-flow reactor.

in which $c _ { j }$ is the molar concentration of component $j , \nu _ { j }$ is the velocity of component j, and $R _ { j }$ is the production rate of component j due to chemical reaction.9

Plug flow means the fluid velocity of all components is purely in the z direction, and is independent of r and θ and, we assume here, z

$$v _ {j} = v \delta_ {z}$$

(b) Assuming plug flow and neglecting chemical reaction in the tube, show that the equation of change reduces to

$$\frac {\partial c _ {j}}{\partial t} = - \nu \frac {\partial c _ {j}}{\partial z} \tag {1.47}$$

This equation is known as a hyperbolic, first-order partial differential equation. Assume the boundary and initial conditions are

$$c _ {j} (z, t) = u (t) \quad 0 = z \quad t \geq 0 \tag {1.48}c _ {j} (z, t) = c _ {j 0} (z) \quad 0 \leq z \leq L \quad t = 0 \tag {1.49}$$

In other words, we are using the feed concentration as the manipulated variable, $u ( t )$ , and the tube starts out with some initial concentration profile of component $j , c _ { j 0 } ( z )$ .

(c) Show that the solution to (1.47) with these boundary conditions is

$$
c _ {j} (z, t) = \left\{ \begin{array}{l l} u (t - z / v) & v t > z \\ c _ {j 0} (z - v t) & v t <   z \end{array} \right. \tag {1.50}
$$

(d) If the reactor starts out empty of component $^ { j , }$ show that the transfer function between the outlet concentration, $y = c _ { j } ( L , t )$ , and the inlet concentration, $c _ { j } ( 0 , t ) = u ( t )$ , is a time delay. What is the value of $\theta ?$
