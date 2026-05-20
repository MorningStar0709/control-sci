Now, (7.5.17) implies that (using (7.5.21))

$$
\begin{array}{l} \min _ {| \mathbf {u} (t) | \leq 1} \left\{\mathbf {w} ^ {\prime} (t) \mathbf {R} (t) \mathbf {w} (t) \right\} = \min _ {| \mathbf {u} (t) | \leq 1 |} \left\{\sum_ {j = 1} ^ {r} d _ {j} (t) v _ {j} ^ {2} (t) \right\} \\ = \sum_ {j = 1} ^ {r} \min _ {v _ {j} (t)} \left\{v _ {j} ^ {2} (t) \right\}. \tag {7.5.24} \\ \end{array}
$$

This implies that if $\mathbf{w}^{*}(t)$ minimizes $\mathbf{w}'(t)\mathbf{R}(t)\mathbf{w}(t)$ , then the components $\mathbf{v}_{j}(t)$ also minimize $\mathbf{v}'(t)\mathbf{v}(t)$ . This fact is also evident from (7.5.22). In other words, we have established that

$$\text { if } \quad \mathbf {w} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {w} ^ {*} (t) \leq \mathbf {w} ^ {\prime} (t) \mathbf {R} (t) \mathbf {w} (t)\text { then } \quad \mathbf {w} ^ {* \prime} (t) \mathbf {w} ^ {*} (t) \leq \mathbf {w} ^ {\prime} (t) \mathbf {w} (t) \tag {7.5.25}$$

and the converse is also true. Or the effect of $\mathbf{R}(t)$ is nullified in the minimization process. Thus,

$$
\begin{array}{l} \min _ {| \mathbf {u} (t) | \leq 1 |} \left\{\mathbf {w} ^ {\prime} (t) \mathbf {R} (t) \mathbf {w} (t) \right\} = \min _ {| \mathbf {u} (t) | \leq 1 |} \left\{\mathbf {w} ^ {\prime} (t) \mathbf {w} (t) \right\}, \\ = \sum_ {j = 1} ^ {r} \min _ {\mathbf {w} (t)} \left\{w _ {j} ^ {2} (t) \right\}, \\ = \sum_ {j = 1} ^ {r} \min _ {| \mathbf {u} (t) | \leq 1 |} \left\{\left[ u _ {j} (t) + q _ {j} ^ {*} (t) \right] ^ {2} \right\}. \tag {7.5.26} \\ \end{array}
$$

A careful examination of (7.5.26) reveals that to minimize the positive quantity $[u_j(t) + q_j^*(t)]^2$ , we must select

$$
u ^ {*} (t) = \left\{ \begin{array}{c c c} - q _ {j} ^ {*} (t) & \text { if } & | q _ {j} ^ {*} (t) | \leq 1, \\ + 1 & \text { if } & q _ {j} ^ {*} (t) <   - 1, \\ - 1 & \text { if } & q _ {j} ^ {*} (t) > + 1. \end{array} \right. \tag {7.5.27}
$$

First, let us define $sat\{\}$ as the saturation function between the input $f_{i}$ and the output $f_{o}$ (see Figure 7.36) as $f_{o} = sat\{f_{i}\}$ means that

$$
f _ {o} = \left\{ \begin{array}{l l} f _ {i} & \text { if } \quad | f _ {i} | \leq 1 \\ s g n \left\{f _ {i} \right\} & \text { if } \quad | f _ {i} | > 1. \end{array} \right. \tag {7.5.28}
$$

The sgn function is already defined in Section 7.1.1. Then the

![](image/e90b2729bb53bb61ee255a3cb26e2446d68fc194c36acfe94ab4cc43950e4760.jpg)

<details>
<summary>line</summary>

| f_i | f_o |
| --- | --- |
| -1 | -1 |
| 0 | 0 |
| +1 | +1 |
</details>

Figure 7.36 Saturation Function
