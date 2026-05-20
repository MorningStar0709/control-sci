<table><tr><td></td><td>系统方程</td><td>原点稳定性</td><td>充分必要条件或充分条件</td></tr><tr><td rowspan="2">间接法</td><td rowspan="2">x=Ax,t≥0x(0)=x0</td><td>稳定</td><td>A的所有特征值均具有非正(负或零)实部,且具有零实部的特征值为A的最小特征多项式的单根</td></tr><tr><td>渐近稳定</td><td>A的所有特征值均具有负实部</td></tr><tr><td rowspan="8">直接法</td><td rowspan="4">x=f(x,t)f(0,t)=0t≥t0</td><td>稳定</td><td>V(x(t1;x0,t0),t)正定有界,V(x(t1;x0,t0),t)存在且连续,负定且有界</td></tr><tr><td>一致渐近稳定</td><td>V(x(t1;x0),t)正定有界,V(x(t1;x0),t)存在且连续,负定且有界</td></tr><tr><td>全局一致渐近稳定</td><td>V(x(t1;x0,t0),t)正定有界,V(x(t1;x0,t0),t)存在且连续,负定且有界,并且当||x||→∞时,V(x,t)→∞</td></tr><tr><td>不稳定</td><td>V(x(t1;x0,t0),t)在原点某一邻域内正定且有界,V(x(t1;x0,t0),t)在同样的领域内存在且连续,但为正定</td></tr><tr><td rowspan="4">x=f(x)f(0)=0t≥t0</td><td>稳定</td><td>V(x)正定,V(x)负半定</td></tr><tr><td>渐近稳定</td><td>V(x)正定,V(x)负定或V(x)负半定且V(x;x0,0)不恒等于零</td></tr><tr><td>全局渐近稳定</td><td>满足渐近稳定条件,并且当||x||→∞时,V(x)→∞</td></tr><tr><td>不稳定</td><td>V(x)正定,V(x)正定</td></tr><tr><td rowspan="5">直接法</td><td>x=A(t)x
x(t0)=x0
t≥t0</td><td>一致渐近稳定</td><td>对任意给定的一个实对称、一致有界和一致正定的时变矩阵Q(t),有唯一的实对称、一致有界和一致正定的时变矩阵P(t)存在,并使-P(t)=P(t)A(t)+AT(t)P(t)+Q(t)成立</td></tr><tr><td>x=Ax,t≥0
x(0)=x0</td><td>全局一致渐近稳定</td><td>对给定的任一个正定对称矩阵Q,有唯一存在的正定对称矩阵P,使ATP+PA=-Q成立</td></tr><tr><td rowspan="2">x(k+1)=f(x(k))
f(0)=0
k=1,2,...</td><td rowspan="2">全局一致渐近稳定</td><td>V(x(k))正定
ΔV(x(k))=V(x(k+1))-V(x(k))负定
当||x(k)||→∞时,V(x(k))→∞</td></tr><tr><td>V(x(k))正定,ΔV(x(k))负半定,由任意初始状态x(0)所确定的系统轨线x(k)的ΔV(x(k))不恒为零,||x(k)||→∞时,V(x(k))→∞</td></tr><tr><td>x(k+1)=Gx(k)
x(0)=x0</td><td>渐近稳定</td><td>给定一正定对称矩阵Q,存在一个正定对称矩阵P,使GTPG-P=-Q成立</td></tr></table>
