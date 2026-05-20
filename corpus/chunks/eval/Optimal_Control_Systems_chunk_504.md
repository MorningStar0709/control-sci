# C.3 MATLAB© for Matrix Difference Riccati Equation

% diagonals to create a new matrix M   
```matlab
j=n;
[m1,index1]=sort(real(diag(D)));
for i=1:1:n
    m2(i)=m1(j);
    index2(i)=index1(j);
    index2(i+n)=index1(i+n);
    j=j-1;
end
Md=diag(m2); 
```  
%Rearrange W so that it corresponds to the % sort of the eigenvalues

```matlab
for i=1:2*n
    w2(:,i)=W(:,index2(i));
end
W=w2; 
```

%Define the Modal Matrix for D and split it into parts   
```matlab
W11=zeros(n);
W12=zeros(n);
W21=zeros(n);
W22=zeros(n);
j=1;
for i=1:2*n:(2*n*n-2*n+1)
    W11(j:j+n-1)=W(i:i+n-1);
    W21(j:j+n-1)=W(i+n:i+2*n-1);
    W12(j:j+n-1)=W(2*n*n+i:2*n*n+i+n-1);
    W22(j:j+n-1)=W(2*n*n+i+n:2*n*n+i+2*n-1);
    j=j+n;
end 
```

```matlab
%Find M
M=zeros(n);
j=1;
for i=1:2*n:(2*n*n-2*n+1) 
```

```matlab
M(j:j+n-1)=D(i:i+n-1);
j=j+n;
end

%Zero Vectors
x=zeros(n,1);

%Define Loop Variables (l=lambda)
k0=kspan(1);
kf=kspan(2);

%x and P Conditions
x(:,1)=x0(:,1);
Tt=-inv(W22-F*W12)*(W21-F*W11);
P=real((W21+W22*((Md^-(kf-0))*Tt*(Md^-(kf-0))))...
*inv(W11+W12*((Md^-(kf-0))*Tt*(Md^-(kf-0)))));
L=inv(R)*B'*(inv(A))'(P-Q);
u(:,1)=-L*x0(:,1);
k1(1)=0;

for k=(k0+1):1:(kf)
    Tt=-inv(W22-F*W12)*(W21-F*W11);
    P=real((W21+W22*((Md^-(kf-k))*Tt*(Md^-(kf-k))))...
*inv(W11+W12*((Md^-(kf-k))*Tt*(Md^-(kf-k)))));
    L=inv(R)*B'*(inv(A))'(P-Q);
    x(:,k+1)=(A-B*L)*x(:,k);
    u(:,k+1)=-L*x(:,k+1);
    k1(k+1)=k;
end

%Plotting Section, if desired
if plotflag~=1

%Plot Riccati coefficients using flag variables
% to hold and change colors
%Variables are plotted one at a time and the plot held
fig=1; %Figure number 
```

C.3 MATLAB© for Matrix Difference Riccati Equation

```matlab
cflag=1; %Variable used to change plot color
j=1;
Ps=0.; %Initialize P Matrix plot variable
for i=1:1:n*n
    for k=(k0):1:(kf)
    Tt=-inv(W22-F*W12)*(W21-F*W11);
    P=real((W21+W22*((Md^-(kf-k))*Tt*(Md^-(kf-k))))...
*inv(W11+W12*((Md^-(kf-k))*Tt*(Md^-(kf-k)))));
    Ps(j)=P(i);
    k2(j)=k;
    j=j+1;
    end
    if cflag==1;
    figure(fig);
    plot(k2,Ps,'b')
    title('Plot of Riccati Coefficients')
    grid on
    xlabel('k')
    ylabel('P Matrix')
    hold
    cflag=2;
    elseif cflag==2
    plot(k2,Ps,'b')
    cflag=3;
    elseif cflag==3
    plot(k2,Ps,'b')
    cflag=4;
    elseif cflag==4
    plot(k2,Ps,'b')
    cflag=1;
    fig=fig+1;

end
    Ps=0.;
    j=1;
end
if cflag==2|cflag==3|cflag==4
    hold
    fig=fig+1; 
```

end   
```matlab
%Plot Optimized x
