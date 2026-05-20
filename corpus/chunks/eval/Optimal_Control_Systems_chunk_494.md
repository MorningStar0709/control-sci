```matlab
error('A and Q must be the same size');
return
end
if ~(mf==1&nf==1)
    if (nq ~= nf) | (mq ~= mf)
%Check that Q and F are the same size
    error('Q and F must be the same size');
    return
    end
end
if ~(mr==1&nr==1)
    if (mr ~= nr) | (mb ~= nr)
    error('R must be consistent with B');
    return
    end
end
mq = norm(Q,1);
% Check if Q is positive semi-definite and symmetric
if any(eig(Q) < -eps*mq) | (norm(Q' - Q,1)/mq > eps)
    disp('Warning: Q is not symmetric and positive ... semi-definite');
end
mr = norm(R,1);
% Check if R is positive definite and symmetric
if any(eig(R) <= -eps*mr) | (norm(R' - R,1)/mr > eps)
disp('Warning: R is not symmetric and positive ... definite');
end
%
%Define Initial Conditions for
%numerical solution of x states
%
t0=tspan(1);
tf=tspan(2);
tspan=[tf t0];
%
%Define Calculated Matrices and Vectors
%
E=B*inv(R)*B'; %E Matrix E=B*(1/R)*B' 
```

C.1 MATLAB $^{©}$ for Matrix Differential Riccati Equation

```matlab
%
%Find Hamiltonian matrix needed to use
% analytical solution to
% matrix Riccati differential equation
%
Z=[A,-E;-Q,-A'];
%
%Find Eigenvectors
%
[W,D]=eig(Z);
%
%Find the diagonals from D and pick the
% negative diagonals to create
% a new matrix M
%
j=n;
[m1,index1]=sort(real(diag(D)));
for i=1:1:n
    m2(i)=m1(j);
    index2(i)=index1(j);
    index2(i+n)=index1(i+n);
    j=j-1;
end
Md=-diag(m2);
%
%Rearrange W so that it corresponds to the sort
% of the eigenvalues
%
for i=1:2*n
    w2(:,i)=W(:,index2(i));
end
W=w2;
%
%Define the Modal Matrix for D and Split it into Parts
%
W11=zeros(n);
W12=zeros(n);
W21=zeros(n);
W22=zeros(n); 
```

```matlab
j=1;
    for i=1:2*n:(2*n*n-2*n+1)
    W11(j:j+n-1)=W(i:i+n-1);
    W21(j:j+n-1)=W(i+n:i+2*n-1);
    W12(j:j+n-1)=W(2*n*n+i:2*n*n+i+n-1);
    W22(j:j+n-1)=W(2*n*n+i+n:2*n*n+i+2*n-1);
    j=j+n;
    end
%
%Define other initial conditions for
% calculation of P, g, x and u
%
t1=0.;
tx=0.; %time array for x
tu=0.; %time array for u
x=0.; %state vector
%
%Calculation of optimized x
%
[tx,x]=ode45('lqrnssf',fliplr(tspan),x0,...
odeset('refine',2,'RelTol',1e-4,'AbsTol',1e-6));
%
%Find u vector
%
j=1;
us=0.; %Initialize computational variable
for i=1:1:mb
    for tua=t0:.1:tf
    Tt=-inv(W22-F*W12)*(W21-F*W11);
    P=(W21+W22*expm(-Md*(tf-tua))*Tt*...
    expm(-Md*(tf-tua))*inv(W11+W12*expm(-Md*(tf-tua))...
    *Tt*expm(-Md*(tf-tua)));
    K=inv(R)*B'*P;
    xs=interp1(tx,x,tua);
    us1=real(-K*xs');
    us(j)=us1(i);
    tu(j)=tua;
    j=j+1;
    end 
```
