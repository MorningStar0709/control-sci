# 5.6 TRANSFER FUNCTIONS

Transfer functions are a convenient way to represent and analyze the I/O (or cause-and-effect) relationship of an LTI dynamic system. They are frequently used in simulation diagrams (“block diagrams,” to be discussed in the next section) to characterize a desired input/output equation. Numerical algorithms such as MATLAB and Simulink use transfer functions to represent dynamic systems that have a single input and a single output.

Traditionally, transfer functions are introduced using Laplace transform methods. The Laplace transform maps the function f (t) from the time domain to the domain of the complex variable s, and is defined by

$$\mathscr {L} \{f (t) \} = F (s) = \int_ {0} ^ {\infty} f (t) e ^ {- s t} d t \tag {5.95}$$

The reader may recall that Laplace transforms can be used to solve linear differential equations with constant coefficients, where the Laplace transformation converts a differential equation into an algebraic equation in variable s. If a forcing function f (t) exists in the differential equation, it can be converted into the s-domain function $F ( s )$ using Eq. (5.95). Hence, a table comprising the Laplace transforms of “standard” time functions (such as sinusoidal functions) can be constructed. The solution to the differential equation in the time domain is obtained by applying the inverse Laplace transform to the algebraic equation in the s-domain. Chapter 8 presents a brief overview of Laplace transform theory, including transforms of common time functions, Laplace transform properties, and the solution of differential equations using Laplace transform methods.
