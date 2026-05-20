# 7.1 Constrained Optimal Control

![](image/0f50156d96170d35ae2da9f98bd1b8e5ed41789825b4e7ddead6a8e1716ddcbb.jpg)

<details>
<summary>line</summary>

| t | Value |
| --- | --- |
| t0 | +1 |
| t1 | -1 |
| T1 | 0 |
| T2 | 0 |
| t2 | +1 |
| tf* | -1 |
</details>

Figure 7.4 Singular Time-Optimal Control System

\- Step 7: Bang-Bang Control Law: For a normal time-optimal system, the optimal control, given by (7.1.27)

$$\boxed {\mathbf {u} ^ {*} (t) = - S G N \{\mathbf {q} ^ {*} (t) \} = - S G N \{\mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \}} \tag {7.1.31}$$

for all $t \in [t_{0}, t_{f}^{*}]$ , is a piecewise constant function of time (i.e., bang-bang).

\- Step 8: Conditions for NTOC System: Here, we derive the conditions necessary for the system to be not singular, thereby obtaining the conditions for the system to be normal. First of all, the solution of the costate equation (7.1.19) is

$$\boldsymbol {\lambda} ^ {*} (t) = \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) \tag {7.1.32}$$

and assume that the costate initial condition $\boldsymbol{\lambda}^{*}(0)$ must be a nonzero vector. With this solution for $\boldsymbol{\lambda}^{*}(t)$ , the control law (7.1.31) becomes

$$\mathbf {u} ^ {*} (t) = - S G N \{\mathbf {B} ^ {\prime} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) \} \tag {7.1.33}$$

or component wise,

$$
\begin{array}{l} u _ {j} ^ {*} (t) = - s g n \{q _ {j} ^ {*} (t) \}, \\ = - s g n \left\{\mathbf {b} _ {j} ^ {\prime} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) \right\}. \tag {7.1.34} \\ \end{array}
$$

Let us suppose that there is an interval of time $[T_{1}, T_{2}]$ during which the function $\mathbf{q}^{*}(t)$ is zero. Then, it follows that during the time interval $[T_{1}, T_{2}]$ all the derivatives of $\mathbf{q}^{*}(t)$ must be zero. That is
