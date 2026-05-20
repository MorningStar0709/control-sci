# 6.2 SYSTEM RESPONSE USING MATLAB COMMANDS

MATLAB has a suite of built-in commands for obtaining the response of a linear dynamic system due to its initial conditions and/or the system input function. It should be emphasized that these MATLAB commands can be used only for linear systems. Furthermore, these MATLAB commands are easy to use and allow the user to quickly obtain the dynamic response of linear systems that are represented by either a transfer function or SSR. Appendix B presents a primer on using MATLAB and Table B.2 summarizes many useful MATLAB commands for simulating dynamic systems.

The four basic MATLAB simulation commands that we present are step, impulse, lsim, and initial. All four commands require that the user define the LTI system model using either the transfer function or SSR format. For example, consider the second-order I/O equation

$$\ddot {y} + 3 \dot {y} + 1 2 y = 0. 8 u \tag {6.1}$$

Applying the D operator to replace the derivative terms, that is, ẏ = Dy and ÿ = D2y, Eq. (6.1) becomes

$$(D ^ {2} + 3 D + 1 2) y = 0. 8 u \tag {6.2}$$

Next, form the ratio of output to input and replace D with the Laplace variable s to derive the transfer function G(s)

$$G (s) = \frac {0 . 8}{s ^ {2} + 3 s + 1 2} = \frac {Y (s)}{U (s)} \tag {6.3}$$

The following MATLAB commands create the object sys that represents the transfer function in Eq. (6.3)

>> numG = 0.8; % numerator of $G(s) = 0.8/(s^{2} + 3s + 12)$ >> denG = [1 3 12]; % denominator of $G(s) = 0.8/(s^{2} + 3s + 12)$ >> sys = tf(numG, denG) % create LTI transfer function $G(s)$

Note that denG is a row vector of the denominator polynomial coefficients in descending powers of s. After hitting the return key, MATLAB displays sys as

```txt
Transfer function:
0.8
s^2 + 3 s + 12 
```

so that the user can verify that he or she has properly defined the desired transfer function. Next, the user can obtain a plot of the unit-step response using the built-in MATLAB command step as follows

```txt
>> step(sys) 
```

The step command simulates the response to the input u(t) = U(t) and automatically plots the output y(t) to the screen. In this case, the LTI system sys is transfer function G(s).

In a similar fashion the built-in MATLAB command impulse simulates the response to the unitimpulse input u(t) = ??(t):

```lisp
>> impulse(sys) 
```
