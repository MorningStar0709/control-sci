# Example 6.7

Consider again the spool-valve system in Fig. 6.3 and Example 6.2, but with the inclusion of Coulomb or dry friction along with viscous friction. Simulate the response to a 12-N step input.

Let us assume that the dry friction force $F _ { \mathrm { d r y } }$ has a magnitude of 0.4 N. Because the dry friction force always opposes the direction of motion, it can be modeled as $F _ { \mathrm { d r y } } \operatorname { s g n } ( \dot { y } )$ , where the signum function “sgn” returns the sign of its input value, which is velocity ẏ . Adding the dry friction term $F _ { \mathrm { d r y } } \operatorname { s g n } ( \dot { y } )$ to the linear spool-valve equation (6.8) yields a nonlinear mathematical model of the spool valve

$$0. 0 4 \ddot {y} + 1 6 \dot {y} + 0. 4 \operatorname{sgn} (\dot {y}) + 7 0 0 0 y = f (t) \tag {6.20}$$

Because the mathematical model is nonlinear, we must use the integrator-block approach to obtain the system’s response. Recall that in Example 6.6 we constructed our block diagram from the double integration of acceleration of the valve mass, and therefore we solve Eq. (6.20) for acceleration

$$\ddot {y} = \frac {1}{0 . 0 4} (- 1 6 \dot {y} - 0. 4 \operatorname{sgn} (\dot {y}) - 7 0 0 0 y + f (t)) \tag {6.21}$$

All bracketed terms in Eq. (6.21) are forces: viscous friction force, dry friction force, spring force, and the applied force f (t). We can modify the linear system Simulink diagram shown in Fig. 6.12 and include an additional feedback path for the dry friction force. Figure 6.13 shows the Simulink diagram of the spool valve with the addition of the dry friction force. This force is created by sending velocity ẏ to the signum (or Sign) function from the Math Operations library, followed by a Gain block that represents the dry force magnitude (0.4 N in this case). Note that the summing junction has been modified to accept four (force) signals with the appropriate signs in order to match Eq. (6.21).

![](image/9ff7aa4bc9b12a4ff14ea8216c526113654eee481652efe74f90c44300f78a04.jpg)

<details>
<summary>flowchart</summary>
