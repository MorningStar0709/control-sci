# 2. YALMIP 工具箱仿真实例

求解下列 LMI 问题。

LMI 不等式为

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {F} ^ {\mathrm{T}} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} + \boldsymbol {P B F} < 0$$

已知矩阵 A、B、P，求矩阵 F。

具体的一个求解实例如下：取 $A = \begin{bmatrix} -2.548 & 9.1 & 0\\ 1 & -1 & 0\\ 0 & -14.2 & 0 \end{bmatrix}$ ， $B = \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix}$ ， $P =$ $\left[ \begin{array}{ccc}1000000 & 0 & 0\\ 0 & 1000000 & 0\\ 0 & 0 & 1000000 \end{array} \right]$ ，解该LMI式，可得 $F = \left[ \begin{array}{ccc} - 492.4768 & -5.05 & 0\\ -5.05 & -494.0248 & 6.6\\ 0 & 6.6 & -495.0248 \end{array} \right]$ 。

〖仿真程序〗 chap16\_1.m

```matlab
clearall;
closeall;
A=[-2.548 9.1 0;1 -1 1;0 -14.2 0];
B=[1 0 0;0 1 0;0 0 1];
F=sdpvar(3,3);
M=sdpvar(3,3);
P=1000000*eye(3);
FAI=(A'+F'*B')*P+P*(A+B*F);
%LMI description
L=set(FAI<0);
solvesdp(L);
F=double(F)
```

![](image/0c8e59acd9a6de9b4f5b525cead902771092759979c048313f9de431f5e4d441.jpg)
