Figure 11.16 shows the inner details of the mechanical subsystem. The reader should be able to identify the six force components from the mathematical model (11.10) that are summed to produce the net force acting on the armature mass (note that dry-friction force is included in the Simulink model, even though the constant Fdry is set to zero as indicated in Table 11.2). Recall that the wall-contact force $F _ { C }$ balances the difference between the spring preload and electromagnetic forces if the armature is seated:

$$
F _ {C} = \left\{ \begin{array}{c c c} F _ {\mathrm{PL}} - F _ {\mathrm{em}} & \text { if } & F _ {\mathrm{em}} <   F _ {\mathrm{PL}} \\ 0 & \text { if } & F _ {\mathrm{em}} \geq F _ {\mathrm{PL}} \end{array} \right. \tag {11.16}
$$

The contact force is determined in the Simulink model according to Eq. (11.16) by subtracting the electromagnetic force from the preload spring force and sending the result to the Saturation block from the Discontinuities library. A Saturation block will set its output equal to the input if the input is between upper and lower limits set by the user. Otherwise, the output is set to either the upper limit if the input exceeds the upper limit or to the lower limit if the input is less than the lower limit. Equation (11.16) is satisfied if the upper limit of the Saturation block is set to a large positive number and the lower limit is set to zero. In other words, the wall-contact force is the positive force difference $F _ { \mathrm { P L } } - F _ { \mathrm { e m } }$ required to balance the preloaded spring (when $F _ { \mathrm { e m } } < F _ { \mathrm { P L } }$ and the mass is still seated), but the contact force cannot be negative.

![](image/bbed73ed70618146f6e500a712f9014e98048275ea2df0bfb03b96b9ffa52239.jpg)

<details>
<summary>flowchart</summary>
