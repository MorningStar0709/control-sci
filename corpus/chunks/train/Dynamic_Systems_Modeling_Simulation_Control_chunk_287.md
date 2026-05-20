As before, a plot of the response is automatically created. The user has the option to define a desired simulation time vector t and invoke left-hand-side arguments in order to create their own plot as shown below

>> t = 0:0.01:5; % define time vector from 0 to 5 in steps $\Delta t = 0.01$ s  
>> [y,t] = step(sys,t); % compute the unit-step response $y(t)$ (no plot)  
>> plot(t,y) % plot the unit-step response $y(t)$

We can also use the step and impulse commands with the LTI system sys defined as a state-space representation. Using the LTI system presented by Eq. (6.1), we can define the following SSR for states x1 = y and x = ẏ

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 2 & - 3 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0. 8 \end{array} \right] u \tag {6.4}

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \mathbf {x} + [ 0 ] u
$$

Next, define the SSR matrices noting that MATLAB uses square brackets to denote matrices and vectors, where each row is separated by a semicolon (see Appendix B for a brief MATLAB tutorial):

>> A = [0 1 ; -12 -3 ]; % define state matrix A
>> B = [0 ; 0.8 ]; % define input matrix B
>> C = [1 0 ]; % define output matrix C
>> D = 0; % define direct-link “matrix” D

We can create the SSR object sys using the ss command

$$> > \text { sys } = \text { ss } (A, B, C, D)$$

Finally, we can simulate and plot the unit-step or unit-impulse responses using the step or impulse commands with SSR object sys representing the system dynamics. Because transfer function Eq. (6.3) and SSR Eq. (6.4) both represent the system dynamics, that is, Eq. (6.1), we get identical simulation results whether we choose to define sys using tf(numG,denG) or ss(A,B,C,D).

The MATLAB command lsim (“linear simulation”) allows the user to simulate the response of a linear system to an arbitrary user-defined input function. For example, suppose the desired input is a pulse with a magnitude of 20 that lasts for 5 s. To simulate the pulse response, we type the commands

>> t = 0:0.01:10; % define time vector from 0 to 10 in steps $\Delta t = 0.01$ s  
>> u(1:501) = 20; % define pulse $u(t) = 20$ for $0 \leq t \leq 5$ s  
>> u(502:1001) = 0; % define zero input $u(t) = 0$ for $t > 5$ s  
>> [y,t] = lsim(sys,u,t); % obtain system output $y(t)$ for user-defined input $u(t)$
