%进入主要循环，直到满足精度要求
for kg=1:1:G
time(kg)=kg;
%变异
fori=1:Size
    r1=1;r2=1;r3=1;
while(r1==r2||r1==r3||r2==r3||r1==i||r2==i||r3==i)
    r1=ceil(Size * rand(1));
    r2=ceil(Size * rand(1));
    r3=ceil(Size * rand(1));
end
    h(i,:) = P(r1,:) + F*(P(r2,:) - P(r3,:));
    for j=1:CodeL    %检查位置是否越界
if h(i,j)<MinX(j)
h(i,j)=MinX(j);
elseif h(i,j)>MaxX(j)
```

```matlab
h(i,j)=MaxX(j);
end
end

%交叉
for j = 1:1:CodeL
tempr = rand(1);
if (tempr<cr)
v(i,j) = h(i,j);
else
v(i,j) = P(i,j);
end
end

%选择
    if (chap10_2obj(v(i,1),v(i,2))>chap10_2obj(P(i,1),P(i,2)))
P(i,:)=v(i,:);
end
%判断和更新
    if (chap10_2obj(P(i,1),P(i,2))>fi) %判断当此时的位置是否为最优的情况
fi=chap10_2obj(P(i,1),P(i,2));
BestS=P(i,:);
end
end
End
Best_f(kg)=chap10_2obj(BestS(1),BestS(2));
end
BestS    %最佳个体
Best_f(kg)    %最大函数值

figure(1);
plot(time,Best_f(time),'k','linewidth',2);
xlabel('Times');ylabel('Best f'); 
```

(2) 函数计算程序: chap10\_2obj.m

```matlab
function J=evaluate_objective(x1,x2) % 计算函数值
J=100*(x1^2-x2)^2+(1-x1)^2;
end
```

![](image/2cb87c20ed13b46b8fd1368278d719c631948ac9847c789c3c5ce983012a174b.jpg)
