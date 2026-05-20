MATLAB Program 5–1 produces four such step-response curves.The curves are shown in Figure 5–18. (Note that the time vector t is automatically determined, since the command does not include t.)

<table><tr><td>MATLAB Program 5-1</td></tr><tr><td>A = [-1 -1;6.5 0];B = [1 1;1 0];C = [1 0;0 1];D = [0 0;0 0];step(A,B,C,D)</td></tr></table>

Step Response   
![](image/3e928b8787ab35c0ea3e09cb34847e1bf287da11f91cff8adf7774595d3f44c2.jpg)  
Figure 5–18   
Unit-step response curves.

To plot two step-response curves for the input $u _ { 1 }$ in one diagram and two step-response curves for the input $u _ { 2 }$ in another diagram, we may use the commands

step(A,B,C,D,1)

and

step(A,B,C,D,2)

respectively. MATLAB Program 5–2 is a program to plot two step-response curves for the input $u _ { 1 }$ in one diagram and two step-response curves for the input $u _ { 2 }$ in another diagram. Figure 5–19 shows the two diagrams, each consisting of two step-response curves. (This MATLAB program uses text commands. For such commands, refer to the paragraph following this example.)

MATLAB Program 5–2   
% ***** In this program we plot step-response curves of a system
% having two inputs (u1 and u2) and two outputs (y1 and y2) *****
% ***** We shall first plot step-response curves when the input is
% u1. Then we shall plot step-response curves when the input is
% u2 *****
% ***** Enter matrices A, B, C, and D *****
A = [-1 -1;6.5 0];
B = [1 1;1 0];
C = [1 0;0 1];
D = [0 0;0 0];
% ***** To plot step-response curves when the input is u1, enter
% the command 'step(A,B,C,D,1)' *****
step(A,B,C,D,1)
grid
title ('Step-Response Plots: Input = u1 (u2 = 0)')
text(3.4, -0.06,'Y1')
text(3.4, 1.4,'Y2')
% ***** Next, we shall plot step-response curves when the input
% is u2. Enter the command 'step(A,B,C,D,2)' *****
step(A,B,C,D,2)
grid
title ('Step-Response Plots: Input = u2 (u1 = 0)')
text(3,0.14,'Y1')
text(2.8,1.1,'Y2')

Figure 5–19 Unit-step response curves. $\mathbf { \Psi } ( \mathbf { a } ) u _ { 1 }$ is the input $\left( u _ { 2 } = 0 \right) ; \left( \mathrm { b } \right) u _ { 2 }$ is the input $\left( u _ { 1 } = 0 \right)$ .   
![](image/7a4b28a3f4cf33a09356aa6ae9ad6de480f3cb7097e3098364c13c8b6318a497.jpg)

<details>
<summary>line</summary>

| Time (sec) | Y1 | Y2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.2 | 1.8 |
| 2 | -0.4 | 0.8 |
| 3 | -0.1 | 1.3 |
| 4 | -0.2 | 1.1 |
| 5 | -0.1 | 1.0 |
| 6 | -0.1 | 1.2 |
| 7 | -0.1 | 1.1 |
| 8 | -0.1 | 1.1 |
| 9 | -0.1 | 1.1 |
| 10 | -0.1 | 1.1 |
</details>
