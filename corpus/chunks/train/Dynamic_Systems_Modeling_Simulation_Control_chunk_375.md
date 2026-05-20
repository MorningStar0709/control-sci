# Example 7.7

Several LTI second-order I/O equations are given below. Describe the free response for each I/O equation, and (if applicable) estimate the time to reach steady state and the number of periodic oscillations before the free (or transient) response “dies out” to zero.

$( { \bf a } ) ~ 2 \ddot { y } + 2 2 \dot { y } + 4 8 y = 3 u$

The nature of the free response $y _ { H } ( t )$ depends on the characteristic roots, so the starting point is the characteristic equation, which can be written from the inspection of the left-hand side coefficients of the I/O equation

$$2 r ^ {2} + 2 2 r + 4 8 = 0$$

or

$$2 (r ^ {2} + 1 1 r + 2 4) = 2 (r + 3) (r + 8) = 0$$

Therefore, the characteristic roots are $r _ { 1 } = - 3$ and $r _ { 2 } = - 8$ . Immediately we know that the free response will be composed of two decaying exponential functions as both roots are negative real numbers, and the free response will resemble the response in Fig. 7.13a. The free response has the form

$$y _ {H} (t) = c _ {1} e ^ {- 3 t} + c _ {2} e ^ {- 8 t}$$

where the constants $c _ { 1 }$ and $c _ { 2 }$ can be determined from knowledge of the two initial conditions $y _ { 0 }$ and $\dot { y } _ { 0 }$ , which are not provided in this example. The first exponential function $e ^ { - 3 t } = e ^ { - t / 0 . 3 3 3 3 }$ has a time constant $\tau _ { 1 } = 0 . 3 3 3 3 \mathrm { s } .$ , so it “dies out” to zero in approximately $4 \tau _ { 1 } = 1 . 3 3 3 3 \mathrm { s }$ . The second exponential function $e ^ { - 8 t } = { \dot { e } } ^ { - t / 0 . 1 2 5 }$ has a time constant $\tau _ { 2 } = 0 . 1 2 5 \mathrm { ~ s ~ }$ , so it “dies out” to zero in approximately $4 \tau _ { 2 } = 0 . 5 ~ \mathrm { s }$ . Hence, the settling time of $y _ { H } ( t )$ ) is 1.3333 s, which is dictated by its “slowest” of the two exponential functions, in this case $e ^ { - 3 t }$ t. Obviously the free response does not exhibit oscillations because it is composed of two exponential functions. The complete system response will depend on the input $u ( t )$ , but we know that the homogeneous or free response will go to zero in 1.3333 s.

$( { \bf b } ) { \ddot { y } } - 4 { \dot { y } } + 4 0 y = 3 u$

The characteristic equation is

$$r ^ {2} - 4 r + 4 0 = 0$$
