# Constant Future Control

Consider Eq. (4.54) and assume that the predicted output is equal to the desired output, that is, $y(t + d) = y_{m}(t + d)$ . If we assume that Eq. (4.55) holds, then $u(t)$ should be chosen such that

$$y _ {m} (t + d) = \left(R _ {d} ^ {*} (1) + q ^ {- 1} \bar {R} _ {d} ^ {*} (q ^ {- 1})\right) u (t) + G _ {d} ^ {*} (q ^ {- 1}) y (t)$$

This gives the control law

$$u (t) = \frac {y _ {m} (t + d) - G _ {d} ^ {*} \left(q ^ {- 1}\right) y (t)}{R _ {d} ^ {*} (1) + \bar {R} _ {d} ^ {*} \left(q ^ {- 1}\right) q ^ {- 1}} \tag {4.57}$$

This control signal is then applied to the process. At the next sampling instant a new measurement is obtained, and the control law of Eq. (4.57) is used again. Note that the value of the control signal is changed rather than kept constant, as was assumed when Eq. (4.57) was derived. The receding-horizon control principle is thus used. Note that the control law is time-invariant, in contrast to a fixed-horizon linear quadratic controller.

We now analyze the closed-loop system when Eq. (4.57) is used to control the process of Eq. (4.50). It is now necessary to make the calculations in the forward shift operator, since poles at the origin may otherwise be overlooked. The identity of Eq. (4.51) can be written in the forward shift operator as

$$q ^ {n + d - 1} = A (q) F _ {d} (q) + G _ {d} (q) \tag {4.58}$$

The characteristic polynomial of the closed-loop system is

$$P (q) = A (q) \left(q ^ {n - 1} R _ {d} (1) + \bar {R} _ {d} (q)\right) + G _ {d} (q) B (q) \tag {4.59}$$

where

$$\deg P = \deg A + n - 1 = 2 n - 1$$

The design equation (Eq. 4.58) can now be used to rewrite $P(q)$ :

$$
\begin{array}{l} B (q) q ^ {n + d - 1} = A (q) B (q) F _ {d} (q) + G _ {d} (q) B (q) \\ = A (q) \left(q ^ {n - 1} R _ {d} (q) + \bar {R} _ {d} (q)\right) + G _ {d} (q) B (q) \\ \end{array}
$$

Hence

$$A (q) \bar {R} _ {d} (q) + G _ {d} (q) B (q) = B (q) q ^ {n \cdot d - 1} - A (q) q ^ {n \cdot 1} R _ {d} (q)$$

which gives

$$P (q) = q ^ {n - 1} A (q) R _ {d} (1) + q ^ {n - 1} \left(q ^ {d} B (q) - A (q) R _ {d} (q)\right)$$

If the process is stable, it follows from Eq. (4.53) that the last term vanishes as $d \to \infty$ . Thus

$$\lim _ {d \rightarrow \infty} P (q) = q ^ {n - 1} A (q) R _ {d} (1) \quad \text { if } A (z) \text { is a stable polynomial }$$

The properties of the predictive control law are illustrated by an example.
