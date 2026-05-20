Now, using the signum function (see Figure 7.1) defined between input $f_{i}$ and output $f_{0}$ , written as $f_{o} = \text{sgn}\{f_{i}\}$ as

$$
f _ {0} = \left\{ \begin{array}{l l} + 1 & \text {if} f _ {i} > 0 \\ - 1 & \text {if} f _ {i} <   0 \\ \text {indeterminate} & \text {if} f _ {i} = 0. \end{array} \right.
$$

The engineering realization of the signum function is an ideal relay.

Then, we can write the control algorithm (7.1.26) in a compact form as

$$\boxed {\mathbf {u} ^ {*} (t) = - S G N \{\mathbf {q} ^ {*} (t) \}} \tag {7.1.27}$$

![](image/5a443b114093e1a7bbc74b85429715b74af61dfe96a120c57e798af409382100.jpg)

<details>
<summary>line</summary>

| f_i | f_o |
| --- | --- |
| -1 | -1 |
| 0 | +1 |
| +1 | +1 |
</details>

Figure 7.1 Signum Function   
![](image/7dd7145a1c2758d6a08a3ca84ec080d6da9f6e8861e69084b02a7b5436ea9b8b.jpg)

<details>
<summary>text_image</summary>

-q*(t)
-1
+1
-1
+1
u*(t)
</details>

Figure 7.2 Time-Optimal Control

where the relation between the time-optimal control $\mathbf{u}^{*}(t)$ and the function $\mathbf{q}^{*}(t)$ is shown in Figure 7.2.

In terms of component wise,

$$
\begin{array}{l} u _ {j} ^ {*} (t) = - s g n \{q _ {j} ^ {*} (t) \} \\ = - s g n \{\mathbf {b} _ {j} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \} \tag {7.1.28} \\ \end{array}
$$

where, $b_{j}, j = 1, 2, \ldots, r$ denote the column vectors of the input matrix B. From the time-optimal control relation (7.1.27), note that the optimal control $\mathbf{u}^{*}(t)$ depends on the costate function $\boldsymbol{\lambda}^{*}(t)$ .

\- Step 6: Types of Time-Optimal Controls: We now have two types of time-optimal controls, depending upon the nature of the function $\mathbf{q}^{*}(t)$ .

1. Normal Time-Optimal Control (NTOC) System: Suppose that during the interval $[t_{0}, t_{f}^{*}]$ , there exists a set of times $t_1, t_2, \ldots, t_{\gamma j} \in [t_0, t_f], \quad \gamma = 1, 2, 3, \ldots, j = 1, 2, \ldots, r$ such that

$$
q _ {j} ^ {*} (t) = \mathbf {b} _ {j} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = \left\{ \begin{array}{l l} 0, & \text { if   and   only   if } t = t _ {\gamma j} \\ \text { nonzero }, & \text { otherwise }, \end{array} \right. \tag {7.1.29}
$$

then we have a normal time-optimal control (NTOC) system. The situation is depicted in Figure 7.3. Here, the

![](image/c58f0193bbde159452cf8afb70b2cb847eb4828e7988795a807feb28ea8e023c.jpg)

<details>
<summary>line</summary>
