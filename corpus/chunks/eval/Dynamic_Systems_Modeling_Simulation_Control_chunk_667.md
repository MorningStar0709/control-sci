We can now simulate a few trial solenoid designs using the integrated Simulink model shown in Fig. 11.14 with $N = 4 0 , 5 0$ , and 60. Equation (11.20) and Fig. 11.17a show that the steady-state electromagnetic force is between 4.3 (for $N = 4 0 )$ ) and 9.7 N (for N = 60). The spring constant k required to balance $\overline { { F } } _ { \mathrm { e m } }$ for a 2-mm stroke is computed using Eq. (11.21), and the inductance $L _ { 0 }$ and $d L / d x$ values are computed using Eqs. (11.12) and (11.14), respectively. Figure 11.18 shows the valve position x(t) for a 12-V step input for these three values of N. Clearly, all three solenoid designs show a 2-mm stroke at steady state because the return spring is perfectly matched to balance the electromagnetic force. The solenoid actuator with $N = 6 0$ has the smallest response time, while the actuator with $N = 4 0$ took the longest time to reach steady state. Next, we investigated solenoid designs with more powerful electromagnets with N = 70, 80, and 90 turns. Figure 11.19 shows the valve responses for these three cases. While all three solenoid designs show good initial movement toward the steady-state position, all three show “dips” in x(t) before reaching x = 2 mm and subsequently an extended settling time for the transient response. Figure 11.20 shows that the solenoid responses become even slower for even stronger electromagnets with N = 100, 110, and 120.

![](image/33923fb8c316e0ffd687e41deebffa8503a4430b2f54f89c25aeb15ce77bcf5d.jpg)

<details>
<summary>line</summary>

| Number of turns, N | Steady-state electromagnetic force, N |
| --- | --- |
| 0 | 0 |
| 20 | ~2 |
| 40 | ~6 |
| 60 | ~12 |
| 80 | ~20 |
| 100 | ~30 |
| 120 | ~45 |
| 140 | ~60 |
| 160 | ~75 |
| 180 | ~90 |
| 200 | ~108 |
</details>

(a)

![](image/e92fb936cb260e3c9b93b04528c95290eb9a68ad3d5e81bdc337607908cc103f.jpg)

<details>
<summary>line</summary>

| Number of turns, N | Spring constant, k, N/m |
| --- | --- |
| 0 | 0 |
| 20 | ~500 |
| 40 | ~1000 |
| 60 | ~1500 |
| 80 | ~2000 |
| 100 | ~2500 |
| 120 | ~3000 |
| 140 | ~3500 |
| 160 | ~4000 |
| 180 | ~4500 |
| 200 | ~5000 |
</details>

(b)   
Figure 11.17 Solenoid parameters vs. number of turns N: (a) steady-state electromagnetic force and (b) spring constant k.

![](image/b9e1c7371dc9051c035b53c1d6bc3031fb0d8b317bd6d84a825e7b35d3cda1c8.jpg)

<details>
<summary>line</summary>
