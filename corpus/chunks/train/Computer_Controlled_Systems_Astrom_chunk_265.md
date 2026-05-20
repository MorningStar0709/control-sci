# Generation of the Feedforward Signal

Given the model (4.54) it is straightforward to generate the desired states. It remains to discuss generation of the signal $u_{ff}$ . Let the pulse-transfer functions of the process and the model be $H(z)$ and $H_{m}(z)$ , respectively. If the signal

$$u _ {f f} (k) = \frac {H _ {m} (q)}{H (q)} u _ {c} (k) \tag {4.56}$$

could be generated it would give the desired result, several conditions are required for this. The model $H_{m}$ must be stable, the pole excess of the model must not be less than the pole excess of the process, and unstable process zeros must also be zeros of the model.

In the single-input-single-output case the generation of $u_{ff}$ is particularly simple if the order and the zeros of the model and the process are the same. Assume that $H(z) = B(z)/A(z)$ and $H_{m}(z) = \lambda B(z)/A_{m}(z)$ then Eq. (4.56) becomes

$$u _ {f f} (k) = \lambda \frac {A (q)}{A _ {m} (q)} u _ {c} (k) = \lambda \left(1 + \frac {\left(a _ {1} - a _ {1} ^ {m}\right) q ^ {n - 1} + \cdots + \left(a _ {n} - a _ {n} ^ {m}\right)}{q ^ {n} + a _ {1} ^ {m} q ^ {n - 1} + \cdots + a _ {n} ^ {m}}\right) u _ {c} (k) \tag {4.57}$$

The signal $u_{ff}$ then can be generated from the states of the reference model. Generation of feedforward signals is simplified even further if the reference model (4.54) has reachable canonical form, that is,

$$
\Phi_ {m} = \left( \begin{array}{c c c c c} - a _ {1} ^ {m} & - a _ {2} ^ {m} & \dots & - a _ {n - 1} ^ {m} & - a _ {n} ^ {m} \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right) \quad \Gamma_ {m} = \left( \begin{array}{l} \lambda \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right) \tag {4.58}
$$

It then follows from Eq. (4.57) that

$$u _ {f f} = \lambda u _ {c} (k) + C _ {f f} x _ {m} (k) \tag {4.59}$$

where

$$
C _ {f f} = \left( \begin{array}{l l l l} a _ {1} - a _ {1} ^ {m} & a _ {2} - a _ {2} ^ {m} & \dots & a _ {n} - a _ {n} ^ {m} \end{array} \right) \tag {4.60}
$$

Having obtained the closed-form solution we can obtain other representations by transforming the state variables.

A full discussion of design of feedforward compensation is outside the scope of this book. Let it suffice to mention that it is often useful to introduce nonlinearities in the feedforward path so that the system is not driven too hard in response to command signals. Because the signal $u_{ff}$ is used mostly to get the system to move rapidly in the right way it is also possible to use approximate process models; small deviations are easily handled by the feedback.
