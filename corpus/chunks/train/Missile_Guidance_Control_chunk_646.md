# 6.6.2 Missile Dynamics

This section discusses the simplified model assumed for the missile as it relates to the computation of the specific force $\mathbf { a } _ { T }$ . During launch recovery, aT is given as a function of time (t), position (R), velocity $( { \bf V } _ { M } )$ , attitude (θ and $\psi )$ , and angular acceleration $( ( d ^ { 2 } \theta / d t ^ { 2 } )$ and $( d ^ { 2 } \psi / d t ^ { 2 } ) )$ . After the start of guidance control, aT is assumed not to depend on angular acceleration. With a spherically symmetric

Earth, the gravitational acceleration (g) is given directly as a function of missile position:

$$\mathbf {g} = - \left(\mu / R ^ {3}\right) \mathbf {R}, \tag {6.232}$$

where R is the position vector measured from the center of the Earth. The instantaneous thrust and aerodynamic forces that determine aT are most easily computed in missile axes $( X _ { M } , Y _ { M } , Z _ { M } )$ and then transformed to the guidance axes $( X , Y , Z )$ for use in the equations of motion as follows:

$$
\left[ \begin{array}{c} a _ {T X} \\ a _ {T Y} \\ a _ {T Z} \end{array} \right] = \left[ \begin{array}{c c c} \cos \psi \cos \theta & - \sin \psi \cos \theta & \sin \theta \\ \sin \psi & \cos \psi & 0 \\ - \cos \psi \sin \theta & \sin \psi \sin \theta & \cos \theta \end{array} \right] \left[ \begin{array}{c} a _ {T X M} \\ a _ {T Y M} \\ a _ {T Z M} \end{array} \right] \tag {6.233}
$$

The specific force vector can then be conventionally resolved as follows:

$$a _ {T X M} = (T - D - T _ {D}) / M,a _ {T Y M} = \left(L _ {Y M} + F _ {Y M}\right) / M,a _ {T Z M} = \left(L _ {Z M} + F _ {Z M}\right) / M, \tag {6.234}$$

where

M = instantaneous missile mass,

T = total motor thrust,

$T _ { D }$ = total decrement in longitudinal thrust due to thrust vector deflection,

D = longitudinal aerodynamic force (drag),

$L _ { Y M } , Z _ { M }$ = normal components of aerodynamic force (lift),

$F _ { Y M } , Z _ { M }$ = normal components of thrust due to thrust vector deflection (control).

An Example: In the previous sections we developed the equations of motion for a missile (or rocket). In this example, we will state these equations in a different way. It is well known that optimal trajectories of a rocket moving with constant exhaust velocity and limited mass-flow rate in a Newtonian gravitational field may consist of arcs, such as null thrust, intermediate thrust, and maximum thrust. For such a case, the equations of motion in the Newtonian gravitational field can be written in vector form as follows:
