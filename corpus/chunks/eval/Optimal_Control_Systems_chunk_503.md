# C.3 MATLAB© for Matrix Difference Riccati Equation

end

%Convert Variables to normal symbology to % prevent problems with global statement

```matlab
A=As;
B=Bs;
F=Fs;
Q=Qs;
R=Rs;
plotflag=0; %set plotflag to a 1 to avoid plotting
% of data on figures 
```

%Define secondary variables for global passing to % ode-related functions and determine matrice size

```matlab
[n,m]=size(A); %Find dimensions of A
[nb,mb]=size(B); %Find dimensions of B
[nq,mq]=size(Q); %Find dimensions of Q
[nr,mr]=size(R); %Find Dimensions of R
[nf,mf]=size(F); %Find Dimensions of F
if n~=m %Verify A is square error('A must be square')
else
    [n,n]=size(A);
end 
```

```matlab
%Data Checks for proper setup
%Check for controllability
if length(A) > rank(ctrb(A, B))
    error('System Not Controllable')
    return
end
if (n ~= nq) | (n ~= mq)
%Check that A and Q are the same size
    error('A and Q must be the same size');
    return
end
if ~(mf == 1 & nf == 1) 
```

```matlab
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
disp('Warning: Q is not symmetric and ...
positive semi-definite');
end
mr = norm(R,1);
% Check if R is positive definite and symmetric
if any(eig(R) <= -eps*mr) | (norm(R' - R,1)/mr > eps)
disp('Warning: R is not symmetric and ...
positive definite');
end 
```  
%Define Calculated Matrix

```matlab
E=B*inv(R)*B';
%Find matrix needed to calculate Analytical Solution
% to Riccati Equation
H=[inv(A),inv(A)*E;Q*inv(A),A'+Q*inv(A)*E];
%Find Eigenvectors
[W,D]=eig(H);
%Find the diagonals from D and pick the negative 
```
