num=1;
while num<c+1 % 取距离小的 c 个样本
    [b,mmin(num)]=min(m11);
    m11(mmin(num))=a;
    num=num+1;
end

for i=1:c
    pop(mmax(i),:)=pop(mmin(i),:); % 用距离大的 c 个样本替换距离小的 c 个样本
end
```

(4) 交叉算子函数: chap10\_2cross.m  
```matlab
function [pop]=chap10_2cross(pop)
[s,t]=size(pop);
pop_1=pop;
n=randperm(s); % 每次进化将种群随机排序
for i=1:2:s 
```

% 选择两个随机交叉点

```matlab
m=randperm(t-3)+1;
crosspoint(1)=min(m(1),m(2));
crosspoint(2)=max(m(1),m(2)); 
```

% 任意取两行交叉

```javascript
x1=n(i);
x2=n(i+1); 
```

% 将 x1 左面与 x2 左面互换

```javascript
middle=pop(x1,1:crosspoint(1));
pop(x1,1:crosspoint(1))=pop(x2,1:crosspoint(1));
pop(x2,1:crosspoint(1))=middle; 
```

% 将 x1 右面与 x2 右面互换

```matlab
middle=pop(x1,crosspoint(2)+1:t);
pop(x1,crosspoint(2)+1:t)=pop(x2,crosspoint(2)+1:t);
pop(x2,crosspoint(2)+1:t)=middle; 
```

% 检查 x1 左面的重复性并得到 x1 左面

```matlab
for j=1:crosspoint(1)
    while find(pop(x1,crosspoint(1)+1:crosspoint(2))==pop(x1,j))
zhi=find(pop(x1,crosspoint(1)+1:crosspoint(2))==pop(x1,j)); % 确定重复的位置
    temp=pop(x2,crosspoint(1)+zhi);
    pop(x1,j)=temp;
end
end 
```

% 检查 x1 右面的重复性并得到 x1 右面

```matlab
for j=crosspoint(2)+1:t-1
    while find(pop(x1,crosspoint(1)+1:crosspoint(2))==pop(x1,j))
    zhi=find(pop(x1,crosspoint(1)+1:crosspoint(2))==pop(x1,j)); % 确定重复的位置
    temp=pop(x2,crosspoint(1)+zhi);
    pop(x1,j)=temp;
    end
end 
```

% 检查 x2 左面的重复性并得到 x2 左面

```matlab
for j=1:crosspoint(1)
    while find(pop(x2,crosspoint(1)+1:crosspoint(2))==pop(x2,j))
zhi=find(pop(x2,crosspoint(1)+1:crosspoint(2))==pop(x2,j)); % 确定重复的位置
    temp=pop(x1,crosspoint(1)+zhi);
    pop(x2,j)=temp;
end
end 
```

% 检查 x2 右面的重复性并得到 x2 右面

```matlab
for j=crosspoint(2)+1:t-1
    while find(pop(x2,crosspoint(1)+1:crosspoint(2))==pop(x2,j))
    zhi=find(pop(x2,crosspoint(1)+1:crosspoint(2))==pop(x2,j)); % 确定重复的位置
    temp=pop(x1,crosspoint(1)+zhi);
    pop(x2,j)=temp;
    end
end
end 
```

% 生成的新种群与交叉前比较,并取两者最优

```javascript
[pop]=chap10_2dis(pop); 
```

```matlab
r i=1:s
    if pop_1(i,t)<pop(i,t)
    pop(i,:)=pop_1(i,:);
    end
end 
```

5) 变异算子函数: chap10\_2mutate. m   
```matlab
unction [pop]=mutate(pop)
s,t]=size(pop);
pop_1=pop;
for i=1:2:s
    m=randperm(t-3)+1; 
```  
% 随机取两个点

```matlab
mutatepoint(1)=min(m(1),m(2));
mutatepoint(2)=max(m(1),m(2)); 
```  
% 采用倒置变异方法倒置两个点的中间部分位置

```matlab
mutate=round((mutatepoint(2)-mutatepoint(1))/2-0.5);
for j=1:mutate
    zhong=pop(i,mutatepoint(1)+j);
    pop(i,mutatepoint(1)+j)=pop(i,mutatepoint(2)-j);
    pop(i,mutatepoint(2)-j)=zhong;
end
end 
```

[pop]=chap10\_2dis(pop);%生成的新种群与变异前比较,并取两者最优   
```matlab
for i=1:s
    if pop_1(i,t)<pop(i,t)
    pop(i,:) = pop_1(i,:);
    end
end 
```
