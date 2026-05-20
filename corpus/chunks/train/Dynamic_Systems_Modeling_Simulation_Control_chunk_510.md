We can analyze the response of the PUH mass by using the transfer function that relates PUH displacement $x _ { 1 }$ to frame displacement $x _ { \mathrm { i n } } ( t )$ , or $G ( s ) = X _ { 1 } ( s ) / X _ { \mathrm { i n } } ( s )$ . However, the mathematical model consists of two coupled second-order ODEs and, therefore, we must manipulate both modeling equations in order to develop an I/O equation with PUH displacement $x _ { 1 }$ as the single output and frame displacement $x _ { \mathrm { i n } } ( t )$ as the single input (see Problem 5.35). The first step is to apply the differential or D operator to the mathematical model to yield

PUH: $( m _ { 1 } D ^ { 2 } + b _ { 1 } D + k _ { 1 } ) x _ { 1 } = ( b _ { 1 } D + k _ { 1 } ) x _ { 2 }$ (9.64)

Chassis/cart: $\begin{array} { r } { \big ( m _ { 2 } D ^ { 2 } + ( b _ { 1 } + b _ { 2 } ) D + k _ { 1 } + k _ { 2 } \big ) x _ { 2 } = ( b _ { 1 } D + k _ { 1 } ) x _ { 1 } + ( b _ { 2 } D + k _ { 2 } ) x _ { \mathrm { i n } } ( t ) } \end{array}$ (9.65)

Next, we can solve Eq. (9.65) for the chassis/cart position $x _ { 2 }$ and substitute the result into Eq. (9.64), which will yield an equation in terms of $x _ { 1 }$ and $x _ { \mathrm { i n } } ( t )$ . After some algebra, the following I/O equation is obtained by noting that $D x _ { 1 } = \dot { x } _ { 1 } , D ^ { 2 } x _ { 1 } = \ddot { x } _ { 1 }$ , etc.

$$a _ {4} x _ {1} ^ {(4)} + a _ {3} \ddot {x} _ {1} + a _ {2} \ddot {x} _ {1} + a _ {1} \dot {x} _ {1} + a _ {0} x _ {1} = c _ {2} \ddot {x} _ {\text { in }} (t) + c _ {1} \dot {x} _ {\text { in }} (t) + c _ {0} x _ {\text { in }} (t) \tag {9.66}$$

where the left- and right-hand-side coefficients are

$$
\begin{array}{l} a _ {4} = m _ {1} m _ {2} \\ a _ {3} = m _ {1} (b _ {1} + b _ {2}) + m _ {2} b _ {1} \\ a _ {2} = m _ {1} (k _ {1} + k _ {2}) + m _ {2} k _ {1} + b _ {1} b _ {2} \\ a _ {1} = b _ {1} k _ {2} + b _ {2} k _ {1} \\ a _ {0} = k _ {1} k _ {2} \\ c _ {2} = b _ {1} b _ {2} \\ c _ {1} = b _ {1} k _ {2} + b _ {2} k _ {1} = a _ {1} \\ c _ {0} = k _ {1} k _ {2} = a _ {0} \\ \end{array}
$$

Hence, the transfer function can be derived from the I/O equation (9.66)

$$G (s) = \frac {X _ {1} (s)}{X _ {\mathrm{in}} (s)} = \frac {c _ {2} s ^ {2} + c _ {1} s + c _ {0}}{a _ {4} s ^ {4} + a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s + a _ {0}} \tag {9.67}$$

Note that because $c _ { 0 } = a _ { 0 }$ the DC gain is unity and, therefore, the amplitude of low-frequency frame vibrations will be transmitted without gain or attenuation to vibrations in the PUH mass. Table 9.2 presents numerical values for mass, stiffness, and friction that are representative of an optical drive system [6].

Using the values in Table 9.2, the transfer function (9.67) becomes
