# 差分进化算法参数辨识仿真程序

1. 模型测试程序: chap10\_7.m  
```txt
clear all;
close all;
g=1;
```

```matlab
h=2;
k1=1;
k2=0.5;

xmin=-4;
xmax=4;
N=(xmax-xmin)/0.1+1;

for i=1:1:N
    x(i)=xmin+(i-1)*0.10;
    x_abs=abs(x(i));
if x_abs<=g
    y(i)=0;
elseif x_abs> g&&x_abs<=h
    y(i)=k1*(x(i)-g*sign(x(i)));
elseif x_abs>=h
    y(i)=k2*(x(i)-h*sign(x(i))+k1*(h-g)*sign(x(i));
end
end

save del_file N x y; 
```
