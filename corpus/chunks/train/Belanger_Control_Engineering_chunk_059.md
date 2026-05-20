ii. $J_{m}\dot{\omega}_{m} = T_{m} - \frac{1}{N}$ (torque exerted by spring).

iii. Write $di / dt$ as in Example 2.1, and use the fact that $\omega_{m} = N\dot{\theta}_{1}$ .

iv. Because $\theta_{1} - \theta_{2}$ is small, the equations for $\dot{\omega}_{1}$ and $\dot{\omega}_{2}$ call for differences of almost equal terms. It is numerically preferable to work with $\Delta = \theta_{1} - \theta_{2}$ . Define $\dot{\Delta} = \Omega$ , and write an equation for $\dot{\Omega}$ in terms of $\Delta$ and $i$ . Write the state equations, using the state variables $\theta_{2}, \Delta, \omega_{2}, \Omega$ , and $i$ , with $v$ as the input.

b. Write the state equations for the specific values of Example 2.1, with $K = 500 \, \mathrm{Nm/rad}$ .

c. Simulate under the conditions given in Example 2.1.

![](image/9f93483b969ca52f6f35445a04bdd893ee4333d1c7bc1912eb8ebc61cc17a40e.jpg)

<details>
<summary>text_image</summary>

i
+
v
-
ωm, Tm
θ1 K θ2 J
N : 1
</details>

Figure 2.19 Servo with flexible shaft

![](image/4f04871c5835158260634cd76336658004e5bf3ff616460762a4038011b36238.jpg)

2.6 Drum speed control In the system of Figure 2.20, two identical dc motors are working in cooperation to rotate a large drum, which is subject to a load torque. The motors are assumed to have rotor inertia $J_{m}$ negligible inductance, and their shafts are modeled by rotary springs. (This model is useful to explain why shafts fail from vibration fatigue.)

![](image/8fbec6e99b170bc9629c37f63399ce24113e8665d202c1cd7cefcaca64e5d1c8.jpg)

<details>
<summary>text_image</summary>

J0
R
T0
ω0
K
φ1
r
φ2
K
u1
θ1, ω1, T1
u2
θ2, ω2, T2
</details>

Figure 2.20 Drum driven by two motors

a. Model the system, with the following suggested steps:

i. Write Newton's law for $\dot{\omega}_1$ and $\dot{\omega}_2$ , using the motor torques $T_1$ and $T_2$ and the fact that the spring torques are proportional to the differences $\theta_1 - \phi_1$ and $\theta_2 - \phi_2$ , respectively.

ii. Write Newton's law for the large inertia; the torque applied by each motor shaft is multiplied by the ratio $R / r$ .
