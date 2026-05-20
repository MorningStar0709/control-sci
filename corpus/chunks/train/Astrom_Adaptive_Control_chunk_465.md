# EXAMPLE 6.13 Stochastic averaging

Consider the system

$$y (t) + a y (t - 1) = u (t - 1) + b u (t - 2) + e (t) + c e (t - 1)$$

with $a = -0.99$ , $b = 0.5$ , and $c = -0.7$ . Let the estimated model be

$$y (t) = u (t - 1) + r _ {1} u (t - 2) + s _ {0} y (t - 1)$$

and use the controller

$$u (t) = - s _ {0} y (t) - r _ {1} u (t - 1)$$

![](image/24577dd2e811df068d4d5fcd75dfcc35db66e9cca250876cac109ee4806ea38b.jpg)

<details>
<summary>line</summary>

| $\bar{s}_0$ | $\hat{r}_1$ |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | 0 |
| 3 | 1 |
</details>

![](image/0bccb7477258151f20e68ee667144ae08f77675099c2c4c4ff77a0c6ee83ecb6.jpg)

<details>
<summary>line</summary>

| ŝ₀ | r̂₁ |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 0.5 |
| 2.0 | 0.0 |
| 2.5 | -0.5 |
| 3.0 | -1.0 |
</details>

Figure 6.18 Phase plane for the controller parameters in Example 6.13 when recursive least-squares estimation is used. (a) Trajectories of the associated ODE. (b) Realizations of the difference equations. The parameter values corresponding to the minimum-variance controller are indicated by a dot.

The closed-loop system is described by

$$y (t) = \frac {(1 + c q ^ {- 1}) (1 + r _ {1} q ^ {- 1})}{(1 + a q ^ {- 1}) (1 + r _ {1} q ^ {- 1}) + s _ {0} q ^ {- 1} (1 + b q ^ {- 1})} e (t)u (t) = \frac {- s _ {0} (1 + c q ^ {- 1})}{(1 + a q ^ {- 1}) (1 + r _ {1} q ^ {- 1}) + s _ {0} q ^ {- 1} (1 + b q ^ {- 1})} e (t)$$

In this case,

$$
\varphi^ {T} (t - 1) = \left( \begin{array}{l l} u (t - 2) & y (t - 1) \end{array} \right) \quad \theta^ {T} = \left( \begin{array}{l l} r _ {1} & s _ {0} \end{array} \right)
$$

and

$$\varepsilon (t) = y (t)$$

Thus

$$
f (\bar {\theta}) = \binom{r _ {y u} (2)}{r _ {y} (1)} \quad G (\bar {\theta}) = \left( \begin{array}{c c} r _ {u} (0) & r _ {y u} (1) \\ r _ {y u} (1) & r _ {y} (0) \end{array} \right)
$$

where $r_y(\tau), r_u(\tau)$ , and $r_{yu}(\tau)$ are the covariance functions of $y$ and $u$ and the cross-covariance between $y$ and $u$ .
