# The Criterion

It is assumed that the purpose of the control is to keep the output of the system as close as possible to a known reference value trajectory $u_{c}(t)$ . The deviation is measured by the criterion

$$J _ {N} = E \left\{\frac {1}{N} \sum_ {t = 1} ^ {N} (y (t) - u _ {c} (t)) ^ {2} \right\} \tag {7.8}$$

where E denotes mathematical expectation. This is called an N-stage criterion. The loss function should be minimized with respect to $u(0)$ , $u(1)$ , $\ldots$ , $u(N-1)$ . The controller obtained for N = 1 is sometimes called a myopic controller, since it is short-sighted and looks only one step ahead. The minimizing controller will be very different if N = 1 or if N is large.
