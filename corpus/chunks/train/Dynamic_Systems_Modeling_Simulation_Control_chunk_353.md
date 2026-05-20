Next, we derive the system transfer function from the I/O equation (7.16) by using the D operator to replace the derivative terms, that is, $\ddot { y } = D ^ { 2 } y$ and $\dot { y } = D y$ , which yields

$$(0. 0 4 D ^ {2} + 1 6 D + 7 0 0 0) y = f (t) \tag {7.18}$$

Next, form the ratio of output to input, $y ( t ) / f ( t )$ , and replace D with the Laplace variable s to derive the transfer function G(s)

$$G (s) = \frac {1}{0 . 0 4 s ^ {2} + 1 6 s + 7 0 0 0} \tag {7.19}$$

Equation (7.19) is the transfer function that represents the spool-valve system. For this case, the numerator of $G ( s )$ is 1, and the denominator of $G ( s )$ is the polynomial $0 . 0 \hat { 4 } s ^ { 2 } + 1 6 s + 7 0 0 0$ . The poles of the transfer function G(s) are determined by setting the denominator polynomial to zero

$$0. 0 4 s ^ {2} + 1 6 s + 7 0 0 0 = 0 \tag {7.20}$$

Equation (7.20) is identical to the characteristic equation (7.17), and hence the poles of the transfer function are

$$s _ {1} = - 2 0 0 + j 3 6 7. 4 2 \qquad s _ {2} = - 2 0 0 - j 3 6 7. 4 2$$

which are the same as the characteristic roots.

We can use MATLAB’s pole command to determine the poles of the transfer function G(s). First, we must construct the system transfer function using the tf command as follows:

$$
\begin{array}{l} > > \text { numG } = 1; \quad \% \text { numerator of } G (s) - \text { see   Eq. } \tag {7.19} \\ > > \text { denG } = [ 0. 0 4 1 6 7 0 0 0 ]; \quad \% \text { denominator   of } G (s) - \text { see   Eq. } (7. 1 9) \\ > > \text {sysG} = \text {tf (numG, denG)} \quad \% \text {define sysG as transfer function G(s)} \\ \end{array}
$$

Note that the row vector denG = [0.04 16 7000] contains the coefficients of the denominator of transfer function G(s) in descending powers of s. The MATLAB pole command below computes the poles of the transfer function defined as sysG.

$$> > \mathrm{p} = \text {pole(sysG)} \quad \% \text {compute poles of} G (s)$$

Executing these MATLAB line commands yields the vector of poles p with components $p _ { 1 } = - 2 0 0 + j 3 6 7 . 4 2$ and $p _ { 2 } = - 2 0 0 - j 3 6 7 . 4 2$ , which is the same result previously obtained in this example.
