The ancillary controller may be tuned to reduce more effectively the spread of trajectories due to the external disturbance. It can be said that the main purpose of the central controller is to steer the system from one equilibrium state to another, while the purpose of the ancillary controller is to reduce the effect of the disturbance. These different objectives may require different stage costs. Our next simulation compares the performance of the standard and tube-based MPC when a more “aggressive” stage cost is employed for the ancillary controller. Figure 3.7 shows the performance of these two controllers when the nominal and standard MPC controller employ $\ell ( z - z _ { e } , \nu - \nu _ { e } )$ with $\ell ( z , \nu ) : = ( 1 / 2 ) | z | ^ { 2 } + 5 \nu ^ { 2 }$ and the ancillary controller employs $\ell _ { a } ( x , u ) = 5 0 | x | ^ { 2 } + ( 1 / 2 0 ) u ^ { 2 }$ . The tube-based MPC controller reduces the spread of the trajectories during both the transient and the steady state phases.

![](image/afa89fbd40ea5a72391d9e79407f710e9c96a9ff09ec111467bfeeda83dec64a.jpg)

<details>
<summary>line</summary>

| x | concentration |
| --- | --- |
| 0 | 1.0 |
| 50 | 0.9 |
| 100 | 0.6 |
| 150 | 0.45 |
| 200 | 0.4 |
| 250 | 0.38 |
| 300 | 0.37 |
</details>

![](image/241daa16ed2513359233807c96ace75930c90c59b1bef486e5a2798e3b30ef0e.jpg)

<details>
<summary>line</summary>

| x | temperature |
| --- | --- |
| 0 | 0.4 |
| 50 | 0.45 |
| 100 | 0.55 |
| 150 | 0.6 |
| 200 | 0.6 |
| 250 | 0.6 |
| 300 | 0.6 |
</details>

(a) Standard MPC.   
![](image/582388e65737181a33ea1d90161113dfb896e720f0f74b57499d698c288792b2.jpg)

<details>
<summary>line</summary>

| t | concentration |
| --- | --- |
| 0 | 1.0 |
| 50 | 0.98 |
| 100 | 0.85 |
| 150 | 0.55 |
| 200 | 0.35 |
| 250 | 0.25 |
| 300 | 0.25 |
</details>

![](image/ae99fbeaac7e456cc28e690fe035136d9bcb1032db91d59901f684573bc09b92.jpg)

<details>
<summary>line</summary>

| t | temperature |
| --- | --- |
| 0 | 0.4 |
| 50 | 0.42 |
| 100 | 0.55 |
| 150 | 0.6 |
| 200 | 0.65 |
| 250 | 0.66 |
| 300 | 0.66 |
</details>

(b) Tube-based MPC.   
Figure 3.7: Comparison of standard and tube-based MPC with an aggressive ancillary controller.

![](image/420b870e141537227126519f8b9ec5e5500ae8fd3bc39f730f35fae6a362e226.jpg)

<details>
<summary>line</summary>

| t | z(t) | x(t) |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 100 | 0.25 | 0.0 |
| 200 | 0.25 | 0.3 |
| 300 | 0.25 | 0.3 |
| 400 | 0.25 | 0.3 |
| 500 | 0.25 | 0.3 |
</details>
