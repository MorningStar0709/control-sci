7.33 An engineer needs to select a shock-mount system for a delicate instrument’s housing. The instrument and shock-mounts are modeled as a mass–spring–damper mechanical system. The total system mass is 3 kg. Two shock-mount options are available, and the composite stiffness and friction coefficients are listed below:

$$\text { Option A: } \quad k = 1 1, 3 0 0 \mathrm{N} / \mathrm{m} \quad b = 9 0 \mathrm{N} - \mathrm{s} / \mathrm{m}\text { Option B: } \quad k = 8 7 0 0 \mathrm{N} / \mathrm{m} \quad b = 8 8 \mathrm{N} - \mathrm{s} / \mathrm{m}$$

Which shock-mount option would result in the smallest maximum overshoot for a step input? Explain your answer.

7.34 An engineer wants to develop a model of an existing mechanical system that has complicated geometry. She suspects that a low-order linear model may provide an accurate representation of the complex system. She applies a step torque input $T _ { \mathrm { i n } } ( t ) = 0 . 6 U ( t )$ N-m and measures the angular position of the rotational system. Figure P7.34 shows the step response she obtains by experimentation.

![](image/30c30bab2ed48512bee0ea0aadd1674e01840748f5901bcec4e9d60c5f80e67c.jpg)

<details>
<summary>line</summary>

| Time, s | Angular position, θ(t), rad |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0160 |
| 1.0 | 0.0110 |
| 1.5 | 0.0125 |
| 2.0 | 0.0120 |
| 2.5 | 0.0120 |
| 3.0 | 0.0120 |
</details>

Figure P7.34

a. Develop a transfer function for the mechanical system.   
b. Use MATLAB or Simulink to simulate the step response of the transfer function developed in part (a) using the torque input $T _ { \mathrm { i n } } ( t ) = 0 . 6 U ( t ) \mathrm { N \mathrm { - m } }$ . Compare the simulation result to Fig. P7.34. Is the low-order linear model accurate?
