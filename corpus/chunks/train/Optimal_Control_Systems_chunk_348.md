# Previous to Last Stage: $k = k_{f} - 1$

At $i = k_{f} - 1$ , the cost function (6.3.16) becomes

$$
\begin{array}{l} J _ {k _ {f} - 1} = \frac {1}{2} \mathbf {x} ^ {\prime} \left(k _ {f} - 1\right) \mathbf {Q x} \left(k _ {f} - 1\right) + \frac {1}{2} \mathbf {u} ^ {\prime} \left(k _ {f} - 1\right) \mathbf {R u} \left(k _ {f} - 1\right) \\ + \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F} \mathbf {x} (k _ {f}). \tag {6.3.18} \\ \end{array}
$$

According to the functional equation of the principle of optimality (6.3.4), we need to find the optimal control $\mathbf{u}^{*}(k_{f}-1)$ to minimize the cost function (6.3.18). Before that, let us rewrite the relation (6.3.18) to make all the terms in (6.3.18) to belong to stage $k_{f}-1$ . For this, using (6.3.15) in (6.3.18), we have

$$J _ {k _ {f} - 1} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f} - 1) \mathbf {Q x} (k _ {f} - 1) + \frac {1}{2} \mathbf {u} ^ {\prime} (k _ {f} - 1) \mathbf {R u} (k _ {f} - 1)+ \frac {1}{2} \left[ \mathbf {A x} \left(k _ {f} - 1\right) + \mathbf {B u} \left(k _ {f} - 1\right) \right] ^ {\prime} \mathbf {F} \left[ \mathbf {A x} \left(k _ {f} - 1\right) + \mathbf {B u} \left(k _ {f} - 1\right) \right]. \tag {6.3.19}$$

Since there are no constraints on states or controls, we can easily find the minimum value of (6.3.19) w.r.t. $\mathbf{u}(k_f - 1)$ by simply making

$$\frac {\partial J _ {k _ {f} - 1}}{\partial \mathbf {u} (k _ {f} - 1)} = \mathbf {R u} ^ {*} (k _ {f} - 1) + \mathbf {B} ^ {\prime} \mathbf {F} [ \mathbf {A x} (k _ {f} - 1) + \mathbf {B u} ^ {*} (k _ {f} - 1) ] = 0. \tag {6.3.20}$$

Solving for $\mathbf{u}^{*}(k_{f} - 1)$ , we have

$$
\begin{array}{l} \mathbf {u} ^ {*} \left(k _ {f} - 1\right) = - \left[ \mathbf {R} + \mathbf {B} ^ {\prime} \mathbf {F B} \right] ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {F A x} \left(k _ {f} - 1\right) \\ = - \mathbf {L} (k _ {f} - 1) \mathbf {x} (k _ {f} - 1) \tag {6.3.21} \\ \end{array}
$$

where,

$$\mathbf {L} \left(k _ {f} - 1\right) = \left[ \mathbf {R} + \mathbf {B} ^ {\prime} \mathbf {F B} \right] ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {F A} \tag {6.3.22}$$

is also called the Kalman gain. Now the optimal cost $J_{k_{f}-1}^{*}$ for this stage $k_{f}-1$ is found by substituting the optimal control $\mathbf{u}^{*}(k_{f}-1)$ from (6.3.21) into the cost function (6.3.19) to get
