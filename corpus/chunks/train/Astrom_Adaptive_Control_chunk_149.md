where R, S, and T are polynomials. This control law represents a negative feedback with the transfer operator S/R and a feedforward with the transfer operator T/R. It thus has two degrees of freedom. A block diagram of the closed-loop system is shown in Fig. 3.2. Elimination of u between Eqs. (3.1)

and (3.2) gives the following equations for the closed-loop system:

$$y (t) = - \frac {B T}{A R + B S} u _ {c} (t) + \frac {B R}{A R + B S} v (t) \tag {3.3}u (t) = \frac {A T}{A R + B S} u _ {c} (t) - \frac {B S}{A R + B S} v (t)$$

The closed-loop characteristic polynomial is thus

$$A R + B S = A _ {c} \tag {3.4}$$

The key idea of the design method is to specify the desired closed-loop characteristic polynomial $A_{c}$ . The polynomials R and S can then be solved from Eq. (3.4). Notice that in the design procedure we consider polynomial $A_{c}$ to be a design parameter that is chosen to give desired properties to the closed-loop system. Equation (3.4), which plays a fundamental role in algebra, is called the Diophantine equation. It is also called the Bezout identity or the Aryabhatta equation. The equation always has solutions if the polynomials A and B do not have common factors. The solution may be poorly conditioned if the polynomials have factors that are close. The solution can be obtained by introducing polynomials with unknown coefficients and solving the linear equations obtained. The solution of the equation is discussed in detail in Chapter 11.
