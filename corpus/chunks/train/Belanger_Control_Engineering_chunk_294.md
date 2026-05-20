a. Compute the range of positive values of $\tau$ for which the closed-loop system is stable.   
b. Choose a stabilizing value of $\tau$ .   
c. Using the linearized model, compute the responses $\theta(t)$ and $\phi(t)$ for $\theta(0)=1$ , $\phi(0)=-1$ , and $\omega_{\theta}(0)=\omega_{\phi}(0)=0$ .   
d. Using the nonlinear model, repeat part (c) for $\theta(0) = a$ , $\phi(0) = -a$ , and $\omega_{\theta}(0) = \omega_{\phi}(0) = 0$ . Do this for several values of $a$ , to explore the range of validity of the control.

![](image/5be4f928bbc9129638eb1b881a96e60803660e8c4d1048b4835b22013880dcba.jpg)

5.33 Two-pendula problem Repeat Problem 5.32 for the $H^{\infty}$ design of Problem 4.32 (Chapter 4). For the simulations, use the initial conditions $\theta_{1}(0) = a$ , $\theta_{2}(0) = -a$ , and all other state variables equal to zero.   
5.34 Assess the robust stability of the interval polynomial family based on the nominal polynomial $p(s) = s^3 + 3s^2 + 2s + 3$ , where all coefficients except that of $s^3$ may vary independently by $\pm \epsilon$ percent. For what range of values of $\epsilon$ is robust stability assured?

![](image/b324fc48b32958d5f81c974c179021745347597253a429070e821577c95a119b.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 0.1 | 80 |
| 1 | 0 |
| 10 | -250 |
| 100 | -280 |
</details>

![](image/2810c9fac528791db9c66af3b3792499bfef553f79dfc1d7cbbff170660d0528.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (dB) |
| --- | --- |
| 0.1 | -40 |
| 1 | -35 |
| 10 | -60 |
| 100 | -120 |
</details>

Figure 5.33 Bode plots

![](image/242f9e314e3fd838f1edcd77ad638e3c82ed7c126cb871a4e97c93550fd162ae.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 0.1 | -100 |
| 1 | -200 |
| 10 | -250 |
| 100 | -275 |
</details>

![](image/d52bd32a0e2127d7e82e83b01f3a8f459beba636e31ac491dbc809e45876611f.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (db) |
| --- | --- |
| 0.1 | -10 |
| 1 | -50 |
| 10 | -20 |
| 100 | -40 |
</details>

Figure 5.34 Bode plots

5.35 Repeat Problem 5.34 for the nominal polynomial $p(s) = s^4 + 3.5s^3 + 2s^2 + s + 0.5$ . (Here, the coefficient of $s^4$ is the one that is fixed.)

M
