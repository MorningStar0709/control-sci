iii. Write differential equations for $\Delta_1 = \theta_1 - \phi_1$ and $\Delta_2 = \theta_2 - \phi_2$ . Note that $\dot{\phi}_1 = \dot{\phi}_2 = -\frac{R}{r}\omega_0$ , so $\dot{\Delta}_1$ and $\dot{\Delta}_2$ are expressed in terms of $\omega_1, \omega_2$ , and $\omega_0$ .   
iv. Write the motor torques in terms of the applied armature voltages $u_{1}$ and $u_{2}$ , the motor torque constant $K_{m}$ , and the armature resistance $R_{a}$ .

You should have five state variables, $\Delta_{1}, \Delta_{2}, \omega_{1}, \omega_{2}$ , and $\omega_{0}$ , and three inputs, $u_{1}, u_{2}$ , and $T_{0}$ .

b. Write the state equations for the following values: $K_{m} = 6.0 \, Nm/A$ , $R_{a} = 0.2 \, \Omega$ , $J_{m} = 1 \, kg \, m^{2}$ , $K = 75,000 \, Nm/rad$ , $J_{0} = 10,000 \, kg \, m^{2}$ , $R = 1 \, m$ , r = 0.07 m.   
c. Simulate for the following conditions: $\Delta_{1}(0) = \Delta_{2}(0) = 0, \omega_{0}(0) = 4.67 \mathrm{rad/s}$ , $\omega_{1}(0) = \omega_{2}(0) = 66.68 \mathrm{rad/s}$ , $u_{1} = u_{2} = 4 \mathrm{~V}$ , and the load torque $T_{0}$ is a step of $1000 \mathrm{Nm}$ .

![](image/3328e7c0ffc21213bb536c405224acf73a07433560657e7be62c8720c0115513.jpg)

2.7 Blending tank A blending tank has two input flows of products A and B, respectively (gin and vermouth, for example). The flow of B is uncontrolled, and the flows of A and the output are controlled. The flows $F_{A}$ , $F_{B}$ , and $F_{0}$ are in cubic meters per second. (See Fig. 2.21.) The tank is well mixed, so that uniform composition is assumed. A control system is required to regulate composition and level.

![](image/a7587b22a68d16c06b35de4a65202e7d7dfdf30d03e759a85e876e8f1f68b682.jpg)

<details>
<summary>text_image</summary>

F_A
F_B
l
F_0
</details>

Figure 2.21 Blending tank

a. Derive a model for this system, with the following suggested steps as a guide:
