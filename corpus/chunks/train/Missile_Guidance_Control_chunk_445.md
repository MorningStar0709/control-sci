# 5.10 Three-Degree-of-Freedom Trajectory Equations and Error Analysis

In this section we present the equations that can be used to generate a point mass, three-degree-of-freedom (3DOF) trajectory and the accompanied error analysis of an unguided weapon (bomb) from an attack aircraft to impact a target on the ground. A computer program that generates the trajectory of the weapon in 3DOF from a set of given initial conditions can also perform a sensitivity analysis of impact errors for a given error covariance analysis at weapon release. The 3DOF trajectory equations are obtained from Lagrange’s equations of motion (see also Section 2.3) of a holonomic system (a dynamical system for which a displacement represented by arbitrary infinitesimal changes in the coordinates is in general a possible displacement is said to be holonomic) for a nonthrusting object in the Earth’s atmosphere. Sensitivity differential equations are obtained from the 3DOF equations and are used to propagate the initial condition error covariance matrix to impact where an analytical error analysis is performed to obtain the radial probability distribution of impact errors about the targeted aim point [11]. (Note that a Monte Carlo error analysis of initial condition errors can also be performed for comparison.)

Lagrange’s equations of motion of a holonomic system with n degrees of freedom can be stated as follows: Let $m _ { i }$ represent the mass of one of the particles of the system, and let $( x _ { i } , y _ { i } , z _ { i } )$ be its coordinates, referred to some fixed set of rectangular axes. More specifically, these coordinates of individual particles are known functions of the coordinates $q _ { 1 } , q _ { 2 } , \ldots , q _ { n }$ of the system at time t (see also Section 2.3). Therefore, this dependence can be expressed by the equations [12]

$$x _ {i} = f _ {i} (q _ {1}, q _ {2}, \dots , q _ {n}),y _ {i} = \varphi_ {i} (q _ {1}, q _ {2}, \dots , q _ {n}),z _ {i} = \psi_ {i} (q _ {1}, q _ {2}, \dots , q _ {n}).$$

Furthermore, let $( X _ { i } , Y _ { i } , Z _ { i } )$ be the components of the total force acting on the particle $m _ { i }$ . Thus, the equations of motion of this particle are [6], [11], [12]

$$m _ {i} \left(\frac {d ^ {2} x _ {i}}{d t ^ {2}}\right) = X _ {i}, \tag {5.42a}m _ {i} \left(\frac {d ^ {2} y _ {i}}{d t ^ {2}}\right) = Y _ {i}, \tag {5.42b}m _ {i} \left(\frac {d ^ {2} z _ {i}}{d t ^ {2}}\right) = Z _ {i}. \tag {5.42c}$$

The trajectory equation error model includes the following:
