The specification requires that the response to the unit-step disturbance be such that the settling time be 2 to 3 sec and the system have a reasonable damping. We may interpret the specification as andz = 0.5 $\omega _ { n } = 4$ radsec for the dominant closed-loop poles.We may choose the third pole at s=–10 so that the effect of this real pole on the response is small. Then the desired characteristic equation can be written as

$$(s + 1 0) \left(s ^ {2} + 2 \times 0. 5 \times 4 s + 4 ^ {2}\right) = (s + 1 0) \left(s ^ {2} + 4 s + 1 6\right) = s ^ {3} + 1 4 s ^ {2} + 5 6 s + 1 6 0$$

The characteristic equation for the system given by Equation (8–14) is

$$s ^ {3} + (3. 6 + K a b) s ^ {2} + (9 + K a + K b) s + K = 0$$

Hence, we require

$$3. 6 + K a b = 1 49 + K a + K b = 5 6K = 1 6 0$$

which yields

$$a b = 0. 0 6 5, \quad a + b = 0. 2 9 3 7 5$$

The PID controller now becomes

$$
\begin{array}{l} G _ {c} (s) = \frac {K [ a b s ^ {2} + (a + b) s + 1 ]}{s} \\ = \frac {1 6 0 (0 . 0 6 5 s ^ {2} + 0 . 2 9 3 7 5 s + 1)}{s} \\ = \frac {1 0 . 4 (s ^ {2} + 4 . 5 1 9 2 s + 1 5 . 3 8 5)}{s} \\ \end{array}
$$

With this PID controller, the response to the disturbance is given by

$$
\begin{array}{l} C _ {d} (s) = \frac {s}{s ^ {3} + 1 4 s ^ {2} + 5 6 s + 1 6 0} D (s) \\ = \frac {s}{(s + 1 0) (s ^ {2} + 4 s + 1 6)} D (s) \\ \end{array}
$$

Clearly, for a unit-step disturbance input, the steady-state output is zero, since

$$\lim _ {t \rightarrow \infty} c _ {d} (t) = \lim _ {s \rightarrow 0} s C _ {d} (s) = \lim _ {s \rightarrow 0} \frac {s ^ {2}}{(s + 1 0) (s ^ {2} + 4 s + 1 6)} \frac {1}{s} = 0$$

The response to a unit-step disturbance input can be obtained easily with MATLAB. MATLAB Program 8–9 produces a response curve as shown in Figure 8–48(a). From the response curve, we see that the settling time is approximately 2.7 sec.The response damps out quickly.Therefore, the system designed here is acceptable.

MATLAB Program 8–9   
% ***** Response to unit-step disturbance input ****
numd = [1 0];
dend = [1 14 56 160];
t = 0:0.01:5;
[c1,x1,t] = step(numd,dend,t);
plot(t,c1)
grid
title('Response to Unit-Step Disturbance Input')
xlabel('t Sec')
ylabel('Output to Disturbance Input')
% ***** Response to unit-step reference input ****
numr = [10.4 47 160];
denr = [1 14 56 160];
[c2,x2,t] = step(numr,denr,t);
plot(t,c2)
grid
title('Response to Unit-Step Reference Input')
xlabel('t Sec')
ylabel('Output to Reference Input')

For the reference input r(t), the closed-loop transfer function is
