# EXAMPLE 7.5 Probing

An interesting feature of the dual control law is that it behaves quite differently from the heuristic algorithms. The most significant feature is the probing that takes place to gain more information about the unknown parameters. The effect of probing is most significant when the output y is small. Probing can be illustrated by using the results of Example 7.4. Both the cautious and certainty equivalence control laws are continuous in y and zero for y = 0. However, the dual control law is very different. To show this, consider the control signal for y = 0-. Figure 7.6 shows the control signal for y = 0- as a function of the normalized parameter precision, $\beta = \hat{b}/\sqrt{P}$ , for different time horizons. All control laws give zero control signal when the parameter estimate is reasonably precise. However, for uncertain estimates, the control signal is different from zero, and the transition is discontinuous. This discontinuity can be used to define a probing zone. Notice that the probing zone increases with increasing time horizon. For N = 31, probing occurs when $\beta \leq 1.3$ , that is, when $\hat{b} \leq 1.3\sqrt{P}$ .

![](image/00803e3fd115fc5856b381b83b975dab4e21fa19ca03ae1cc009320bce759e12.jpg)

<details>
<summary>area</summary>

| β | μ (N=3) | μ (N=6) | μ (N=31) |
| --- | --- | --- | --- |
| 0.0 | 0.5 | 1.0 | 1.0 |
| 0.5 | 0.5 | 0.5 | 0.5 |
| 1.0 | 0.5 | 0.5 | 0.5 |
| 1.5 | 0.5 | 0.5 | 0.5 |
</details>

Figure 7.6 Control signal as a function of the normalized parameter precision $\beta$ for optimal control laws for different time horizons.
