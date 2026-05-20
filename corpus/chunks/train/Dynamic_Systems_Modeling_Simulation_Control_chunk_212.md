# Example 5.3

Figure 5.2 shows the solenoid actuator–valve system described in Chapters 2 and 3. Obtain a set of state-variable equations for this system.

The solenoid actuator consists of a coil circuit and a valve mass constrained by a return spring. When a voltage is applied to the armature circuit, an electromagnetic force is produced, which pushes on the valve to meter hydraulic flow. Recall that in Chapter 3 we showed that the inductance $L ( z )$ of the solenoid coil is a nonlinear function of armature displacement z. We also showed that the electromagnetic force $F _ { \mathrm { e m } }$ is a nonlinear function of current I and position z, or $F _ { \mathrm { e m } } = 0 . 5 K I ^ { 2 }$ , where $K = d L / d z$ . In addition, the motion of the plunger core in the coil produces a “back-emf ” voltage KIż , which is a nonlinear function of current, velocity, and position. In order to simplify matters, let us assume nominal (constant) values for inductance L and its gradient $K = d L / d z ;$ ; furthermore, let us assume linear friction and zero spring preload for the mechanical subsystem. Therefore, the complete mathematical model of the solenoid actuator is

$$L \dot {I} + R I + K I \dot {z} = e _ {\text { in }} (t) \tag {5.12}m \ddot {z} + b \dot {z} + k z = 0. 5 K I ^ {2} \tag {5.13}$$

Equation (5.12) is a first-order nonlinear ODE, and Eq. (5.13) is a second-order nonlinear ODE. Hence $n = 3$ and the complete system requires three state variables. We select current I, and armature position z and velocity ż as the three state variables, and applied voltage $e _ { \mathrm { i n } } ( t )$ is the single system input. Therefore, we have $x _ { 1 } = I , x _ { 2 } = z .$ $x _ { 3 } = { \dot { z } } .$ , and $u = e _ { \mathrm { i n } } ( t )$ .

inOnce we have defined the state variables, we write the n first-order differential equations by taking a time derivative of each state variable

$$\dot {x} _ {1} = \dot {I} = \frac {1}{L} (- R I - K I \dot {z} + e _ {\mathrm{in}} (t)) \tag {5.14}\dot {x} _ {2} = \dot {z} \tag {5.15}\dot {x} _ {3} = \ddot {z} = \frac {1}{m} (- b \dot {z} - k z + 0. 5 K I ^ {2}) \tag {5.16}$$

![](image/3b17166140f1f7f216799383b980b15dd35115f3a1872c6cc0a40dae871de5e1.jpg)

<details>
<summary>text_image</summary>

Seated position
Coil
Air gap
Supply pressure
Spool valve
Drain
Return spring
Electrical input
Armature (plunger)
Push rod
Fluid flow
</details>

Figure 5.2 Solenoid actuator–valve system for Example 5.3.
