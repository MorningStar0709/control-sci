In Figure 7.11, we show the angle responses using the full nonlinear model (MATLAB ode23) for three initial angles (the other three state components are 0 at t = 0). For $\theta(0) = 0.26$ rad, the response is close to that of the linearized system. As $\theta(0)$ increases, the response departs increasingly from that of the linearized system; for $\theta(0) \sim 0.7$ rad or greater, the angle does not go to zero. This illustrates the extent to which a linear control law can be used to control this nonlinear system.

![](image/27a6ddcca04018e772b7d222050e13f0f60c43f9b64bf6e42db2ab78ed4d68be.jpg)

<details>
<summary>line</summary>

| Time(s) | Angle (rad) | Distance (m) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.2 |
| 0.5 | 0.48 | -0.15 |
| 1.0 | 0.15 | 0.03 |
| 1.5 | 0.05 | 0.01 |
| 2.0 | 0.01 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
| 3.5 | 0.0 | 0.0 |
| 4.0 | 0.0 | 0.0 |
| 4.5 | 0.0 | 0.0 |
| 5.0 | 0.0 | 0.0 |
</details>

Figure 7.10 Results of the LQ design for the pendulum-on-cart system

![](image/e3866af5ecfee1a0391413fe6ef01971fece95f5815a4e1fcb39c8889588fb17.jpg)

<details>
<summary>line</summary>

| Time(s) | Angle (rad) - Solid Line | Angle (rad) - Dashed Line | Angle (rad) - Dotted Line |
| --- | --- | --- | --- |
| 0.0 | 0.6 | 0.4 | 0.3 |
| 0.5 | -0.2 | -0.4 | -0.7 |
| 1.0 | 0.0 | 0.1 | 0.6 |
| 1.5 | 0.0 | 0.0 | -0.1 |
| 2.0 | 0.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 | 0.0 |
| 3.5 | 0.0 | 0.0 | 0.0 |
| 4.0 | 0.0 | 0.0 | 0.0 |
| 4.5 | 0.0 | 0.0 | 0.0 |
| 5.0 | 0.0 | 0.0 | 0.0 |
</details>

Figure 7.11 Angle time responses for different initial conditions showing the nonlinear behavior
