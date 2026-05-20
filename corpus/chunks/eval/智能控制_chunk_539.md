# 基于遗传算法的 TSP 问题优化仿真程序

(1) 主程序: chap10\_2.m

clc;

```matlab
clear all;
close all;
global x y

M=2;
if M==1
    cityfile = fopen('city8.txt', 'rt');
    cities = fscanf(cityfile, '%f%f',[2,inf]);
    fclose(cityfile);
    t=8+1; % Number of Cities is t-1
    s=30; % Number of Samples
    G=50;
    c=10;
elseif M==2
    cityfile = fopen('city30.txt', 'rt');
    cities = fscanf(cityfile, '%f%f',[2,inf]);
    fclose(cityfile);
    t=30+1; % Number of Cities is t-1
    s=1500; % Number of Samples
    G=300;
    c=25;
end

x=cities(1,:);
y=cities(2,:);

pc=0.10;
pm=0.8;

pop=zeros(s,t);
for i=1:s
    pop(i,1:t-1)=randperm(t-1); % Create Natural number from 1 to t-1
end

for k=1:1:G % Begin of GA
if mod(k,50)==1
    k
end

pop=chap10_2dis(pop);

pop=chap10_2select(pop,c);

p1=rand;
if p1>=pc
    pop=chap10_2cross(pop);
end

p2=rand;
if p2>=pm
    pop=chap10_2mutate(pop);
end 
```

```matlab
end % End of GA
percentages
%
bestL=min(pop(:,t))
J=pop(:,t);
fi=1./J;

[Oderfi,Indexfi]=sort(fi); % Arranging fi small to bigger
BestS=pop(Indexfi(s),:); % Let BestS=E(m), m is the Indexfi belong to max(fi)

I=BestS;
% disp('Best Sample is:');disp(I);

for i=1:1:t-1
    x1(i)=x(I(i));
    y1(i)=y(I(i));
end
x1(t)=x(I(1));
y1(t)=y(I(1));

cities_new=[x1;y1];
disp('Best Route is:');disp(cities_new);
pos=[cities_new cities_new(:,1rows);
lentemp=0;
for i=1:1:t-1
    temp=sqrt((pos(1,i)-pos(1,i+1))^2+(pos(2,i)-pos(2,i+1))^2);
    lentemp=lentemp+temp;
end
disp('Shortest Length is:');disp(lentemp);

figure(1);
subplot(1,2,1);
x(t)=x(1);y(t)=y(1);
plot(x,y,'-or');
xlabel('X axis'), ylabel('Y axis'), title('Original Route');
axis([0,1,0,1]);
if M==2
    axis([0,100,0,100]);
end
axis on
hold on;
subplot(1,2,2);
plot(x1,y1,'-or');
xlabel('X axis'), ylabel('Y axis'), title('New Route');
axis([0,1,0,1]);
if M==2
    axis([0,100,0,100]);
end
axis on 
```

(2) 距离计算函数(求适应度函数): chap10\_2dis. m  
```matlab
function [pop]=qiujuli(pop)
global x y
[s,t]=size(pop);

for i=1:1:s
    dd=0;
    pos=pop(i,1:t-1);
    pos=[pos pos(:,1)];
    for j=1:1:t-1
    m=pos(j);
    n=pos(j+1);
    dd=dd+sqrt((x(m)-x(n))^2+(y(m)-y(n))^2);
    end
    pop(i,t)=dd;
end 
```

(3) 选择算子函数: chap10\_2select.m   
```matlab
function [pop]=select(pop,c)
[s,t]=size(pop);
m11=(pop(:,t));
m11=m11';
mmax=zeros(1,c);
mmin=zeros(1,c);

num=1;
while num<c+1 % 取距离大的 c 个样本
    [a,mmax(num)]=max(m11); % 选择当前样本最大值，并记录样本编号给 mmax(num)
    m11(mmax(num))=0;
    num=num+1;
end
