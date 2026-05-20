# 2.3 D’Alembert’s Principle

In Section 2.2 we discussed the rigid-body equations of motion. Specifically, we discussed Newton’s second law as given by (2.17b) and (2.18b). In the fundamental equation (2.18b), $\mathbf { F } = m \mathbf { a }$ , the quantity $m ( - \mathbf { a } )$ is called the reversed effective force or inertia force. D’Alembert’s principle is based on Newton’s second and third laws of motion and states that ‘the inertia force is in equilibrium with the external applied force,’ or

$$\mathbf {F} + m (- \mathbf {a}) = 0. \tag {2.54}$$

This principle has the effect of reducing a dynamical problem to a problem in statics and may thus make it easier to solve. Based on the principle of virtual work, ∗ which was established for the case of static equilibrium, we can proceed as follows: Let p be the momentum of a particle in the system, and separate the forces acting on it into an applied force F and a constraint force f. Then the equation of motion of the particle can be written as [9]

$$\mathbf {F} + \mathbf {f} - \left(\frac {d \mathbf {p}}{d t}\right) = 0.$$

The quantity $( d \mathbf { p } / d t )$ is usually referred to as the reverse effective force discussed above. Note that the virtual work of the constraint force is zero, since f and δr are mutually perpendicular. The virtual work of the forces acting on the particle is

$$\left[ \mathbf {F} _ {i} - \left(\frac {d \mathbf {p} _ {i}}{d t}\right) \right] \cdot \delta \mathbf {r} _ {i} = 0 (i = 1, 2, \dots , N),$$

and for a system of N particles,

$$\sum_ {i = 1} ^ {N} \left[ \mathbf {F} _ {i} - \left(\frac {d \mathbf {p} _ {i}}{d t}\right) \right] \cdot \delta \mathbf {r} _ {i} = 0 (i = 1, 2, \dots , N).$$

Another way of writing this equation is

$$\sum_ {i = 1} ^ {N} \left[ \mathbf {F} _ {i} - m _ {i} \left(\frac {d ^ {2} \mathbf {r} _ {i}}{d t ^ {2}}\right) \right] \cdot \delta \mathbf {r} _ {i} = 0 (i = 1, 2, \dots , N),$$

where $\mathbf { r } _ { i }$ is the position vector of the particle. The term $- m _ { i } ( d ^ { 2 } \mathbf { r } _ { i } / d t ^ { 2 } )$ has the dimensions of force and is known as the inertia force acting on the ith particle (see also discussion above). This is the Lagrangian form of d’Alembert’s principle and is one of the most important equations of classical dynamics.
