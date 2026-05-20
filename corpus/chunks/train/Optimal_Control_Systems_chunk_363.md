$$
\begin{array}{l} \frac {1}{2} \mathbf {x} ^ {\prime} (t) \dot {\mathbf {P}} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {x} (t) \mathbf {Q} (t) \mathbf {x} (t) \\ - \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} (t) \\ + \mathbf {x} ^ {\prime} (t) \mathbf {P} (t) \mathbf {A} (t) \mathbf {x} (t) = 0. \tag {6.5.13} \\ \end{array}
$$

Expressing $\mathbf{P}(t)\mathbf{A}(t)$ as

$$
\begin{array}{l} \mathbf {P} (t) \mathbf {A} (t) = \frac {1}{2} \left[ \mathbf {P} (t) \mathbf {A} (t) + \{\mathbf {P} (t) \mathbf {A} (t) \} ^ {\prime} \right] \\ + \frac {1}{2} \left[ \mathbf {P} (t) \mathbf {A} (t) - \{\mathbf {P} (t) \mathbf {A} (t) \} ^ {\prime} \right], \tag {6.5.14} \\ \end{array}
$$

where, the first term on the right-hand side of the above expression is symmetric and the second term is not symmetric. Also, we can easily show that since all the terms, except the last term on the right-hand side of (6.5.13), are symmetric. Using (6.5.14) in (6.5.13), we have

$$
\begin{array}{l} \frac {1}{2} \mathbf {x} ^ {\prime} (t) \dot {\mathbf {P}} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {x} (t) \mathbf {Q} (t) \mathbf {x} (t) \\ - \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} (t) \\ + \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {P} (t) \mathbf {A} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} (t) = 0. \tag {6.5.15} \\ \end{array}
$$

This equation should be valid for any $\mathbf{x}(t)$ , which then reduces to

$$
\begin{array}{l} \dot {\mathbf {P}} (t) + \mathbf {Q} (t) - \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \\ + \mathbf {P} (t) \mathbf {A} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) = 0. \\ \end{array}
$$

(6.5.16)

Rewriting the above, we have the matrix differential Riccati equation (DRE) as

$$\boxed {\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) - \mathbf {Q} (t).} \tag {6.5.17}$$

Using (6.5.10) and (6.5.11),
