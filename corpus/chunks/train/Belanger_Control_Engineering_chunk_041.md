# 2.4 MODELING WITH LAGRANGE'S EQUATIONS

Lagrange's equations constitute a well-known and useful technique for the analysis of mechanical systems [4,5]. To use Lagrange's equations, we define a set of generalized coordinates, that is, a set of positions and angles that completely describe the motion of the system. These coordinates must be independent; that is, motion obtained by arbitrary specification of coordinate time history must be mechanically possible.

The kinetic energy of the system is a function of the generalized coordinates $q_{i}$ and their derivatives, and is written as $T(\mathbf{q}, \dot{\mathbf{q}})$ . The potential energy is a function of the $q_{i}$ and is written as $V(\mathbf{q})$ .

The Lagrangian $L$ is defined as

$$L = T - V. \tag {2.32}$$

To write Lagrange's equations, we need to define the generalized forces, $F_{i}$ . We do this by computing the work done by all nonconservative forces when $q_{i}$ is changed to $q_{i} + dq_{i}$ with all other coordinates held fixed. For infinitesimal $dq_{i}$ , the work is proportional to $dq_{i}$ , and the proportionality factor is $F_{i}$ .

Lagrange's equations are as follows:

$$\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {i}}\right) - \frac {\partial L}{\partial q _ {i}} = F _ {i}, \quad i = 1, 2, \dots , n. \tag {2.33}$$
