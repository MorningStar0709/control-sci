# 4.5 Frequency-Domain Interpretation

In this section, we use frequency domain to derive some results from the classical control point of view for a linear, time-invariant, continuous-time, optimal control system with infinite-time horizon case. For this, we know that the closed-loop optimal control involves the solution of matrix algebraic Riccati equation $[89, 3]$ . For ready reference, we repeat here some of the results of Chapter 3.

Consider a controllable, linear, time-invariant plant

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t), \tag {4.5.1}$$

and the infinite-time interval cost functional

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) ] d t. \tag {4.5.2}$$

The optimal control is given by

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {x} ^ {*} (t) = - \bar {\mathbf {K}} \mathbf {x} ^ {*} (t), \tag {4.5.3}$$

where, $\bar{K} = R^{-1}B'\bar{P}$ , and $\bar{P}$ , the nxn constant, positive definite, symmetric matrix, is the solution of the nonlinear, matrix ARE

$$- \bar {\mathbf {P}} \mathbf {A} - \mathbf {A} ^ {\prime} \bar {\mathbf {P}} + \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} - \mathbf {Q} = 0. \tag {4.5.4}$$

The optimal trajectory (state) is the solution of

$$\dot {\mathbf {x}} ^ {*} (t) = \left(\mathbf {A} - \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}}\right) \mathbf {x} ^ {*} (t) = \left(\mathbf {A} - \mathbf {B} \bar {\mathbf {K}}\right) \mathbf {x} ^ {*} (t), \tag {4.5.5}$$

which is asymptotically stable. Here, we assume that $[A,B]$ is stabilizable and $[A,\sqrt{Q}]$ is observable. Then, the open-loop characteristic polynomial of the system is [89]

$$\boldsymbol {\Delta} _ {o} (s) = | s \mathbf {I} - \mathbf {A} |, \tag {4.5.6}$$

where, $s$ is the Laplace variable and the optimal closed-loop characteristic polynomial is

$$
\begin{array}{l} \boldsymbol {\Delta} _ {c} (s) = | s \mathbf {I} - \mathbf {A} + \mathbf {B} \bar {\mathbf {K}} | \\ = | \mathbf {I} + \mathbf {B} \bar {\mathbf {K}} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} |. | s \mathbf {I} - \mathbf {A} |, \\ = | \mathbf {I} + \bar {\mathbf {K}} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} | \boldsymbol {\Delta} _ {o} (s). \tag {4.5.7} \\ \end{array}
$$
