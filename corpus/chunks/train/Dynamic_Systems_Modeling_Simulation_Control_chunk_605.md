Because the lead controller has an open-loop pole at $s = - 1 2$ , two vertical asymptotes exist at $\sigma _ { a } = - 4 . 6 5$ . If we compare the root-locus plots for the mechanical system with the lead controller (Fig. 10.49) to the system with the PD controller (Fig. 10.42), we see that the PD controller provides more damping because the semicircular root locus (Fig. 10.42) eventually intersects the negative real axis. A good lead-controller design point is indicated on Fig. 10.49 with gain K = 42.5. This gain setting results in the closed-loop poles $s _ { 1 } = - 4 . 8 6 3$ and $s _ { 2 , 3 } = - 3 . 7 1 8 \pm$ j6.214 for a closed-loop damping ratio of $\zeta = 0 . 5 1 4$ .

Figure 10.50 shows the closed-loop step responses using both the PD and lead controllers. The closedloop system using the PD controller (Example 10.12) exhibits better damping and a shorter transient response

![](image/5e58f84976b934da1c67aa396eec2fb7c110dd3fe3c11dfcacf6f869c3091623.jpg)

<details>
<summary>line</summary>

| Point Type | Real Axis | Imaginary Axis |
| --- | --- | --- |
| Design point | 42.5 | 0 |
| σₐ = -4.65 | -4.65 | 0 |
| Lead controller pole-zero pair | -12 | 0 |
| End Point (x-intercept) | 0 | 0 |
</details>

Figure 10.49 Root-locus plot for system with lead controller $G _ { \scriptscriptstyle \mathrm { L F } } ( s ) = ( s + 3 ) / ( s + 1 2 )$ (Example 10.13).

![](image/54859d0cf3730e4f53927eca5869f5f30cb8201f1f9f674c45af3fb1ddc97fe5.jpg)

<details>
<summary>line</summary>

| Time, s | PD controller | Lead controller |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.11 | 0.14 |
| 1.0 | 0.10 | 0.09 |
| 1.5 | 0.10 | 0.10 |
</details>

Figure 10.50 Closed-loop step response using lead and PD controllers (Example 10.13).

compared to the closed-loop system using the lead controller. However, the lead controller has removed highfrequency feedback signals. Unlike the PD controller, the lead controller does not produce an impulsive force because of the step input.

On the basis of the previous discussion and Examples 10.12 and 10.13, we can make the following summary statements regarding PD and lead controllers:
