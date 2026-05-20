# (7) 综合应用

例 B-9 设系统状态方程为

$$
\dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c c} - 2 & 2 & - 1 \\ 0 & - 2 & 0 \\ 1 & - 4 & 0 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right] \boldsymbol {u} (t), \boldsymbol {y} (t) = \left[ \begin{array}{l l l} 1 & 0 & 1 \end{array} \right] \boldsymbol {x} (t), \boldsymbol {x} (0) = \left[ \begin{array}{l} 1 \\ - 2 \\ 3 \end{array} \right]
$$

要求：

1) 判断系统的稳定性，并绘制系统的零输入状态响应曲线；  
2) 求系统传递函数，并绘制系统在初始状态作用下的输出响应曲线；  
3) 判断系统的可控性, 如有可能, 将系统状态方程化为可控标准型;  
4) 判断系统的可观测性,对系统进行可观测性分解,并求出系统的最小实现。

解 1) 利用李雅普诺夫第二法判断系统的稳定性。选定 Q 为单位阵，求解李雅普诺夫方程，得对称矩阵 P。若 P 正定，即 P 的全部特征根均为负数，系统稳定。

2) 系统的传递函数 $G(s)=c(sI-A)^{-1}b$ 。  
3）系统的可控标准型实现可按如下步骤求解：

① 计算系统的可控性矩阵 S，并利用秩判据判断系统的可控性；  
② 若系统可控, 计算可控性矩阵的逆阵 $S^{-1}$ ;  
③ 取出 $S^{-1}$ 的最后一行构成 $p_{1}$ 行向量；  
④ 构造 T 阵

$$
\boldsymbol {T} = \left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {1} \boldsymbol {A} \\ \vdots \\ \boldsymbol {p} _ {1} \boldsymbol {A} ^ {n - 1} \end{array} \right]
$$

⑤ 利用相似变换矩阵 T 将非标准型可控系统化为可控标准型。

4) 计算系统的可观测性矩阵 V，利用秩判据判断系统的可观测性，并对系统进行可观测性分解，其中的可控、可观测子系统即为系统的最小实现。

MATLAB 程序: example9.m

$$\mathrm{A} = [ - 2 2 - 1; 0 - 2 0; 1 - 4 0 ]; \mathrm{b} = [ 0 1 1 ] ^ {\prime}; \mathrm{c} = [ 1 0 1 ]; \mathrm{d} = 0;\mathrm{N} = \text { size } (\mathrm{A}); \mathrm{n} = \mathrm{N} (1);\mathrm{Q} = \text { eye } (3);\mathrm{P} = \text { lyap } (\mathrm{A} ^ {\prime}, \mathrm{Q})\mathrm{e} = \operatorname{eig} (\mathrm{P})\mathrm{sys} = \mathrm{ss} (\mathrm{A}, \mathrm{b}, \mathrm{c}, \mathrm{d});$$

%选定 $Q$ 为单位阵

$\%$ 求对称阵 $\pmb{P}$

%利用特征值判断对称阵 P 是否正定

%建立系统的状态空间模型

[y,t,x]=initial(sys,[1-23]'); %计算系统的零输入响应
figure(1)
plot(t,x); grid %绘制系统零输入响应状态曲线
xlabel('t(s)');ylabel('x(t)');title('initial response');
figure(2)
plot(t,y);grid %绘制系统零输入响应输出曲线
xlabel('t(s)');ylabel('y(t)');title('initial response');
[num,den]=ss2tf(A,b,c,d) %将系统状态空间模型转换成传递函数模型
S=ctrb(A,b); %计算可控性矩阵 S
f=rank(S) %通过 rank 命令求可控性矩阵的秩
if f==n %判断系统的可控性
    disp('system is controlled')
else
    disp('system is no controlled')
end
V=obsv(A,c); %计算可观测性矩阵 V
m=rank(V) %求可观测性矩阵的秩
if m==n %判断系统的可观测性
    disp('system is observable')
else
    disp('system is no observable')
end
S1=inv(S); %通过 inv 命令求矩阵的逆 $S^{-1}$ T=[S1(3,:);S1(3,:)*A;S1(3,:)*A^2]; %求变换矩阵 T
sys1=ss2ss(sys,T) %通过相似变换矩阵 T 将系统化为可控标准型
[A1,b1,c1,T1]=obsvf(A,b,c) %系统可观测性分解
sysr=minreal(sys); %求系统的最小实现
