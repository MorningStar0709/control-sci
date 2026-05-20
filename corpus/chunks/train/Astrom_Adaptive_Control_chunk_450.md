# Step Commands

First, the behavior illustrated in Fig. 6.13 is analyzed. The case of step commands is first investigated when there is no measurement noise. When $\omega = 0$ , the equilibrium condition of Eq. (6.58) reduces to

$$\bar {\theta} _ {2} = \frac {1}{G _ {m} (0)} \bar {\theta} _ {1} - \frac {1}{G (0)} \tag {6.64}$$

![](image/447d63a19a6217840a1ccc4386889a3d0590c7876b0e74f7191adac6029f053f.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ | θ̂₂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 50 | ~1.2 | ~0.8 |
| 100 | ~1.3 | ~0.9 |
| 150 | ~1.35 | ~0.95 |
| 200 | ~1.4 | ~1.0 |
</details>

![](image/c99023087d82ae6ea6685dd244d5c3404e2616016e671e2da5f944907c7f6e49.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ | θ̂₂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 50 | 1.8 | 1.8 |
| 100 | 1.8 | 1.8 |
| 150 | 1.8 | 1.8 |
| 200 | 1.8 | 1.8 |
</details>

![](image/f483759181e0f2d087c68075f05a2d14e206c416e3a22f0e9d34c235ef489539.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ | θ̂₂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 25 | 3.8 | 4.5 |
| 50 | 1.5 | 4.0 |
| 100 | 1.2 | 3.5 |
| 150 | 1.3 | 3.3 |
| 200 | 1.4 | 3.2 |
</details>

![](image/29ca0ad543191baf85c66ff7be1869d6c28f6d75d20dab635f1d06bfcf5fef98.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ | θ̂₂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 50 | ~1.0 | ~0.5 |
| 100 | ~3.0 | ~1.5 |
| 150 | ~8.0 | ~4.0 |
| 200 | ~16.0 | ~9.0 |
</details>

Figure 6.14 Controller parameters $\hat{\theta}_1$ and $\hat{\theta}_2$ when the adaptive control law of Eqs. (6.57) is applied to the process of Eq. (6.63) when the command signal is $u_c = \sin \omega t$ with (a) $\omega = 1$ ; (b) $\omega = 3$ ; (c) $\omega = 6$ ; (d) $\omega = 20$ .

The equilibrium set is thus a straight line in the parameter space. The line is uniquely determined by the steady-state gains $G(0)$ and $G_{m}(0)$ . Notice in particular that the equilibrium set is not a point. This is easily understood from the viewpoint of system identification. We wish to determine two parameters, $\hat{\theta}_{1}$ and $\hat{\theta}_{2}$ . However, the excitation used is a step that is persistently exciting of first order and thus admits determination of only one parameter. (See Example 2.5.)
