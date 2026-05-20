# Inverse Laplace transform using Symbolic Math Toolbox

The following example illustrates the built-in command ilaplace for computing the inverse Laplace transform f (t) = ℒ −1{F(s)}:

```matlab
>> syms s % define Laplace variable s as a symbolic object
>> F = 6/(s+2); % define Laplace transform F(s) as a symbolic object
>> f = ilaplace(F); % compute the inverse Laplace transform f(t)
>> pretty(f) % display f in a format similar to typeset mathematics 
```

Upon hitting the return key, the result is

6 $\exp(-2\ t)$

which is the inverse result of the previous Laplace transform example. The three commands for Laplace transform analysis are collected and summarized in Table B.3.
