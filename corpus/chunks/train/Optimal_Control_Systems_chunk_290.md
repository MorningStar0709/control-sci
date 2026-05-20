# Example 5.4

Consider the minimization of the performance index (5.3.30) without the terminal cost function and the plant (5.3.31) with $k_{f} = \infty$ . Let us find the closed-loop optimal control for this system.

Solution: We have already identified the various matrices of the state (5.2.1) and the performance index (5.2.3) as given by (5.3.33), except that we now have $\mathbf{F}(k_{f}) = \mathbf{0}$ .

Then, the solution of the algebraic Riccati equation (5.4.7), the closed-loop, optimal control (5.4.8) and the optimal states (5.4.10) are best solved using MATLAB $^{©}$ as shown below.

```matlab
**************************
% Solution Using Control System Toolbox (STB) in
% the MATLAB, Version 6
%
A=[0.8 1;0,0.6]; %% system matrix A
B=[1;0.5]; %% system matrix B
Q=[1 0;0 1]; %% performance index state weighting matrix Q0.5
R=[1]; %% performance index control weighting matrix R
%
x1(1)=5; %% initial condition on state x1 
```

```matlab
x2(1)=3; % initial condition on state x2
xk=[x1(1);x2(1)];
% note that if kf = 10 then k = [k0,kf] = [0 1 2,...,10],
% then we have 11 points and an array x1 should have subscript
% x1(N) with N=1 to 11. This is because x(o) is illegal in array
% definition in MATLAB. Let us use N = kf+1
k0=0; % the initial instant k_0
kf=10; % the final instant k_f
N=kf+1; %
[n,n]=size(A); % fixing the order of the system matrix A
I=eye(n); % identity matrix I
E=B*inv(R)*B'; % the matrix E = BR^{-1}B'
%
% solve matrix algebraic Riccati equation
% use the form P = A'PA - A'PB[B'PB+R]^{-1}B'PA + Q
% note that P, Q, R are all symmetric ij = ji
% calculate the feedback coefficient L
% L = [B'PB+R]^{-1}B'PA
%
[P,EIGVAL,L,RR] = dare(A,B,Q,R)
%
P =
    1.3944    0.3738
    0.3738    1.7803

EIGVAL =
    0.3211 + 0.2151i
    0.3211 - 0.2151i

L =
    0.3937    0.7281
%
% solve the optimal states
% x(k+1) = (A-B*L)x(k) given x(0)
%
for k=1:N-1,
    xk = [x1(k);x2(k)];
    xkplus1 = (A-B*L)*xk;
    x1(k+1) = xkplus1(1);
    x2(k+1) = xkplus1(2);
end
%
% solve for optimal control u(k) = -Lx(k) 
```
