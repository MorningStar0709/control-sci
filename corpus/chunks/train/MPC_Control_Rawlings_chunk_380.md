# 3.3.4 “Feedback” MPC

The DP solution yields the receding horizon control law $\kappa _ { N } ( \cdot )$ but requires extensive computation. In the deterministic case discussed in Chapter $2 , \kappa _ { N } ( x )$ , the MPC action for a given state x (usually the current state), can be obtained by solving an open-loop optimal control problem. For a given state x, the solutions obtained by DP and by solving the open-loop optimal control problem are identical, in which “open-loop” means the decision variable is the control sequence ${ \textbf { u } } =$ $\{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ . Our first task is to find out if there is a similar relationship when uncertainty is present. DP may again be used to determine the receding horizon control law $\kappa _ { N } ( \cdot )$ as shown in Section 3.3. The question arises: does there exist an optimal control problem $\mathbb { P } _ { N } ( x )$ , parameterized by the state x, the solution of which yields $\kappa _ { N } ( { \boldsymbol { x } } )$ , the value of the control law at $x ?$ The answer is “yes,” but the problem is, unfortunately, no longer an open-loop optimal control problem.

In the deterministic case when $x ^ { + } = f ( x , u )$ , the decision variable is $\mathbf { u } = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ , a sequence of control actions, and, if x is the initial state at time 0, a state sequence $\mathbf { x } = \{ x ( 0 ) , x ( 1 ) , \ldots , x ( N ) \}$ , where $x ( 0 ) = x$ and $x ( i ) = \phi ( i ; x , { \bf u } )$ , is generated. In the uncertain case when $x ^ { + } = f ( x , u , w )$ , the decision variable is a control policy $\pmb { \mu } = \{ u ( 0 ) , \mu _ { 1 } ( \cdot ) . , \ldots , \mu _ { N - 1 } ( \cdot ) \}$ ; if x is the initial state, the policy µ generates a state tube $\mathbf { X } ( x , \pmb { \mu } ) = \{ X ( 0 ; x ) , X ( 1 ; x , \pmb { \mu } ) , \ldots , X ( N ; x , \pmb { \mu } ) \}$ where $X ( 0 ; x ) = \{ x \}$ and, for all $i \in \mathbb { I } _ { \geq 0 } , X ( i ; x , \pmb { \mu } ) = \ \{ \phi ( i ; x , \pmb { \mu } , \mathbf { w } ) \ | \ \mathbf { w } \in \mathcal { W } \}$ . The tube $\mathbf { X } ( x , \pmb { \mu } )$ is a bundle of state trajectories, one for each admissible disturbance sequence w; see Figure 3.3. In Figure 3.3(b), the central trajectory corresponds to the disturbance sequence $\mathbf { w } = \{ 0 , 0 , 0 \}$ . The tube X may be regarded as the solution of the set difference equation

![](image/64cbc6698d289282f4ae38c8679493054a40a2ef85193fd5e1b3e7bc7785c86a.jpg)

<details>
<summary>line</summary>

| k | x |
| --- | --- |
| 0 | 1 |
| 1 | 0.5 |
| 2 | 0.3 |
| 3 | 0.2 |
</details>

(a) Deterministic case.
