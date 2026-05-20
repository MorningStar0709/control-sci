# Defining transfer function object sysG

>> numG = 3; % numerator of $G(s) = 3/(s^2 + 2s + 16)$ >> denG = [1 2 16]; % denominator of $G(s) = 3/(s^2 + 2s + 16)$ >> sysG = tf (numG, denG) % define LTI transfer function $G(s)$

Note that denG is a row vector defining the denominator polynomial coefficients in descending powers of s. Upon hitting the return key MATLAB displays sysG as

Transfer function:   
```csv
3
s^2 + 2 s + 16 
```

Therefore, the user can verify that he or she has properly defined the desired transfer function.

Roots of polynomial denG   
>> roots (denG) % roots of $s^{2} + 2s + 16 = 0$

Poles of transfer function sysG   
>> pole(sysG) % poles of $G(s)$ ; i.e., roots of $s^{2} + 2s + 16 = 0$

Undamped natural frequency and damping ratio   
>> [Wn, zeta] = damp(sysG) % $\omega_{n}$ and $\zeta$ for LTI system $G(s)$

Plot of unit-step response of sysG   
```erlang
>> [y,t] = step(sysG); % unit-step response of G(s)
>> plot(t,y) % plot the unit-step response y(t) 
```

Plot of sysG response to an arbitrary input   
>> t = 0:0.01:12; % define time vector from 0 to 12 in steps $\Delta t = 0.01s$ >> u = zeros (size(t)); % define input vector u as all zeros (same size as t)  
>> u(1:601) = 2; % define $u = 2$ for time $0 \leq t \leq 6$ s; $u(t)$ is a pulse  
>> [y,t] = lsim(sysG,u,t); % response of $G(s)$ to pulse input $u(t)$ >> plot(t,y) % plot the response $y(t)$

These commands, along with related commands for linear system analysis, are collected and summarized in Table B.2. Note that the built-in commands for system response in the time domain (step, impulse, lsim, and initial) and frequency-response analysis (bode and bandwidth) require an LTI system object sys that is created either as a transfer function (using tf) or state-space representation (using ss).
