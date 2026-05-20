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

![](image/99f373fc544d8915bfbd709a65ee2a345ff2a90a8cd1c8618fe3b14cbb5f01b0.jpg)

<details>
<summary>line</summary>

| x | temperature |
| --- | --- |
| 0 | 0.4 |
| 50 | 0.45 |
| 100 | 0.55 |
| 150 | 0.6 |
| 200 | 0.61 |
| 250 | 0.61 |
| 300 | 0.61 |
</details>

(a) Standard MPC.   
![](image/f9ea1155b6c186371a604ffb32f0da559661720a00e3ae966117949d33857105.jpg)

<details>
<summary>line</summary>

| t | concentration |
| --- | --- |
| 0 | 1.0 |
| 50 | 0.95 |
| 100 | 0.85 |
| 150 | 0.25 |
| 200 | 0.25 |
| 250 | 0.25 |
| 300 | 0.25 |
</details>

![](image/4e53e5533c6b6ce597a79c819a79020339bf5bbc57c5926d43e6067e6b62e379.jpg)

<details>
<summary>line</summary>

| t | temperature |
| --- | --- |
| 0 | 0.4 |
| 50 | 0.45 |
| 100 | 0.55 |
| 150 | 0.65 |
| 200 | 0.66 |
| 250 | 0.66 |
| 300 | 0.66 |
</details>

(b) Tube-based MPC.   
Figure 3.6: Comparison of 100 realizations of standard and tubebased MPC for the chemical reactor example.

For comparison, a standard MPC controller using the same stage cost $\ell ( \cdot )$ , and the same terminal constraint set $\mathbb { Z } _ { f }$ employed in the central path controller is simulated. Figure 3.6(a) illustrates the performance standard MPC, and Figure 3.6(b) the performance of tube-based MPC for 100 realizations of the disturbance sequence. Tube-based MPC, as expected, has a smaller spread of trajectories than is the case for standard MPC. Because each controller has the same stage cost and terminal constraint, the spread of trajectories in the steady-state phase when $z ( t ) = z _ { e }$ is the same for the two controllers. Because the control constraint set for the tube-based central controller is tighter than that for the standard controller, however, the tube-based controller is somewhat slower than the standard controller.
