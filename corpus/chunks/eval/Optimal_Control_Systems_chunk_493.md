# C.1.1 MATLAB File lqrnss.m

This MATLAB $^{©}$ file lqrnss.m is required along with the other files example.m and lqrnssf.m to solve the matrix Riccati equation using its analytical solution.

```matlab
% The following is lqrnss.m
function [x,u,K]=lqrnss(As,Bs,Fs,Qs,Rs,x0,tspan)
%Revision Date 11/14/01
%
% This m-file calculates and plots the outputs for a
% Linear Quadratic Regulator (LQR) system based on given
% state space matrices A and B and performance index
% matrices F, Q and R. This function takes these inputs,
% and using the analytical solution to the
%% matrix Riccati equation,
% and then computing optimal states and controls.
%
%
% SYNTAX: [x,u,K]=lqrnss(A,B,F,Q,R,x0,tspan)
%
% INPUTS (All numeric):
% A,B Matrices from xdot=Ax+Bu
% F,Q,R Performance Index Parameters;
% x0 State variable initial condition
% tspan Vector containing time span [t0 tf]
%
% OUTPUTS:
% x is the state variable vector
% u is the input vector
% K is the steady-state matrix inv(R)*B'*P
%
% The system plots Riccati coefficients, x vector,
% and u vector
%
%Define variables to use in external functions
%
global A E F Md tf W11 W12 W21 W22 n.
%
%Check for correct number of inputs 
```

C.1 MATLAB© for Matrix Differential Riccati Equation

```matlab
%
if nargin<7
    error('Incorrect number of inputs specified')
    return
end
%
%Convert Variables to normal symbology to prevent
% problems with global statement
%
A=As;
B=Bs;
F=Fs;
Q=Qs;
R=Rs;
plotflag=0; %set plotflag to 1 to avoid plotting of
% data on figures
%
%Define secondary variables for global passing to
% ode-related functions and determine matrice size
%
[n,m]=size(A); %Find dimensions of A
[nb,mb]=size(B); %Find dimensions of B
[nq,mq]=size(Q); %Find dimensions of Q
[nr,mr]=size(R); %Find Dimensions of R
[nf,mf]=size(F); %Find Dimensions of F
if n~=m %Verify A is square
    error('A must be square')
else
    [n,n]=size(A);
end
%
%Data Checks for proper setup
if length(A)>rank(ctrb(A,B))
%Check for controllability
    error('System Not Controllable')
    return
end
if (n ~= nq) | (n ~= mq)
%Check that A and Q are the same size 
```
