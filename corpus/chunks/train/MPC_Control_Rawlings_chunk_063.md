# 1.2.3 Distributed Models

Distributed models arise whenever we consider systems that are not spatially uniform. Consider, for example, a multicomponent, chemical mixture undergoing convection and chemical reaction. The microscopic mass balance for species A is

$$\frac {\partial c _ {A}}{\partial t} + \nabla \cdot (c _ {A} \nu_ {A}) - R _ {A} = 0$$

in which $c _ { A }$ is the molar concentration of species A, $\nu _ { A }$ is the velocity of species A, and $R _ { A }$ is the production rate of species A due to chemical reaction, in which

$$\nabla := \delta_ {x} \frac {\partial}{\partial x} + \delta_ {y} \frac {\partial}{\partial y} + \delta_ {z} \frac {\partial}{\partial z}$$

and the $\delta _ { x , y , z }$ are the respective unit vectors in the $( x , y , z )$ spatial coordinates.

We also should note that the distribution does not have to be “spatial.” Consider a particle size distribution $f ( \boldsymbol { r } , t )$ in which $f ( r , t ) d r$ represents the number of particles of size r to $r + d r$ in a particle reactor at time t. The reactor volume is considered well mixed and spatially homogeneous. If the particles nucleate at zero size with nucleation rate B(t) and grow with growth rate, $G ( t )$ , the evolution of the particle size distribution is given by

$${\frac {\partial f}{\partial t}} = - G {\frac {\partial f}{\partial r}}f (r, t) = B / G \quad r = 0 \quad t \geq 0f (r, t) = f _ {0} (r) \quad r \geq 0 \quad t = 0$$

Again we have partial differential equation descriptions even though the particle reactor is well mixed and spatially uniform.
