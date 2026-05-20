$$
\begin{array}{l} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + [ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} ] \bar {\mathbf {L}} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \bar {\mathbf {P}} ^ {\prime} [ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} ] \\ + \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \bar {\mathbf {L}} ^ {- T} [ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} ] \bar {\mathbf {L}} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B}, \\ = \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \mathbf {Q} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B}. \tag {5.6.12} \\ \end{array}
$$

Now, adding the positive definite matrix $\mathbf{R}$ to both sides of the previous equation and factoring we get

$$
\begin{array}{l} \mathbf {B} ^ {\prime} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ^ {\prime} ] ^ {- 1} \mathbf {Q} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {R} \\ = \left[ \mathbf {I} + \bar {\mathbf {L}} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right] ^ {\prime} \left[ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] \left[ \mathbf {I} + \bar {\mathbf {L}} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right]. \tag {5.6.13} \\ \end{array}
$$

With fictitious output equation as

$$\mathbf {y} (k) = \mathbf {C x} (k) + \mathbf {D u} (k) \tag {5.6.14}$$

where, $Q = C'C$ and $R = D'D$ , and using (5.6.1), the transfer function relating the output $\mathbf{y}(k)$ and the control $\mathbf{u}^{*}(k)$ becomes

$$
\mathbf {Y} (z) = \left[ \begin{array}{c} \mathbf {C} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \\ \mathbf {D} \end{array} \right] \mathbf {U} (z). \tag {5.6.15}
$$

Also, we see that

$$
\begin{array}{l} \left[ \begin{array}{c} \mathbf {C} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \\ \mathbf {D} \end{array} \right] ^ {\prime} \left[ \begin{array}{c} \mathbf {C} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \\ \mathbf {D} \end{array} \right] \\ = \mathbf {B} [ z ^ {- 1} \mathbf {I} - \mathbf {A} ] ^ {- T} \mathbf {Q} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {R}. \tag {5.6.16} \\ \end{array}
$$

Then, we can easily see from $(5.6.13)$ that the previous transfer function product can be expressed in terms of the return difference matrix. Hence, the relation $(5.6.15)$ implies that Figure 5.17 shows a return difference product.
