The convergence properties of the four algorithms RLS, LMS, PA, and SA are compared in Fig. 2.13. All algorithms are initialized with $\theta(0) = 0$ . The RLS method in Fig. 2.13(a) uses $P(0) = 100I$ and $\lambda = 1$ . Notice that the estimates move very quickly initially. The LMS method used in Fig. 2.13(b) has a constant gain $\gamma = 0.01$ . The estimates approach values that are close to the correct ones relatively quickly, but the estimates do not converge, since the gain is not decreasing. In the PA method in Fig. 2.13(c) the gain is normalized with $\varphi^T(t)\varphi(t)$ . Further, $\alpha = 0.1$ and $\gamma = 0.01$ are used. The approach toward the correct values is slower than for the LMS algorithm. However, the PA method is less sensitive than the LMS method to the size of the signals. The SA method is used in Fig. 2.13(d) with $\gamma = 0.2$ , and the estimates converge to the correct values even if the convergence is very slow. About 25,000-50,000 steps are needed before the estimates are close to the correct values. From the simulations it is seen that the recursive least-squares method has superior convergence properties. The price for this is the increase in computations.

![](image/f09720524bf1448d90eaa0fab6048c2713cb1e4fbb8f50ece0b0ae49c85d375d.jpg)

<details>
<summary>line</summary>

| Time | Ê | Ê' |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 400 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 800 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

![](image/02544d32c3e1552a409418e0ecfbfd091fe2faa2d38e46eab9f60ad9b98bfd80.jpg)

<details>
<summary>line</summary>

| Time | â | b̂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 200 | -1.0 | 0.5 |
| 600 | -1.0 | 0.5 |
| 1000 | -1.0 | 0.5 |
</details>

![](image/bb40030ae8b824767cd4e47474834a9b27832d8d181dd950bfec777558c7bbea.jpg)

<details>
<summary>line</summary>

| Time | â | b̂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 200 | -0.5 | 0.5 |
| 600 | -1.0 | 0.5 |
| 1000 | -1.0 | 0.5 |
</details>

![](image/99e5ab876398951a33bf3644c86b440c12bf4f5fcb80a07236c84a492df6367a.jpg)

<details>
<summary>line</summary>

| Time | â | b̂ |
| --- | --- | --- |
| 0 | -0.5 | 0.5 |
| 200 | -0.7 | 0.4 |
| 600 | -0.8 | 0.4 |
| 1000 | -0.8 | 0.4 |
</details>

Figure 2.13 The estimates of the parameters in the process for different estimation methods. (a) Recursive least squares (RLS) with $P(0) = 100$ and $\lambda = 1$ . (b) Least mean squares (LMS) with $\gamma = 0.01$ . (c) Projection algorithm (PA) with $\alpha = 0.1$ and $\gamma = 0.01$ . (d) Stochastic approximation (SA) with $\gamma = 0.2$ .

The examples show that there are many things that influence the performance of the estimators. In adaptive control it is important to remember that the estimation is done in closed loop.
