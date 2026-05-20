# C.3 MATLAB $^{©}$ for Matrix Difference Riccati Equation

The following is the typical MATLAB $^{©}$ file containing the various given matrices for a problem, such as Example 5.5, using analytical solution of matrix Riccati difference equation given in Chapter 5. This file, say example.m requires the other file lqrdnss.m given below.

```matlab
%%%%
clear all
A=[.8,1;0,.5];
B=[1;.5];
F=[2,0;0,4];
Q=[1,0;0,1];
R=1;
kspan=[0 10];
x0(:,1)=[5.;3.];
[x,u]=lqrdnss(A,B,F,Q,R,x0,kspan);
%%% 
```
