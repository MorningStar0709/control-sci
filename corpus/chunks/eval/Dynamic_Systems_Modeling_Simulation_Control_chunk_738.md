# Laplace transform using Symbolic Math Toolbox

MATLAB’s Symbolic Math Toolbox can be used to compute the Laplace transform of a given time function f (t). The user must define the time function f (t) as the symbolic object f. The following example illustrates the built-in command laplace:

>> syms t    % define variable t (time) as a symbolic object
>> f = 6*exp(-2*t);    % define function $f(t) = 6e^{-2t}$ as a symbolic object
>> F = laplace(f);    % compute the Laplace transform $F(s)$ >> pretty(F)    % display F in a format similar to typeset mathematics

Upon hitting the return key, the result is

```lisp
6
----
s + 2
```
