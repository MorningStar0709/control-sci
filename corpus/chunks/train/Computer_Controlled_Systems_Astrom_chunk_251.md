# Analysis of the Closed-Loop System

The closed-loop system has desirable properties. To show this, introduce

$$\vec {x} = x - \hat {x}$$

It follows from Eqs. (4.33) and (4.34) that the closed-loop system can be described by the equations

$$
\begin{array}{l} x (k + 1) = (\Phi - \Gamma L) x (k) + \Gamma L \tilde {x} (k \mid k - 1) \\ \tilde {x} (k + 1 \mid k) = (\Phi - K C) \tilde {x} (k \mid k - 1) \tag {4.36} \\ \end{array}
$$

The closed-loop system has order 2n. The eigenvalues of the closed-loop system are the eigenvalues of the matrices $\Phi - \Gamma L$ and $\Phi - KC$ . Notice that the eigenvalues of $\Phi - \Gamma L$ are the desired closed-loop poles obtained by solving the pole-placement problem in Sec. 4.3 and the eigenvalues of $\Phi - KC$ are the poles of the observer given in Sec. 4.4.

![](image/9e360b1284bfd2552e0d88bf688bb1e07416c23373b5929215285ff9c908b8b9.jpg)

<details>
<summary>line</summary>

| x | Position |
| --- | --- |
| 0 | 0 |
| 1 | 1.5 |
| 2 | 2.0 |
| 3 | 1.8 |
| 4 | 1.5 |
| 5 | 1.0 |
| 6 | 0.5 |
| 7 | 0.2 |
| 8 | 0.1 |
| 9 | 0.05 |
| 10 | 0 |
</details>

![](image/b7f5f663a86675a47bc97349963835293fd5eeb406a83148c6dd31b08cc64d0e.jpg)

<details>
<summary>line</summary>

| x | Velocity |
| --- | --- |
| 0 | 1.0 |
| 1 | 0.5 |
| 2 | 0.0 |
| 3 | -0.5 |
| 4 | -0.8 |
| 5 | -0.6 |
| 6 | -0.4 |
| 7 | -0.2 |
| 8 | -0.1 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

![](image/0791cd4bc1ff3024f8d18c6f6f35669b1d729e26399bff183a6e150ff7526c0e.jpg)

<details>
<summary>line</summary>

| Time | Position |
| --- | --- |
| 0 | 1.0 |
| 1 | 1.5 |
| 2 | 1.2 |
| 3 | 0.8 |
| 4 | 0.4 |
| 5 | 0.1 |
| 6 | 0.05 |
| 7 | 0.02 |
| 8 | 0.01 |
| 9 | 0.005 |
| 10 | 0.001 |
</details>

![](image/f74666b37f3e810986ecaf6f018bde34b973f90fe503beede966ae7490aa2e78.jpg)

<details>
<summary>line</summary>

| Time | Velocity |
| --- | --- |
| 0 | 1.0 |
| 1 | 0.2 |
| 2 | -0.3 |
| 3 | -0.4 |
| 4 | -0.3 |
| 5 | -0.1 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

Figure 4.7 Control of the double-integrator plant using estimated states. The states and the estimated states are shown for a (a) second-order observer; (b) reduced-order observer.
