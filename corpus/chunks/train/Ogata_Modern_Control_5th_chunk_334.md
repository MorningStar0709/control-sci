Notice that the system designed by Method 1 gives a larger value of the static velocity error constant. This means that the system designed by Method 1 will give smaller steady-state errors in following ramp inputs than the system designed by Method 2.

For different combinations of a zero and pole of the compensator that contributes 40.894°, the value of $K _ { v }$ will be different. Although a certain change in the value of $K _ { v }$ can be made by altering the pole-zero location of the lead compensator, if a large increase in the value of $K _ { v }$ is desired, then we must alter the lead compensator to a lag–lead compensator.

Comparison of step and ramp responses of the compensated and uncompensated systems. In what follows we shall compare the unit-step and unit-ramp responses of the three systems: the original uncompensated system, the system designed by Method 1, and the system designed by Method 2. The MATLAB program used to obtain unit-step response curves is given in

MATLAB Program 6–9, where num1 and den1 denote the numerator and denominator of the system designed by Method 1 and num2 and den2 denote that designed by Method 2. Also, num and den are used for the original uncompensated system.The resulting unit-step response curves are shown in Figure 6–45.The MATLAB program to obtain the unit-ramp response curves of the designed systems is given in MATLAB Program 6–10, where we used the step command to obtain unit-ramp responses by using the numerators and denominators for the systems designed by Method 1 and Method 2 as follows:

MATLAB Program 6–9   
% ***** Unit-Step Response of Compensated and Uncompensated Systems *****
num1 = [12.287 23.876];
den1 = [1 5.646 16.933 23.876];
num2 = [9];
den2 = [1 3 9];
num = [10];
den = [1 1 10];
t = 0:0.05:5;
c1 = step(num1, den1, t);
c2 = step(num2, den2, t);
c = step(num, den, t);
plot(t, c1, '-', t, c2, '.', t, c, 'x')
grid
title('Unit-Step Responses of Compensated Systems and Uncompensated System')
xlabel('t Sec')
ylabel('Outputs c1, c2, and c')
text(1.51, 1.48, 'Compensated System (Method 1)')
text(0.9, 0.48, 'Compensated System (Method 2)')
text(2.51, 0.67, 'Uncompensated System')

Unit-Step Responses of Compensated Systems and Uncompensated System   
![](image/9c683477899ab103eeb7524e5d14d85830cb2fc90b391cfe24fde4b6cc608b98.jpg)

<details>
<summary>line</summary>
