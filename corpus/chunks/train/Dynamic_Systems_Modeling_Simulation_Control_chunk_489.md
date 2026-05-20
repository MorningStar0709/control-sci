For LTI systems with multiple DOF (such as multiple-mass mechanical systems) it is probably easier to use bode with the system defined as a state-space representation (SSR). The MATLAB commands for a Bode diagram using an SSR are

```matlab
>> A = [ ... ]    % create state matrix A
>> B = [ ... ]    % create input matrix B
>> C = [ ... ]    % create output matrix C
>> D = [ ... ]    % create direct-link matrix D
>> sys = ss(A, B, C, D)    % build system using SSR
>> bode(sys)    % plot Bode diagram(s) for SSR 
```

Of course, the user must fill in the appropriate matrices for the desired SSR. The number of Bode diagrams plotted by MATLAB corresponds to the number of inputs and outputs. The user can also compute the magnitude and phase for a desired frequency ?? by using the command

>> w = 7; % set desired input frequency $\omega = 7$ rad/s  
>> [mag, phase] = bode(sys, w) % compute magnitude and phase (degrees)

where sys corresponds to the desired SSR determined by matrices A, B, C, and D. For example, if an SSR has one input u(t) and two outputs $y _ { 1 } ( t )$ and $y _ { 2 } ( t )$ , then the above command will return two magnitudes and phase angles because the desired SSR is essentially defining two transfer functions: $G _ { 1 } ( s ) = Y _ { 1 } ( s ) / U ( s )$ ) and $G _ { 2 } ( s ) = Y _ { 2 } ( s ) / U ( s )$ .
