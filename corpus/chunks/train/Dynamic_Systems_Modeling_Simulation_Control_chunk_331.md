# Conceptual Problems

6.1 Figure P6.1 shows a flywheel with moment of inertia $J = 0 . 5 \mathrm { k g } \mathrm { - m } ^ { 2 }$ that is initially rotating at an angular velocity $\dot { \theta } _ { 0 } = 4 0 \mathrm { r a d / s }$ . The flywheel is subjected to friction, which is modeled by linear viscous friction torque b??̇ , with friction coefficient $b = 0 . 0 6 \mathrm { N - m { - } s / r a d }$ . Use Simulink to obtain the dynamic response and plot the angular position ??(t) (in rad) and angular velocity $\dot { \theta } ( t )$ (in rad/s). In addition, use the simulation to integrate the rate of energy dissipation $\dot { \xi }$ and plot dissipated energy (in J) vs. time. Show that the total dissipated energy as computed by the simulation is equal to the system’s initial energy.

![](image/d9b86c513f0504f1dbbf146d1d48170d7af205d0e76bfaadbd96b61829989976.jpg)

<details>
<summary>text_image</summary>

Flywheel, J
θ
Viscous friction, b
</details>

Figure P6.1

6.2 Repeat Problem 6.1 with the addition of dry (Coulomb) friction torque, $T _ { \mathrm { d r y } } \operatorname { s g n } ( \dot { \theta } )$ , where $T _ { \mathrm { d r y } } = 0 . 1 \ : \mathrm { N – m }$ . Linear viscous friction torque $( b = 0 . 0 6 \mathrm { N - m { - } s / r a d ) }$ also acts on the flywheel.   
6.3 Figure P6.3 shows a mass–damper system (no stiffness, Problem 2.3). Displacement x is measured from an equilibrium position where the damper is at the “neutral” position. The external force $f _ { a } ( t )$ is a

short-duration pulse function: $f _ { a } ( t ) = 5 \mathrm { N }$ for $0 \leq t \leq 0 . 0 2 \mathrm { s }$ , and $f _ { a } ( t ) = 0$ for $t > 0 . 0 2 { \mathrm { s } }$ . The system parameters are mass $m = 0 . 5 \mathrm { k g }$ and viscous friction coefficient b = 3 N-s/m and the system is initially at rest. Use Simulink to determine the system response and plot displacement x(t) and velocity ẋ (t).

![](image/7cb6a556731dcdb448ff3e9e0fd675e96174f9c22b6a6f563f1e61b33def1aa1.jpg)

<details>
<summary>text_image</summary>

f_a(t)
m
x
b
</details>

Figure P6.3

6.4 Figure P6.4 shows a mass–spring–damper mechanical system. The system is initially at rest. At time $t = 0$ , a pulse force is applied to the mass. The pulse force is $F _ { a } ( t ) = 8 \mathrm { N }$ for $0 \leq t \leq 0 . 0 5$ s and $F _ { a } ( t ) = 0$ for $t > 0 . 0 5 \mathrm { s }$ . The system parameters are m = 2 kg, b = 5 N-s/m, and $k = 2 0 0 \mathrm { N } / \mathrm { m }$ . Simulate the dynamic response using MATLAB commands and plot the response z(t).
