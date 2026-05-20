In the case of a multivariable system, there are more free parameters in the state feedback gain matrix than there are eigenvalues. That freedom can be used either to achieve desirable eigenvectors $[1, 2]$ or to achieve other desirable properties $[3]$ .

Since closed-loop poles can be chosen arbitrarily, one might wonder why they should not be placed so far into the LHP that transient times are negligible. The reason is that it takes large gain values to move poles far away from their open-loop positions.

![](image/110449af630baacb2bfe9fabf09679968edb305b1caba33c281a21dd4006a7a8.jpg)

<details>
<summary>line</summary>

| Time (s) | Angle (rad) | Distance (m) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.2 |
| 0.5 | 0.55 | -0.15 |
| 1.0 | 0.4 | 0.0 |
| 1.5 | 0.1 | 0.05 |
| 2.0 | -0.05 | 0.0 |
| 2.5 | -0.02 | 0.0 |
| 3.0 | 0.0 | 0.0 |
| 3.5 | 0.0 | 0.0 |
| 4.0 | 0.0 | 0.0 |
| 4.5 | 0.0 | 0.0 |
| 5.0 | 0.0 | 0.0 |
</details>

Figure 7.4 Time responses for pole-placement state feedback, pendulum-on-cart

Figure 7.2 shows the situation in closed-loop unit-feedback form. The loop gain is $L(s) = K(sI - A)^{-1}B$ . If the elements of K are large, $L(j\omega)$ will tend to be large over a relatively large range of $\omega$ , and the complementary sensitivity $T(j\omega)$ for the closed loop will be near unity over a large frequency range. From the results of Chapter 5, Section 5.6, the system will not be robust unless the model is relatively good to frequencies extending beyond the bandwidth. It follows that the closed-loop poles chosen should not produce bandwidths extending beyond the range of validity of the model.
