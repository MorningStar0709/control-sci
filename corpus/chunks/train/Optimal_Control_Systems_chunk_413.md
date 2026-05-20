# 7.5.1 Problem Formulation and Statement

Let us now formulate the energy-optimal control (EOC) system with magnitude-constrained control. Consider a linear, time-varying, fully controllable system

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {7.5.2}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are n- and r-dimensional state and control vectors, respectively, and the energy cost functional

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) d t. \tag {7.5.3}$$

Let us assume that the control $\mathbf{u}(t)$ is constrained as

$$- 1 \leq \mathbf {u} (t) \leq + 1 \quad \text { or } \quad | \mathbf {u} (t) | \leq 1 \tag {7.5.4}$$

or component wise,

$$| u _ {j} (t) | \leq 1 \quad j = 1, 2, \dots , r. \tag {7.5.5}$$

![](image/3426068177f424e250d1a73b55c300b703099ae3bd716b61fb9dd488fb334f33.jpg)

<details>
<summary>line</summary>

| X Axis | Y Axis |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | -2 |
</details>

Figure 7.30 Phase-Plane Trajectory for $\gamma_{+}$ : Initial State (2,-2) and Final State (0,0)   
![](image/f56aefd84be0270aec341e95aaa934bc7004f8db7ec8e3391987ad131e8d310f.jpg)

<details>
<summary>line</summary>

| X Axis | Y Axis |
| --- | --- |
| -2.0 | 2.0 |
| -1.5 | 1.5 |
| -1.0 | 1.0 |
| -0.5 | 0.5 |
| 0.0 | 0.0 |
| 0.5 | -0.5 |
| 1.0 | -1.0 |
| 1.5 | -1.5 |
| 2.0 | -2.0 |
</details>

Figure 7.31 Phase-Plane Trajectory for $\gamma_{-}$ : Initial State (-2,2) and Final State (0,0)

![](image/4d74031ed649939678d1ff2effb3256fa2689e63fdc575662fb099ea0e4bab60.jpg)

<details>
<summary>line</summary>

| X Axis | Y Axis |
| --- | --- |
| 0.0 | 0.0 |
| 1.0 | 1.0 |
| 1.5 | 0.5 |
</details>

Figure 7.32 Phase-Plane Trajectory for $R_{1}$ : Initial State (1,1) and Final State (0,0)   
![](image/172df0b298cebf816cfc4d125e7f7435dc55de1192175002f037a944fe98d471.jpg)

<details>
<summary>other</summary>

| X Axis | Y Axis |
| --- | --- |
| -1.5 | 0.0 |
| -1.0 | -1.0 |
| 0.0 | 0.0 |
</details>

Figure 7.33 Phase-Plane Trajectory for $R_{3}$ : Initial State (-1,-1) and Final State (0,0)

![](image/e55d71ef5831788a4782de36fb934c5860dc206f22d83d73fb4b4bfdaa8bdf9d.jpg)

<details>
<summary>line</summary>

| X Axis | Y Axis |
| --- | --- |
| -1.5 | 1.0 |
| -0.5 | 1.0 |
| 0.0 | 0.0 |
</details>

Figure 7.34 Phase-Plane Trajectory for $R_{2}$ : Initial State (-1.5,1) and Final State (0,0)   
![](image/7b4499678b4081a48bfce6a5f825abd1bec958b3c5e3bef5ce3995c9814c579f.jpg)

<details>
<summary>line</summary>

| X Axis | Y Axis |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | -1.0 |
| 1.0 | -1.0 |
</details>

Figure 7.35 Phase-Plane Trajectory for $R_4$ : Initial State (1.5,-1) and Final State (0,0)
