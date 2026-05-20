# 7.6.4 An Optimal Observer

The pole-placement observer design implies that convergence of the estimation error to zero can be made as fast as desired by moving the eigenvalues of A - GC arbitrarily far into the LHP. That is indeed the case, if the model is exact. Let us now examine the case where

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u} + \mathbf {w} \tag {7.63}\mathbf {y} = C \mathbf {x} + \mathbf {v}. \tag {7.64}$$

![](image/f94382c6c769e3846933b805ab7b10b6dcd54c2e07cc8be9b86313a446b7f874.jpg)

<details>
<summary>line</summary>

| Time(s) | Angle (rad) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 0.0 |
| 1.5 | -2.0 |
| 2.0 | -4.0 |
</details>

![](image/11ff7395ec4090a4a0eaa09d0e7439de97c0fb5ba8f9b9c39b0f550f79917e68.jpg)

<details>
<summary>line</summary>

| Time(s) | Velocity (rad/s) - Solid Line | Velocity (rad/s) - Dashed Line |
| --- | --- | --- |
| 0.0 | 0.0 | 10.0 |
| 0.5 | -3.0 | -4.0 |
| 1.0 | -2.0 | -3.0 |
| 1.5 | -3.5 | -4.5 |
| 2.0 | -4.0 | -5.0 |
</details>

![](image/e45077d2b88e6e92ff30c565fb7763a0c8980bfeaf7166d4f9ff1ce6365cf8db.jpg)

<details>
<summary>line</summary>

| Time(s) | Amplitude (deg) |
| --- | --- |
| 0.0 | -20 |
| 0.5 | 20 |
| 1.0 | 0 |
| 1.5 | 0 |
| 2.0 | 0 |
</details>

![](image/be5c67539b6b7d4900b12edb8310ff5f2eeb9f3383bc0eda8abf1e93342fd542.jpg)

<details>
<summary>line</summary>

| Time(s) | Force (Nm) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | -2.5 |
| 0.5 | 1.5 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
</details>

Figure 7.21 Actual and observed (dashed) variables, dc servo

This model differs from the preceding one in two respects: it allows for (i) an (unknown) disturbance input $\mathbf{w}(t)$ (the plant noise) and (ii) a measurement error $\mathbf{v}(t)$ (the measurement noise). The observer is as before; i.e.,

$$\dot {\widehat {\mathbf {x}}} = A \widehat {\mathbf {x}} + B \mathbf {u} + G (\mathbf {y} - C \widehat {\mathbf {x}}). \tag {7.65}$$

We compute the equation satisfied by $\widetilde{\mathbf{x}}$ , as

$$
\begin{array}{l} \dot {\widetilde {\mathbf {x}}} = . \dot {\mathbf {x}} - \dot {\widehat {\mathbf {x}}} = A \mathbf {x} + B \mathbf {u} + \mathbf {w} - A \widehat {\mathbf {x}} - B \mathbf {u} - G (C \mathbf {x} + \mathbf {v} - C \widehat {\mathbf {x}}) \\ = A (\mathbf {x} - \widehat {\mathbf {x}}) - G C (\mathbf {x} - \widehat {\mathbf {x}}) + \mathbf {w} - G \mathbf {v} \\ \end{array}
$$

or
