Equation (10.30) shows that the steady-state tracking error depends on (1) the nature of the input, R(s), and (2) the forward transfer function G(s).

System type is a designation of the forward transfer function G(s) that is useful for analyzing the steadystate error. It represents the number of “free integrators” that exist in the forward transfer function. To show this, let us write the forward transfer function using the following form:

$$G (s) = \frac {F (s)}{s ^ {N} Q (s)} \tag {10.31}$$

where F(s) and Q(s) are polynomials in s that do not contain a zero at s = 0. The index N is called the system type and it is the number of “free integrators” (1/s terms) that can be divided out of G(s). As a quick example, consider the forward transfer function:

$$G (s) = \frac {6 (s + 2)}{s ^ {2} + 1 4 s + 3 6} = \frac {F (s)}{s ^ {N} Q (s)}$$

Hence, N = 0 and F(s) and Q(s) are the numerator and denominator polynomials of G(s). Because N = 0, this forward transfer function G(s) is called a “type 0 system.” As a second example, consider the forward transfer function:

$$G (s) = \frac {6 (2 s + 4)}{s ^ {2} + 8 s} = \frac {1 2 s + 2 4}{s (s + 8)} = \frac {F (s)}{s ^ {N} Q (s)}$$

Clearly, N = 1 and this is a “type 1 system.” In other words, we can “divide out” a free integrator (1/s) from G(s) in this example. The reader should recall that the forward transfer function G(s) is the product of the controller and plant transfer functions, and therefore a PI or PID controller will introduce a “free integrator”

into G(s). As we shall see the system type N is a purely notational convenience that allows us to categorize the steady-state tracking error.

Now, let us compute the steady-state tracking error defined by Eq. (10.30) for different “standard” reference signals. The step input is the “least demanding” reference signal in terms of tracking requirements because it is a static input. If the reference signal is a unit-step function, $r ( t ) = 1 = U ( t )$ , then its Laplace transform is $\mathcal { L } \{ r ( t ) \} = R ( s ) = 1 / s$ and Eq. (10.30) becomes

$$\text { Unit - step input: } \quad e (\infty) = \lim _ {s \to 0} \frac {s (1 / s)}{1 + G (s)} = \frac {1}{1 + K _ {\mathrm{sp}}} \tag {10.32}$$
