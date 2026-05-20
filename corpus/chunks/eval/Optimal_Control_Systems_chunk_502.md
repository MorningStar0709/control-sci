# C.3.1 MATLAB File lqrdnss.m

This MATLAB© file lqrdnss.m is required along with the other file example.m to solve the matrix Riccati difference equation using its analytical solution.

```matlab
%/%/%/%/%/%/%%
function [x,u]=lqrdnss(As,Bs,Fs,Qs,Rs,x0,kspan)
%
%This m-file calculates and plots the outputs for a
% discrete Linear Quadratic Regulator system
%Based on provided linear state space matrices
% for A and B and Performance Index matrices
% for F, Q and R.
%This function takes these inputs, and using the
% analytical solution to the matrix Riccati equation,
% formulates the optimal states and inputs.
%
%
% SYNTAX: [x,u]=lqrdnss(A,B,F,Q,R,x0,tspan)
%
%
% INPUTS (All numeric):
% A,B Matrices from xdot=Ax+Bu
% F,Q,R Performance Index Parameters; terminal cost,
% error and control weighting
% x0 State variable initial condition. Must be a
% column vector [x10;x20;x30...]
% kspan Vector containing sample span [k0 kf]
%
%
% OUTPUTS:
% x is the state variable vector
% u is the input vector
%
% The system plots the Riccati coefficients in
% combinations of 4,
% and the x vector, and u vector in
% combinations of 3.
% 
```

%Check for correct number of inputs

if nargin<7
    error('Incorrect number of inputs specified')
    return
