# Example 4.40: Comparison of $\mathbf { M H E } , \mathbf { P F } ,$ , and combined MHE/PF

Consider a well-mixed semibatch chemical reactor in which the following reaction takes place

$$2 \mathrm{A} \stackrel {k} {\longrightarrow} \mathrm{B} r = k c _ {A} ^ {2}$$

The material balances for the two components are

$$
\begin{array}{l} \frac {d c _ {A}}{d t} = - 2 k c _ {A} ^ {2} + \frac {Q _ {f}}{V} c _ {A f} \\ \frac {d c _ {B}}{d t} = k c _ {A} ^ {2} + \frac {Q _ {f}}{V} c _ {B f} \\ \end{array}
$$

with constant parameter values

$$\frac {Q _ {f}}{V} = 0. 4 \quad k = 0. 1 6 \quad c _ {A f} = 1 \quad c _ {B f} = 0$$

The scalar measurement is the total pressure, which is the sum of the two states. The sample time is $\Delta = 0 . 1$ . The initial state is $x ( 0 ) = [ 3 \ : 1 ] ^ { \prime }$ and the initial prior mean is ${ \hat { x } ( 0 ) = [ 0 . 1 4 . 5 ] ^ { \prime } }$ . Moreover, the input suffers an unmodeled step disturbance at $t \ : = \ : 5$ for two samples. So this example tests robustness of the estimator to initial state error and unmodeled disturbances.

![](image/ba617dac8395ea25c68df442cdb682c9241d26025ee6292fdaddddfebce66635.jpg)

<details>
<summary>line</summary>

| t | c_A | c_B | c_j |
| --- | --- | --- | --- |
| 0 | 0.0 | 6.0 | 3.0 |
| 2 | 1.0 | 4.5 | 2.0 |
| 4 | 1.0 | 4.0 | 1.5 |
| 6 | 1.0 | 4.5 | 2.5 |
| 8 | 1.0 | 5.0 | 3.0 |
| 10 | 1.0 | 5.5 | 3.5 |
| 12 | 1.0 | 6.0 | 4.0 |
</details>

Figure 4.28: Pure MHE.

First we apply MHE to the example and the results are displayed in Figure 4.28. The horizon is chosen as N = 15. The initial covariance is chosen to be $P _ { 0 } = 1 0 I _ { 2 }$ to reflect the poor confidence in the initial state. Notice that MHE is able to recover from the poor initial state prior in only 4 or 5 samples.

Next we apply pure particle filtering using 50 particles. We use the optimal importance function because the measurement equation is linear. The particles are initialized using the same initial density as used in the MHE estimator.

$$p _ {x (0)} (x) = n (x, \hat {x} (0), P (0))$$

The results are shown in Figure 4.29. The figure shows the state and output mean versus time. We notice two effects. The particle filter is unable to recover from the poor initial samples. The measurement is predicted well but neither state is estimated accurately. The A concentration estimate is also negative, which is physically impossible. The disturbance at $t = 5$ is fortuitous and helps the PF get back on track.

![](image/49d9d7dcc5a84c43d08777267d0e37723fe65bf2f7316bd68593bd1bf7506d29.jpg)
