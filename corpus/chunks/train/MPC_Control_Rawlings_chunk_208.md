Because there are no state or terminal constraints, the set $\mathcal { U } _ { N } ( x ) =$ $\mathcal { U } _ { N }$ for this example does not depend on the parameter x; often it does. Both optimal control problems are quadratic programs.2 The solution for $x = 1 0$ is $u ^ { 0 } ( 1 ; 1 0 ) = u ^ { 0 } ( 2 ; 1 0 ) = - 1$ so the optimal state trajectory is $x ^ { 0 } ( 0 ; 1 0 ) = 1 0 , x ^ { 0 } ( 1 ; 1 0 ) = 9$ and $x ^ { 0 } ( 2 ; 1 0 ) = 8 $ . The value $V _ { N } ^ { 0 } ( 1 0 ) = 1 2 4$ . By solving $\mathbb { P } _ { N } ( x )$ for every $x \in [ - 1 0 , 1 0 ]$ , the optimal control law $\kappa _ { N } ( \cdot )$ on this set can be determined, and is shown in Figure 2.1(a). The implicit MPC control law is time invariant since the system being controlled, the cost, and the constraints are all time invariant. For our example, the controlled system (the system with MPC) satisfies the difference equation

$$x ^ {+} = x + \kappa_ {N} (x) \qquad \kappa_ {N} (x) = - \mathrm{sat} ((3 / 5) x)$$

and the state and control trajectories for an initial state of $x = 1 0$ are shown in Figure 2.1(b). It turns out that the origin is exponentially stable for this simple case; often, however, the terminal cost and terminal constraint set have to be carefully chosen to ensure stability. -

![](image/14a71a4d4e5d833c9f3d68c4dc4f63bce73d65f9d24f2e5e884345bfa4cb4dd1.jpg)

<details>
<summary>scatter</summary>

| x | u0 | u1 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2.25 | -1 | -1 |
| 3 | -1 | -1 |
| 4.5 | -2 | -1 |
| 5/3 | -1 | -1 |
</details>

Figure 2.2: Feasible region $\mathcal { U } _ { 2 }$ , elliptical cost contours, and ellipse center, a(x), and constrained minimizers for different values of x.
