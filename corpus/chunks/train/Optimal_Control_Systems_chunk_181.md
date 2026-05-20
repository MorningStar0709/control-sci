The following MATLAB $^{©}$ m file for Example 3.1 requires two additional MATLAB $^{©}$ files lqrnss.m which itself requires lqrnssf.m given in Appendix C.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
%% Solution using Control System Toolbox of
%% the MATLAB. Version 6
%% The following file example.m requires
%% two other files lqrnss.m and lqrnssf.m
%% which are given in Appendix
clear all
A=[0.,1.;-2.,1.];
B=[0.;1.];
Q=[2.,3.;3.,5.];
F=[1.,0.5;0.5,2.];
R=[.25];
tspan=[0 5];
x0=[2.,-3.];
[x,u,K]=lqrnss(A,B,F,Q,R,x0,tspan);
**************************

![](image/c200076210669696f63c39c098edcfb7cc99fd9a468609a85c10cb12a3a494f5.jpg)

<details>
<summary>line</summary>

| t | p₁₁(t) | p₂₂(t) | p₄₂(t) |
| --- | --- | --- | --- |
| 0.0 | 1.7 | 1.5 | 0.3 |
| 2.5 | 1.7 | 1.5 | 0.3 |
| 3.0 | 1.7 | 1.5 | 0.3 |
| 3.5 | 1.6 | 1.5 | 0.3 |
| 4.0 | 1.5 | 1.5 | 0.3 |
| 4.5 | 1.4 | 1.4 | 0.25 |
| 5.0 | 2.0 | 1.0 | 0.5 |
</details>

Figure 3.3 Riccati Coefficients for Example 3.1
