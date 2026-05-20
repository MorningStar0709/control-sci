MATLAB Program 6–12 produces the plot of the unit-ramp response curves. Figure 6–51 shows the result. Clearly, the compensated system shows much smaller steady-state error (one-tenth of the original steady-state error) in following the unit-ramp input.

MATLAB Program 6–12   
% **** Unit-ramp responses of compensated system and
% uncompensated system ****

% **** Unit-ramp response will be obtained as the unit-step
% response of C(s)/[sR(s)] ****

% **** Enter the numerators and denominators of C1(s)/[sR(s)]
% and C2(s)/[sR(s)], where C1(s) and C2(s) are Laplace
% transforms of the outputs of the compensated and un-
% compensated systems, respectively. ****

numc = [1.0235 0.0512];
denc = [1 3.005 2.015 1.0335 0.0512 0];
num = [1.06];
den = [1 3 2 1.06 0];

% **** Specify the time range (such as t=0:0.1:50) and enter
% step command and plot command. ****

t = 0:0.1:50;
c1 = step(numc,denc,t);
c2 = step(num,den,t);
plot(t,c1,'-',t,c2,'.',t,t,'--')
grid

text(2.2,27,'Compensated system');
text(26,21.3,'Uncompensated system');
title('Unit-Ramp Responses of Compensated and Uncompensated Systems')
xlabel('t Sec');
ylabel('Outputs c1 and c2')

Figure 6–51 Unit-ramp responses of compensated and uncompensated systems. [The compensator is given by Equation (6–20).]   
![](image/a14cf865d2daa06acad20fd4f1beaf8aad7a18fef576a543224742135d3ca8bc.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | ~5 | ~4 |
| 10 | ~10 | ~8 |
| 15 | ~15 | ~13 |
| 20 | ~20 | ~18 |
| 25 | ~25 | ~23 |
| 30 | ~30 | ~28 |
| 35 | ~35 | ~33 |
| 40 | ~40 | ~38 |
| 45 | ~45 | ~43 |
| 50 | ~50 | ~48 |
</details>

MATLAB Program 6–13 gives the unit-step response curves of the compensated and uncompensated systems. The unit-step response curves are shown in Figure 6–52. Notice that the lag-compensated system exhibits a larger maximum overshoot and slower response than the original uncompensated system. Notice that a pair of the pole at s=–0.0549 and zero at s=–0.05 generates a long tail of small amplitude in the transient response. If a larger maximum overshoot and a slower response are not desired, we need to use a lag–lead compensator as presented in Section 6–8.

MATLAB Program 6–13   
% ***** Unit-step responses of compensated system and
% uncompensated system ****

% ***** Enter the numerators and denominators of the
% compensated and uncompensated systems ****
