# C.4 MATLAB $^{©}$ for Discrete-Time Tracking System

This MATLAB $^{©}$ file for tracking Example 5.6 is given below.

```matlab
% Solution Using Control System Toolbox (STB) in
% MATLAB Version 6
clear
A=[0.8 1;0,0.6]; % system matrix A
B=[1;0.5]; % system matrix B
C=[1 0;0 1]; % system matrix C
Q=[1 0;0 0]; % performance index
%% state weighting matrix Q
R=[0.01]; % performance index control
%% weighting matrix R
F=[1,0;0,0]; % performance index weighting matrix F
%
x1(1)=5; % initial condition on state x1 
```

```matlab
x2(1)=3; % initial condition on state x2
xk=[x1(1);x2(1)];
zk=[2;0];
zkf=[2;0];
% note that if kf = 10 then
% k = [k0,kf] = [0 1 2,...,10],
% then we have 11 points and an array x1 should
% have subscript
% x1(N) with N=1 to 11. This is because x(o) is
% illegal in array
% definition in MATLAB. Let us use N = kf+1
k0=0; % the initial instant k_0
kf=10; % the final instant k_f
N=kf+1; %
[n,n]=size(A); % fixing the order of the system matrix A
I=eye(n); % identity matrix I
E=B*inv(R)*B'; % the matrix E = BR^{-1}B'
V=C'*Q*C;
W=C'*Q;
%
% solve matrix difference Riccati equation
% backwards starting from kf to k0
% use the form P(k) = A'P(k+1)[I + EP(k+1)]^{-1}A + V
% first fix the final conditionS P(k_f) = F;
% g(k_f) = C'Fz(k_f)
% note that P, Q, R, F are all symmetric ij = ji
Pkplus1=C'*F*C;
gkplus1=C'*F*zkf;
p11(N)=F(1);
p12(N)=F(2);
p21(N)=F(3);
p22(N)=F(4);
%
g1(N)=gkplus1(1);
g2(N)=gkplus1(2);
%
Pk=0;
gk=0;
for k=N-1:-1:1, 
```

C.4 MATLAB© for Discrete-Time Tracking System

```matlab
Pk = A'*Pkplus1*inv(I+E*Pkplus1)*A+V;
Lk = inv(R+B'*Pkplus1*B)*B'*Pkplus1*A;
gk=(A-B*Lk)'*gkplus1+W*zk;
p11(k) = Pk(1,1);
p12(k) = Pk(1,2);
p21(k) = Pk(2,1);
p22(k) = Pk(2,2);
pkplu1 = Pk;
%
    g1(k) = gk(1);
    g2(k) = gk(2);
    gkplus1 = gk;
end
%
% calculate the feedback coefficients L and Lg(k)
% L(k) = (R+B'P(k+1)B)^{-1}BP(k+1)A
% Lg(k) = [R + B'P(k+1)B]^{-1}B'
%
for k = N:-1:1,
    Pk=[p11(k),p12(k);p21(k),p22(k)];
    gk=[g1(k);g2(k)];
    Lk = inv(R+B'*Pkplus1*B)*B'*Pkplus1*A;
    Lgk= inv(R+B'*Pkplus1*B)*B';
    l1(k) = Lk(1);
    l2(k) = Lk(2);
    lg1(k) = Lgk(1);
    lg2(k) = Lgk(2);
end
%
% solve the optimal states
% x(k+1) = [A-B*L)x(k) + BLg(k+1)g(k+1) given x(0)
%
xk=0.0;
for k=1:N-1,
    Lk = [l1(k),l2(k)];
    Lgk = [lg1(k),lg2(k)];
    Lgkplus1=[lg1(k+1),lg2(k+1)];
    xk = [x1(k);x2(k)];
    xkplus1 = (A-B*Lk)*xk + B*Lgkplus1*gk; 
```

```matlab
x1(k+1) = xkplus1(1);
x2(k+1) = xkplus1(2);

end

% solve for optimal control
% u(k) = -L(k)x(k) + Lg(k)g(k+1)
%
xk=0.0;
% for k=1:N,
    for k=1:N-1,
    Lk = [l1(k),l2(k)];
    Lgk = [lg1(k),lg2(k)];
    gkplus1=[g1(k+1);g2(k+1)];
    xk = [x1(k);x2(k)];
    u(k) = -Lk*xk + Lgk*gkplus1;
end

%
% plot various values: P(k), g(k), x(k), u(k)
% let us first reorder the values of k = 0 to kf
%
% first plot P(k)
%
k = 0:1:kf;
figure(1)
plot(k,p11,'k:o',k,p12,'k:+',k,p22,'k:*')
grid
xlabel('k')
ylabel('Riccati coefficients')
gtext('p_{11}(k)')
gtext('p_{12}(k)')
gtext('p_{22}(k)')
%
% Plot g(k)
%
k = 0:1:kf;
figure(2)
plot(k,g1,'k:o',k,g2,'k:+')
grid
xlabel('k') 
```
