# Partial-fraction expansion

The following MATLAB commands compute the residues for the partial-fraction expansion of the Laplace transform

$$F (s) = \frac {- 2 s + 8}{s ^ {2} + 4 s + 3}$$

```matlab
>> numF = [ -2 8 ];    % F(s) numerator coefficients
>> denF = [ 1 4 3 ];    % F(s) denominator coefficients
>> [r, p, k] = residue(numF, denF)    % compute residues, poles, and direct term 
```

Upon hitting the return key, the result is

```txt
r = -7 5 % vector of residues 
```

Table B.2 MATLAB Commands for Linear System Analysis

<table><tr><td>MATLAB Command</td><td>Description</td></tr><tr><td>roots (denG)</td><td>Computes roots of polynomial with coefficients defined by vector denG.
For example, denG could be the denominator of transfer function G(s)</td></tr><tr><td>sysG = tf (numG, denG)</td><td>Creates transfer function object sysG.
Inputs numG and denG are vectors of the numerator and denominator polynomial coefficients</td></tr><tr><td>dcgain (sysG)</td><td>Computes the DC gain of transfer function sysG</td></tr><tr><td>pole (sysG)</td><td>Computes the poles of transfer function sysG</td></tr><tr><td>[Wn, zeta] = damp (sysG)</td><td>Computes the undamped natural frequency (Wn, rad/s) and damping ratio zeta for LTI system sysG</td></tr><tr><td>sys = ss (A, B, C, D)</td><td>Creates the state-space representation object sys.
