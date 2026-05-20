(a) 校正后的根轨迹   
```txt
G0=tf([1],[1,15,50,0]);
Gc=tf([1,0.1],[1,0.01]);
G=series(G0,Gc);
rlocus(G);hold on;
axis([-15,1,-10,10]);
zeta=0.59;wn=2.49;
x=[-10:0.1:-zeta*wn];y=-sqrt((1-zeta^2)/zeta)*x;
xc=[-10:0.1:-zeta*wn];c=sqrt(wn^2-xc.^2);
plot(x,y,'-',x,-y,'-',xc,c,'-',xc,-c,'-');
xlabel('实轴');ylabel('虚轴') 
```  
(b) MATLAB 文本

图 6-42 滞后校正  
![](image/fb3bca680b8e9b201a6f12edc44bf58f3016746ffa89f294571ff446ab9bc7f2.jpg)

<details>
<summary>line</summary>

| Time | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.15 |
| 2 | 1.05 |
| 4 | 1.03 |
| 6 | 1.02 |
| 8 | 1.02 |
| 10 | 1.02 |
| 12 | 1.02 |
| 14 | 1.02 |
| 16 | 1.02 |
| 18 | 1.02 |
| 20 | 1.02 |
</details>

(a) 校正后的系统阶跃响应  
图 6-43 滞后校正系统的时间响应(MATLAB)

```matlab
G0=tf([1],[1,15,50,0]);
Gc=tf(100*[1,0.1],[1,0.01]);
G=series(G0,Gc);
G1=feedback(G,1); %系统的闭环传递函数
step(G1);grid
(b) MATLAB 文本 
```  
图 6-43 滞后校正系统的时间响应(MATLAB)(续)

表 6-4 采用 MATLAB 得到的校正设计结果

<table><tr><td>校正方案</td><td>增益放大器K1</td><td>超前校正网络</td><td>滞后校正网络</td></tr><tr><td>阶跃响应超调量</td><td>70%</td><td>8%</td><td>13%</td></tr><tr><td>调节时间/s</td><td>8</td><td>1</td><td>4</td></tr><tr><td>斜坡输入的稳态误差</td><td>10%</td><td>20%</td><td>5%</td></tr><tr><td>Kv</td><td>10</td><td>5</td><td>20</td></tr></table>
