# Output Prediction

One basic idea in the predictive control algorithms is to rewrite the process model to get an explicit expression for the output at a future time. Compare Eq. (4.22). Consider the deterministic process

$$A ^ {*} (q ^ {- 1}) y (t) = B ^ {*} (q ^ {- 1}) u (t - d _ {0}) \tag {4.50}$$

and introduce the identity

$$1 = A ^ {*} (q ^ {- 1}) F _ {d} ^ {*} (q ^ {- 1}) + q ^ {- d} G _ {d} ^ {*} (q ^ {- 1}) \tag {4.51}$$

where

$$\deg F _ {d} ^ {*} = d - 1\deg G _ {d} ^ {*} = n - 1$$

The subscript d is used to indicate that the prediction horizon is d steps. It is assumed that $d \geq d_{0}$ . The polynomial identity of Eq. (4.51) can be used to predict the output d steps ahead. Hence

$$y (t + d) = A ^ {*} F _ {d} ^ {*} y (t + d) + G _ {d} ^ {*} y (t) = B ^ {*} F _ {d} ^ {*} u (t + d - d _ {0}) + G _ {d} ^ {*} y (t) \tag {4.52}$$

Compare Eq. (4.12). Introduce

$$B ^ {*} (q ^ {- 1}) F _ {d} ^ {*} (q ^ {- 1}) = R _ {d} ^ {*} (q ^ {- 1}) + q ^ {- (d - d _ {0} + 1)} \bar {R} _ {d} ^ {*} (q ^ {- 1})$$

where

$$\deg R _ {d} ^ {*} = d - d _ {0}\deg \bar {R} _ {d} ^ {*} = n - 2$$

The coefficients of $R_{d}^{*}$ are the first $d - d_{0} + 1$ terms of the pulse response of the open-loop system. This can be seen as follows:

$$
\begin{array}{l} \frac {q ^ {- d _ {0}} B ^ {*}}{A ^ {*}} = q ^ {- d _ {0}} B ^ {*} \left(F _ {d} ^ {*} + q ^ {- d} \frac {G _ {d} ^ {*}}{A ^ {*}}\right) \\ = q ^ {- d _ {0}} R _ {d} ^ {*} \left(q ^ {- 1}\right) + q ^ {- (d + 1)} \bar {R} _ {d} ^ {*} \left(q ^ {- 1}\right) + \frac {B ^ {*} \left(q ^ {- 1}\right) G _ {d} ^ {*} \left(q ^ {- 1}\right)}{A ^ {*} \left(q ^ {- 1}\right)} q ^ {- (d + d _ {0})} \tag {4.53} \\ \end{array}
$$

The powers of the last two terms are at least $-(d+1)$ . It then follows that $R_{d}^{*}$ is the first part of the pulse response, since $\deg R_{d}^{*}=d-d_{0}$ .

Equation (4.52) can be written as

$$
\begin{array}{l} y (t + d) = R _ {d} ^ {*} \left(q ^ {- 1}\right) u \left(t + d - d _ {0}\right) + \bar {R} _ {d} ^ {*} \left(q ^ {- 1}\right) u (t - 1) + G _ {d} ^ {*} \left(q ^ {- 1}\right) y (t) \\ = R _ {d} ^ {*} \left(q ^ {- 1}\right) u (t + d - d _ {0}) + \bar {y} _ {d} (t) \tag {4.54} \\ \end{array}
$$
