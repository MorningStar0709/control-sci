$$\hat {J} = \frac {1}{2} \int_ {t _ {0}} ^ {\infty} \left[ \hat {\mathbf {x}} ^ {\prime} (t) \mathbf {Q} \hat {\mathbf {x}} (t) + \hat {\mathbf {u}} ^ {\prime} (t) \mathbf {R} \hat {\mathbf {u}} (t) \right] d t. \tag {4.4.5}$$

Considering the minimization of the modified system defined by $(4.4.4)$ and $(4.4.5)$ , we see that the optimal control is given by (see Chapter 3, Table 3.3)

$$\hat {\mathbf {u}} ^ {*} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \hat {\mathbf {x}} ^ {*} (t) = - \bar {\mathbf {K}} \hat {\mathbf {x}} ^ {*} (t) \tag {4.4.6}$$

where, $\bar{K} = R^{-1}B'\bar{P}$ and the matrix $\bar{P}$ is the positive definite, symmetric solution of the algebraic Riccati equation

$$\bar {\mathbf {P}} (\mathbf {A} + \alpha \mathbf {I}) + (\mathbf {A} ^ {\prime} + \alpha \mathbf {I}) \bar {\mathbf {P}} - \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} + \mathbf {Q} = 0. \tag {4.4.7}$$

Using the optimal control (4.4.6) in the modified system (4.4.4), we get the optimal closed-loop system as

$$\dot {\hat {\mathbf {x}}} ^ {*} (t) = (\mathbf {A} + \alpha \mathbf {I} - \mathbf {B R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}}) \hat {\mathbf {x}} ^ {*} (t). \tag {4.4.8}$$

Now, we can simply apply these results to the original system. Thus, using the transformations (4.4.3) in (4.4.6), the optimal control of the original system (4.4.1) and the associated performance measure (4.4.2) is given by

$$
\begin{array}{l} \mathbf {u} ^ {*} (t) = e ^ {- \alpha t} \hat {\mathbf {u}} ^ {*} (t) = - e ^ {- \alpha t} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} e ^ {\alpha t} \mathbf {x} ^ {*} (t) \\ = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {x} ^ {*} (t) = - \bar {\mathbf {K}} \mathbf {x} ^ {*} (t). \tag {4.4.9} \\ \end{array}
$$

Interestingly, this desired (original) optimal control (4.4.9) has the same structure as the optimal control (4.4.6) of the modified system. The optimal performance index for original system or modified system is the same and equals to

$$\hat {J} ^ {*} = \frac {1}{2} \hat {\mathbf {x}} ^ {* \prime} (t _ {0}) \bar {\mathbf {P}} \hat {\mathbf {x}} ^ {*} (t _ {0})J ^ {*} = \frac {1}{2} e ^ {2 \alpha t _ {0}} \mathbf {x} ^ {* \prime} (t _ {0}) \bar {\mathbf {P}} \mathbf {x} ^ {*} (t _ {0}). \tag {4.4.10}$$

We see that the closed-loop optimal control system (4.4.8) has eigenvalues with real parts less than $-\alpha$ . In other words, the state $\mathbf{x}^{*}(t)$ approaches zero at least as fast as $e^{-\alpha t}$ . Then, we say that the closed-loop optimal system (4.4.8) has a degree of stability of at least $\alpha$ .
