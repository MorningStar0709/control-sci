# 1.4.4 Moving Horizon Estimation

When using nonlinear models or considering constraints on the estimates, we cannot calculate the conditional density recursively in closed form as we did in Kalman filtering. Similarly, we cannot solve recursively the least squares problem. If we use least squares we must optimize all the states in the trajectory x(T ) simultaneously to obtain the state estimates. This optimization problem becomes computationally intractable as T increases. Moving horizon estimation (MHE) removes this difficulty by considering only the most recent N measurements and finds only the most recent N values of the state trajectory as sketched in Figure 1.4. The states to be estimated are $\mathbf { x } _ { N } ( T ) = \{ x ( T - N ) , \ldots , x ( T ) \}$ given measurements $\mathbf { y } _ { N } ( T ) ~ = ~ \{ y ( T - N ) , \ldots , y ( T ) \}$ . The data have been broken into two sections with $\{ \mathbf { y } ( T - N - 1 ) , \mathbf { y } _ { N } ( T ) \} = \mathbf { y } ( T )$ . We assume here that $T \geq N - 1$ to ignore the initial period in which the estimation window fills with measurements and assume that the window is always full.

![](image/37091dbe51a5ece16a2837b0253632b77575035a52948b4e8bf3c0d5f87e018f.jpg)

<details>
<summary>line</summary>

| Time Point | y(T) | x(T) |
| --- | --- | --- |
| T - N | N | N |
| T | N | N |
| T-N | N | N |
| T | T | T |
</details>

Figure 1.4: Schematic of the moving horizon estimation problem.

The simplest form of MHE is the following least squares problem

$$\min _ {\mathbf {x} _ {N} (T)} \hat {V} _ {T} (\mathbf {x} _ {N} (T)) \tag {1.33}$$

in which the objective function is

$$
\begin{array}{l} \hat {V} _ {T} \left(\mathbf {x} _ {N} (T)\right) = \frac {1}{2} \left(\sum_ {k = T - N} ^ {T - 1} | x (k + 1) - A x (k) | _ {Q ^ {- 1}} ^ {2} + \right. \\ \left. \sum_ {k = T - N} ^ {T} | y (k) - C x (k) | _ {R ^ {- 1}} ^ {2}\right) \tag {1.34} \\ \end{array}
$$

We use the circumflex (hat) to indicate this is the MHE cost function considering data sequence from $T - N$ to T rather than the full information or least squares cost considering the data from 0 to T .

MHE in terms of least squares. Notice that from our previous DP recursion in (1.30), we can write the full least squares problem as

$$
\begin{array}{l} V _ {T} (\mathbf {x} _ {N} (T)) = V _ {T - N} ^ {-} (x (T - N)) + \\ \frac {1}{2} \left(\sum_ {k = T - N} ^ {T - 1} | x (k + 1) - A x (k) | _ {Q ^ {- 1}} ^ {2} + \sum_ {k = T - N} ^ {T} | y (k) - C x (k) | _ {R ^ {- 1}} ^ {2}\right) \\ \end{array}
$$
