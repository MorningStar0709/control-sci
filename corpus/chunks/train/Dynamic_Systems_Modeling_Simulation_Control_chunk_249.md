# Example 5.15

Equation (5.106) is the transfer function for output variable y(t) and input variable u(t)

$$G (s) = \frac {7 s + 4}{2 s ^ {2} + 1 0 s + 2 8} = \frac {Y (s)}{U (s)} \tag {5.106}$$

Derive the time-domain ODE for the I/O equation of this system.

To begin, rewrite the transfer function G(s) with Laplace variable s replaced by the differential operator D

$$\frac {7 D + 4}{2 D ^ {2} + 1 0 D + 2 8} = \frac {y (t)}{u (t)} \tag {5.107}$$

Cross multiplying the denominator term in Eq. (5.107) $( 2 D ^ { 2 } + 1 0 D + 2 8 )$ by the output y and the numerator term (7D + 4) by the input u yields

$$(2 D ^ {2} + 1 0 D + 2 8) y = (7 D + 4) u \tag {5.108}$$

Finally, apply the differential operator to produce the time derivative terms $D ^ { 2 } y = \ddot { y } , D y = \dot { y } ,$ , and $D u = \dot { u }$ , which yields the differential equation

$$2 \ddot {y} + 1 0 \dot {y} + 2 8 y = 7 \dot {u} + 4 u \tag {5.109}$$

Equation (5.109) is the desired I/O equation, the equivalent to the transfer function shown in Eq. (5.106). We can divide the I/O equation by 2 if we desire a unity coefficient on the highest derivative term, which yields the equivalent I/O equation

$$\ddot {y} + 5 \dot {y} + 1 4 y = 3. 5 \dot {u} + 2 u \tag {5.110}$$

With enough practice, the reader should be able to develop transfer functions directly from I/O equations (and vice versa) without relying on the intermediate step with the D operator.
