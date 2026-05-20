$$R / C = \rho = [ (1 + \sin \theta) ^ {(\kappa - 1) / 2} ] / [ (1 - \sin \theta) ^ {(\kappa + 1) / 2} ]. \tag {4.16}$$

The integration constant $C$ can be determined from the initial conditions $R _ { 0 }$ and $\theta _ { 0 } = \pm { 9 0 ^ { \circ } }$ . Thus from (4.16) we obtain

$$
\lim _ {\theta \to 9 0 ^ {\circ}} R = \infty ,\theta = 0, \quad \rho = 1, \quad R = C,
\lim _ {\theta \to - 9 0 ^ {\circ}} R = \left\{ \begin{array}{l l} 0, & \text { when   } \kappa > 1, \\ R / 2, & \text { when   } \kappa = 1, \\ \infty , & \text { when   } \kappa <   1. \end{array} \right.
$$

From the above analysis, we note that the missile will intercept the target if its velocity is greater than that of the target. From (4.16), ρ(θ) can be plotted for different values of the parameter κ (i.e., κ = 0.5, 1.0, 1.5, 2.0, 3.0).

We will now consider the concept of pursuit guidance using vectorial representation. First, the relative position and velocity vectors are computed as follows:

$$\mathbf {R} _ {r} = \mathbf {R} _ {T} - \mathbf {R} _ {M},\mathbf {V} _ {r} = \mathbf {V} _ {T} - \mathbf {V} _ {M},$$

where ${ \bf R } _ { T }$ and $\mathbf { R } _ { M }$ are the position vectors of the target and missile, respectively, and ${ \bf V } _ { T }$ and ${ \mathbf { V } } _ { M }$ are their velocity vectors. The estimated time-to-go for the closest approach is then

$$t _ {g o} = - (\mathbf {R} _ {r} \cdot \mathbf {V} _ {r}) / (\mathbf {V} _ {r} \cdot \mathbf {V} _ {r}).$$

Next, compute

$$\mathbf {u} = (\mathbf {R} _ {r} / | \mathbf {R} _ {r} |) \times \mathbf {V} _ {M})$$

and the pursuer’s lateral velocity

$$\mathbf {V} _ {M L} = | \mathbf {u} |.$$

The unit lift vector’s (see Figure 4.5) direction is then

$$\mathbf {1} _ {L} = (\mathbf {V} _ {M} \times \mathbf {u}) / (\mathbf {V} _ {M} \times \mathbf {u}),$$

and the desired lift acceleration magnitude is computed as

$$a _ {L d} = (G _ {1} \mathbf {V} _ {M L}) / \max (t _ {g o}, 1),$$

where $G _ { 1 }$ is an input guidance gain. Note that the minimum value of the denominator is held at unity to avoid a singularity in $a _ { L d }$ as $t _ { g o } {  } 0$ at impact.
