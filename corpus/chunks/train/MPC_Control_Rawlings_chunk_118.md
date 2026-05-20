# Exercise 1.3: Pendulum in state space

Consider the pendulum suspended at the end of a rigid link depicted in Figure 1.12. Let r and θ denote the polar coordinates of the center of the pendulum, and let $p = r \delta _ { 1 }$ r be the position vector of the pendulum, in which $\delta _ { r }$ and $\delta _ { \theta }$ are the unit vectors in polar coordinates. We wish to determine a state space description of the system. We are able to apply a torque T to the pendulum as our manipulated variable. The pendulum has mass m, the only other external force acting on the pendulum is gravity, and we neglect friction. The link provides force $- t \delta _ { r }$ necessary to maintain the pendulum at distance r = R from the axis of rotation, and we measure this force t.

(a) Provide expressions for the four partial derivatives for changes in the unit vectors with r and θ

$$\frac {\partial \delta_ {r}}{\partial r} \qquad \frac {\partial \delta_ {r}}{\partial \theta} \qquad \frac {\partial \delta_ {\theta}}{\partial r} \qquad \frac {\partial \delta_ {\theta}}{\partial \theta}$$

(b) Use the chain rule to find the velocity of the pendulum in terms of the time derivatives of r and θ. Do not simplify yet by assuming r is constant. We want the general result.

![](image/8c79b5f03b985b2724cfd5cf8ec22165291faab0fe84d5acba1c62a71777979f.jpg)

<details>
<summary>text_image</summary>

T
r
θ
m
g
</details>

Figure 1.12: Pendulum with applied torque.

(c) Differentiate again to show that the acceleration of the pendulum is

$$\ddot {p} = (\ddot {r} - r \dot {\theta} ^ {2}) \delta_ {r} + (r \ddot {\theta} + 2 \dot {r} \dot {\theta}) \delta_ {\theta}$$

(d) Use a momentum balance on the pendulum mass (you may assume it is a point mass) to determine both the force exerted by the link

$$t = m R \dot {\theta} ^ {2} + m g \cos \theta$$

and an equation for the acceleration of the pendulum due to gravity and the applied torque

$$m R \ddot {\theta} - T / R + m g \sin \theta = 0$$

(e) Define a state vector and give a state space description of your system. What is the physical significance of your state. Assume you measure the force exerted by the link.

One answer is

$$\frac {d x _ {1}}{d t} = x _ {2}\frac {d x _ {2}}{d t} = - (g / R) \sin x _ {1} + uy = m R x _ {2} ^ {2} + m g \cos x _ {1}$$

in which $u = T / ( m R ^ { 2 } )$
