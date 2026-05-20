# EXAMPLE 6.5 Lyapunov redesign

In Example 6.3 we found that the MIT rule could give instabilities for large adaptation gains. Under the strong assumption that the transfer function of the process is strictly positive real, however, the control law derived from stability theory is stable for all values of the adaptation gain. We illustrate this in the simulation in Fig. 6.7, in which the Lyapunov rule is applied to the system in Example 6.3. Compare with Fig. 6.5.

![](image/42629e8c2e9c432ae788cac5a05c3dc6217177e036f0c8a082caa8e4a19e911c.jpg)

<details>
<summary>line</summary>

| Time | θ̂ |
| --- | --- |
| 0 | 0 |
| 5 | ~1 |
| 10 | ~1 |
| 15 | ~1 |
| 20 | ~1 |
</details>

![](image/8223b58bff21d4849be0b4a50db0540d9e7d4767f7bd3e385dd75d952a00ff4c.jpg)

<details>
<summary>line</summary>

| Time | θ̂ |
| --- | --- |
| 0 | 0 |
| 5 | ~0.8 |
| 10 | ~0.9 |
| 15 | ~0.95 |
| 20 | ~0.95 |
</details>

![](image/cd547b33283ce0d0ed33bc5b192cf33c37147d4d5f1612ff6d9f0c5d142b059e.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 0.5 |
| 3 | 1 |
| 4 | 0.8 |
| 5 | 1 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |
| 9 | 1 |
| 10 | 1 |
| 11 | 1 |
| 12 | 1 |
| 13 | 1 |
| 14 | 1 |
| 15 | 1 |
| 16 | 1 |
| 17 | 1 |
| 18 | 1 |
| 19 | 1 |
| 20 | 1 |
</details>

Figure 6.7 Behavior of the controller gain for an adaptive system based on Lyapunov stability theory when the input signal is a unit amplitude sinusoidal with frequency (a) 1; (b) 2; and (c) 3 rad/s. The system has the transfer function $G(s) = 1/(s + 1)$ , the parameters are $k = k_{0} = 1$ , and the adaptation gain is $\gamma = 11$ . The dashed lines indicate the correct values of the gain.
