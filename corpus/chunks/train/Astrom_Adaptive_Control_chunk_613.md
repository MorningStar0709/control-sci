# EXAMPLE 10.3 SOAS with lead network and gain changer

The relay control in Example 10.2 gave an error amplitude of about $e_{0} = 0.03$ . Assume that we want to decrease the amplitude by a factor of 3 while maintaining d = 0.35. This gives a new oscillation frequency $\omega_{u}^{\prime}$ such that

$$d \left| G (i \omega_ {u} ^ {\prime}) \right| = 0. 0 1$$

or $\omega_{u}^{\prime}=10$ rad/s. To get this oscillating frequency, a lead network $G_{f}$ is added such that

$$\arg G _ {f} (i \omega_ {u} ^ {\prime}) + \arg G _ {p} (i \omega_ {u} ^ {\prime}) = - \pi$$

Figure 10.11 shows a simulation of the system in Example 10.2 with the compensation network

$$G _ {f} (s) = 1. 2 \frac {s + 5}{s + 1 5}$$

As in Fig. 10.9, the gain is increased by a factor of 5 at t = 25. It is seen that the lead network decreases the amplitude of the oscillation while maintaining

![](image/e47f50ae39d95790bdd771d8fd1cb1302242bd850737a34e508bdbf582650af5.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | -0.5 |
| 10 | 1.0 |
| 20 | -1.0 |
| 30 | -1.0 |
| 40 | 1.0 |
| 50 | 1.0 |
</details>

![](image/7a4f2dec55f15135c55dfa659251d168c0b67280151479fbb4e16dceb3a28311.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
| 25 | 0 |
| 30 | 0 |
| 35 | 0 |
| 40 | 0 |
| 45 | 0 |
| 50 | 0 |
</details>

![](image/d788b0a0f175fe0375e9099fd7340995c843cb0b25058483c9b5db47ceb9b5c7.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0.0 |
| 10 | 0.0 |
| 20 | -0.5 |
| 30 | 0.0 |
| 40 | 0.0 |
| 50 | 0.0 |
</details>

Figure 10.11 Simulation of the system in Example 10.3 using an SOAS with a lead network. The dashed line shows the desired response $y_{m}$ .

![](image/c6f43021855c19aa76f39ec5ea08311e2c9da8489e80bcbf7d45e4cb58c929de.jpg)  
Figure 10.12 Simulation of the system in Example 10.3 using an SOAS with a lead network and a gain changer. The dashed line shows the desired response $y_{m}$ .
