# Example 2.7

Figure 2.22 shows a single-disk mechanical system, where the rotor is supported by bearings, and a motor provides input torque $T _ { \mathrm { i n } } ( t )$ directly to the rotor inertia J. Derive the mathematical model of the 1-DOF system.

In this example, we have a single displacement variable, angular position ??, which is measured clockwise from a fixed reference position as shown in Fig. 2.22. The rotor has friction due to the bearings and the fluid surrounding the rotor. Let us assume an ideal (linear) friction model, and lump the bearing and fluid friction into a single rotational friction coefficient b, with units of N-m-s/rad. Hence, the total friction torque is $b { \dot { \theta } } .$ , which always opposes the angular motion.

Figure 2.23 presents the FBD of the single moment of inertia J, showing the positive (clockwise) convention for angular displacement ??. The input torque $T _ { \mathrm { i n } } ( t )$ is in the positive direction. The direction of the friction torque is determined by assuming a positive angular velocity (clockwise). This positive angular velocity results in a resistive torque that opposes motion. Hence, b??̇ is shown as counterclockwise on the FBD.

![](image/febe4383a67feb65ada3761a9b7dad95fe1bb755fa38172b81cc5484ada7110a.jpg)

<details>
<summary>text_image</summary>

Motor torque,
Tin(t)
θ
Axis
Rotor, J
Viscous
friction, b
</details>

Figure 2.22 Single-disk mechanical system for Example 2.7.

![](image/1a8b2293c559e9a8692584a48529876dfeeb2fc1d883a2c38bd691282d41df16.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["J"] -->|T_in(t)| B
    B -->|+θ| C
    C -->|bθ̇| A
```
</details>

Figure 2.23 Free-body diagram for the rotor (Example 2.7).

Summing all external torques on disk J with the sign convention as positive clockwise yields

$$⑦ + \sum T = T _ {\text { in }} (t) - b \dot {\theta} = J \ddot {\theta} \tag {2.37}$$

Rearranging Eq. (2.37), we obtain the mathematical model

$$J \ddot {\theta} + b \dot {\theta} = T _ {\text { in }} (t) \tag {2.38}$$

Equation (2.38) is a linear, second-order model of the single-disk mechanical system. The dynamic variable is angular position ??, and the input is the applied torque $T _ { \mathrm { i n } } ( t )$ .
