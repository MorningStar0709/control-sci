# DEFINITION

An LTI system is input-output stable if the zero-state output is bounded for all bounded inputs.

Conditions for this type of stability are expressed in terms of the impulse response or its transform, the transfer function.

■ Theorem 3.7 A single-input, single-output LTI system is input–output stable if, and only if, its impulse response $h(t)$ satisfies

$$\int_ {0} ^ {\infty} | h (t) | d t < \infty . \tag {3.84}$$

Proof: To show sufficiency, assume the condition is satisfied. The output is given by the convolution integral,

$$y (t) = \int_ {0} ^ {t} h (\tau) u (t - \tau) d \tau .$$

Let the input be bounded; i.e., let $|u(t - \tau)| \leq M$ . Then

$$| y (t) | \leq \int_ {0} ^ {t} | h (\tau) | | u (t - \tau) | d \tau \leq M \int_ {0} ^ {t} | h (\tau) | d \tau < \infty$$

and $|y(t)|$ is bounded.

To show necessity, we show that, if the condition is violated, it is always possible to construct a bounded input that makes y "blow up." With t fixed, choose

$$
u (t - \tau) = \left\{ \begin{array}{l l} + 1 & \text { if } h (\tau) \geq 0 \\ - 1 & \text { if } h (\tau) <   0. \end{array} \right.
$$

Then $h(\tau)u(t - \tau) = |h(\tau)|$ , and

$$y (t) = \int_ {0} ^ {t} | h (\tau) | d \tau .$$

Since $\lim_{t\to\infty}\int_{0}^{t}|h(\tau)|d\tau=\infty$ , we can make $y(t)$ as large as desired simply by making t sufficiently large. Therefore, $y(t)$ is not bounded for all bounded inputs, and the system is not input–output stable. ■

In the multi-input, multi-output case, all elements of the matrix of impulse responses must satisfy the absolute integrability condition; otherwise, one of the inputs could be excited by a bounded function that would make at least one output grow unbounded.

The condition of Equation 3.84 holds for all LTI systems, lumped or distributed. For the lumped systems of this text, a condition in terms of the transfer function is more easily applicable.
