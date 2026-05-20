# EXAMPLE 9.6 Ship steering

Assume that the ship steering dynamics can be approximated by the Nomoto model of Eq. (9.12) and that a controller of PD type with the transfer function

$$G _ {r} (s) = K \left(1 + s T _ {d}\right)$$

is used. The loop transfer function is

$$G (s) G _ {r} (s) = \frac {K b (1 + s T _ {d})}{s (s + a)}$$

The characteristic equation of the closed-loop system is

$$s ^ {2} + s (a + b K T _ {d}) + b K = 0$$

The relative damping is

$$\zeta = \frac {1}{2} \left(\frac {a}{\sqrt {b K}} + T _ {d} \sqrt {b K}\right)$$

The damping will depend on the speed of the ship. Assume that the model of Eq. (9.12) has the values $a_{nom}$ and $b_{nom}$ at the nominal speed $u_{nom}$ . The variable $u_{nom}$ is the nominal velocity used to design the feedback. Assume that u is the actual constant velocity. Using the speed dependence of a and b given by Eqs. (9.13) gives

$$a = a _ {\mathrm{nom}} \frac {u}{u _ {\mathrm{nom}}}b = b _ {\text { nom }} \left(\frac {u}{u _ {\text { nom }}}\right) ^ {2}$$

This gives the damping

$$\zeta = \frac {1}{2} \left(\frac {a _ {\mathrm{nom}}}{\sqrt {K b _ {\mathrm{nom}}}} + \frac {u}{u _ {\mathrm{nom}}} T _ {d} \sqrt {K b _ {\mathrm{nom}}}\right)$$

Consider an unstable tanker with

$$a _ {\text { nom }} = - 0. 3b _ {\text { nom }} = 0. 8K = 2. 5T _ {d} = 0. 8 6$$

This gives $\zeta = 0.5$ and $\omega = 1.4$ at the nominal velocity. Furthermore,

$$\omega = 1. 4 u / u _ {\text { nom }}\zeta = - 0. 1 1 + 0. 6 1 u / u _ {\text { nom }}$$

The closed-loop characteristic frequency and damping will thus decrease with decreasing velocity. The closed-loop system becomes unstable when the speed of the ship decreases to $u = 0.17u_{nom}$ .

By scaling the parameters of the autopilot according to speed, it is possible to obtain closed-loop performance that is less sensitive to speed variations. The scaling of the parameters of the controller depends on the control goal. One design criterion is time invariance; that is, the time response of the ship should always be the same. If true time invariance is desired, the controller gains should be inversely proportional to the square of the speed. Path invariance is another criterion. In this case the path on the map is always the same. The gains should then be inversely proportional to the velocity of the ship. The gains are limited at low speed to avoid large rudder motions.
