# C.1 MATLAB $^{©}$ for Matrix Differential Riccati Equation

The following is the typical MATLAB© file containing the various given matrices for a problem, such as, Example 3.1 using analytical solution of matrix Riccati differential equation given in Chapter 3. This file, say example.m requires the other two files lqrnss.m and lqrnssf.m given below. The electronic version of ll these files can also be obtained by sending an email to naiduds@isu.edu.

```matlab
%%%%
clear all
A=[0.,1.;-2.,1.];
B=[0.;1.];
Q=[2.,3.;3.,5.];
F=[1.,0.5;0.5,2.];
R=[.25];
tspan=[0 5];
x0=[2.,-3.];
[x,u,K]=lqrnss(A,B,F,Q,R,x0,tspan);
%%%% 
```
