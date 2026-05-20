# 高斯基函数的参数对 RBF 网络逼近的影响仿真程序: chap7\_8.m

```txt
% RBF approximation test
clear all;
close all;
```

```txt
alfa=0.05;
xite=0.5; 
```

$x=\left[0,0\right]'$ ;

% The parameters design of Gaussian Function

% The input of RBF (u(k), y(k)) must be in the effect range of Gaussian function overlay

% The value of b represents the width of Gaussian function overlay

Mb=1;  
```matlab
if Mb==1 % The width of Gaussian function is moderate
    b=1.5*ones(5,1);
elseif Mb==2 % The width of Gaussian function is too narrow, most overlap of the function
% is near to zero
    b=0.0005*ones(5,1);
end 
```

% The value of c represents the center position of Gaussian function overlay

% the NN structure is 2-5-1: i=2; j=1,2,3,4,5; k=1

Mc=1;   
```matlab
if Mc==1 % The center position of Gaussian function is moderate
c=[-1.5 -0.5 0 0.5 1.5;
    -1.5 -0.5 0 0.5 1.5]; % cij
elseif Mc==2 % The center position of Gaussian function is improper
c=0.1* [-1.5 -0.5 0 0.5 1.5;
    -1.5 -0.5 0 0.5 1.5]; % cij 
```  
end

```javascript
w=rands(5,1);
w_1=w; w_2=w_1;
y_1=0; 
```

ts=0.001;   
```txt
for k=1:1:2000 
```

time(k)=k\*ts;   
```javascript
u(k)=0.50*sin(1*2*pi*k*ts); 
```  
y(k)=u(k) $^{3}$ +y\_1/(1+y\_1^2);

```javascript
x(1)=u(k);
x(2)=y(k);
```

for j=1:1:5   
```javascript
h(j)=exp(-norm(x-c(:,j))^2/(2*b(j)*b(j))); 
```  
end

```txt
ym(k) = w' * h';
em(k) = y(k) - ym(k); 
```

d\_w=xite\*em(k)\*h';   
```javascript
w=w_1+d_w+alfa*(w_1-w_2); 
```

y\_1=y(k);   
```javascript
w_2=w_1; w_1=w; 
```

```txt
end
figure(1);
plot(time,y,'r',time,ym,'b:','linewidth',2);
xlabel('time(s)');ylabel('y and ym');
legend('Ideal value','Approximation value'); 
```

隐含层节点数对 RBF 网络逼近的影响仿真程序: chap7\_9.m  
```matlab
% RBF approximation test
clear all;
close all;

alfa=0.05;
xite=0.3;
x=[0,0]';
% The parameters design of Gaussian Function
% The input of RBF (u(k),y(k)) must be in the effect range of Gaussian function overlay
% The value of b represents the width of Gaussian function overlay

bj=1.5;    % The width of Gaussian function
% The value of c represents the center position of Gaussian function overlay
% the NN structure is 2-m-1: i=2; j=1,2,...,m; k=1
M=3;    % Different hidden nets number
if M==1    % only one hidden net
m=1;
c=0;
elseif M==2
m=3;
c=1/3* [-1 0 1;
    -1 0 1];
elseif M==3
m=7;
c=1/9* [-3 -2 -1 0 1 2 3;
    -3 -2 -1 0 1 2 3];
end
w=zeros(m,1);
w_1=w;w_2=w_1;
y_1=0;

ts=0.001;
for k=1:1:5000

time(k)=k*ts;
u(k)=sin(k*ts);

y(k)=u(k)^3+y_1/(1+y_1^2);

x(1)=u(k);
x(2)=y(k); 
```
