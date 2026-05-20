# Inverse Laplace Transform Using MATLAB

Recall that in Section 8.2 we showed how MATLAB’s Symbolic Math Toolbox can be used to compute the Laplace transform of a given time function. The Symbolic Math Toolbox can also compute the inverse Laplace transform $y ( t ) = \mathcal { L } ^ { - 1 } \{ Y ( s ) \}$ using the single-line command $\gamma \ = \ \mathrm { i } \mathrm { 1 } \mathsf { a p l a c e } \left( \mathrm { Y } \right)$ . Here, the user must define the Laplace transform Y(s) as a symbolic object. For example, the following MATLAB commands will determine the inverse Laplace transform of Y(s) presented in Example 8.8:

```matlab
>> syms s    % define Laplace variable s
>> Y = (2*s + 9)/(s^2 + 6*s + 25)    % define Laplace transform Y(s)
>> y = ilaplace(Y)    % find inverse Laplace transform
>> pretty(y)    % display y in math typeset 
```

The third and fourth commands will display y(t) as a symbolic function of time t. Typing all four line commands shown above yields

$$2 \exp (- 3 t) \cos (4 t) + 3 / 4 \exp (- 3 t) \sin (4 t)$$

which is the solution to Example 8.8.
