1) 能否通过状态反馈将系统的闭环极点配置在 -1, -2 和 -3 处？如有可能，求出上述极点配置的反馈增益矩阵 k；  
2) 当系统的状态不可直接测量时,能否通过状态观测器来获取状态变量? 如有可能,试设计一个极点位于-3、-5和-7的全维状态观测器。

解 本题设计步骤如下：

1) 检查系统的可控、可观测性。若被控系统可控可观测，则满足分离定理，用状态观测器估

值形成状态反馈时,其系统的极点配置和观测器设计可分别独立进行。

2）对于系统 $\dot{x}=Ax+bu$ ，选择状态反馈控制律 $u=-kx+v$ ，使得通过反馈构成的闭环系统极点，即 $(A-bk)$ 的特征根配置在期望极点处。  
3）构造全维状态观测器 $\hat{x} = A\hat{x} +bu - hc(\hat{x} -x) = (A - hc)\hat{x} +bu + hy$ ，设计观测器输出反馈阵 $\pmb{h}$ ，使得观测器极点，即 $(A - hc)$ 的特征根位于期望极点处。  
4）利用分离定理分别设计上述状态反馈控制律和观测器，得复合系统动态方程为

$$
\left[ \begin{array}{c} \dot {\boldsymbol {x}} \\ \dot {\boldsymbol {x}} \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {A} & - \boldsymbol {b k} \\ \boldsymbol {h c} & \boldsymbol {A} - \boldsymbol {b k} - \boldsymbol {h c} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {x} \\ \dot {\boldsymbol {x}} \end{array} \right] + \left[ \begin{array}{c} \boldsymbol {b} \\ \boldsymbol {b} \end{array} \right] v

y = \left[ \begin{array}{l l} \boldsymbol {c c} & 0 \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} \\ \hat {\boldsymbol {x}} \end{array} \right]
$$

MATLAB 程序: example10.m  
A=[-2 -2.5 -0.5;1 0 0;0 1 0];b=[1 0 0]';
c=[1 4 3.5];d=0;
N=size(A);n=N(1);
sys0=ss(A,b,c,d); %建立系统状态空间模型
S=ctrb(A,b) %求{A,b}可控性矩阵的秩
f=rank(S); %求可控性矩阵的秩
if f==n %判断系统的可控性
    disp('system is controlled')
else
    disp('system is no controlled')
end
V=obsv(A,c) %计算系统可观测性矩阵
m=rank(V); %求{A,c}可观测性矩阵的秩
if m==n %判断系统的可观测性
    disp('system is observable')
else
    disp('system is no observable')
end
P_s=[-1 -2 -3]; %系统的期望配置极点
k=acker(A,b,P_s) %计算系统的反馈增益向量 k
P_o=[-3 -5 -7] %观测器的期望配置极点
h=(acker(A',c',P_o))' %计算观测器输出反馈阵
A1=[A-b*k;h*c A-b*k-h*c];b1=[b;b];c1=[c zeros(1,3)];d1=0;
x0=[1 -0.75 0.4]';x10=[0 0 0]';
sys=ss(A1,b1,cl,d1); %建立复合系统动态模型
t=0:0.01:4;
[y,t,x]=initial(sys,[x0;x10],t); %计算系统的零输入响应
figure(1);

```matlab
plot(t,x(:,1:3));grid %零输入响应系统状态曲线
xlabel('t(s)');ylabel('x(t)');
figure(2)
plot(t,x(:,4:6));grid; %零输入响应观测状态曲线
xlabel('t(s)');ylabel('x(t)');
figure(3)
plot(t,(x(:,1:3)-x(:,4:6)));grid; %零输入响应状态误差曲线
xlabel('t(s)');ylabel('e(t)'); 
```

在 MATLAB 中运行 M 文件 example10 后, 结果如下:

1）由于系统可控，满足极点配置条件，得反馈增益向量 $k = [4\quad 8.5\quad 5.5]$ 。  
2）由于系统可观测，满足观测器极点配置条件，得观测器输出反馈矩阵

$$
\boldsymbol {h} = \left[ \begin{array}{l l l} 3 5. 2 3 2 4 & - 1 9. 8 1 6 9 & 1 6. 2 9 5 8 \end{array} \right] ^ {\mathrm{T}}
$$
