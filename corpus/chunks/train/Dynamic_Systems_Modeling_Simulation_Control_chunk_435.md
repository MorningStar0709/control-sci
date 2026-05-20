# 8.3 INVERSE LAPLACE TRANSFORMATION

We should restate that our overall goal is to use Laplace transforms to obtain the response of a dynamic system that is subjected to initial conditions and/or a known input function. Consequently, we begin our analysis with the system’s mathematical model, which is an ordinary differential equation. The Laplace transform methods discussed thus far provide a systematic approach for solving the ODE and obtaining the dynamic response. This systematic approach can be summarized as

1. Take the Laplace transform of every term in the input-output (I/O) mathematical model (the ODE) and incorporate the initial conditions using the differentiation properties, Eqs. (8.5), (8.6), and (8.7).   
2. Using the result from step 1, solve for the Laplace transform of the dynamic variable, Y(s).   
3. Obtain the system’s dynamic response by taking the inverse Laplace transform, $y ( t ) = { \mathcal { L } } ^ { - 1 } \{ Y ( s ) \}$

This systematic approach is best illustrated by the following example.
