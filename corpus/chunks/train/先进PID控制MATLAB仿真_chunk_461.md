# 10.4.2 仿真实例

采样时间为 0.001，输入指令为正弦指令信号 $0.5 \sin 2\pi t$ 。差分进化中使用的样本个数为 30，最优指标权值取 $w_{1} = 0.999$ ， $w_{2} = 0.01$ 。

被控对象程序 chap10\_4plant.m 中，可取 $u_{\mathrm{c}}(k)=0$ ，得到无摩擦补偿情况下的正弦响应，如图 10-7 所示。采用差分进化对摩擦模型参数进行辨识，取 F=0.80，CR=0.60。摩擦模型参数取 $kx=[0.3,1.5]$ ，辨识参数 $kx_{1}$ 和 $kx_{2}$ 的范围选为 [0,3.0]，取进化代数为 50。经过优化获得的最优样本和最优指标为 BestS=[0.4094 1.5548]，即 $kx_{1}=0.4094$ ， $kx_{2}=1.5548$ ，采用 PD 控制加摩擦补偿，正弦响应如图 10-8 所示，代价函数值 J 的优化过程如图 10-9 所示。

![](image/e409891abcbccaa237f392dc4b05e560bdeee360759277c5ddf119310bd65ef3.jpg)

<details>
<summary>line</summary>

| Time(s) | Ideal position signal | Position signal tracking |
| --- | --- | --- |
| 0.00 | 0.00 | 0.00 |
| 0.05 | 0.15 | 0.10 |
| 0.10 | 0.30 | 0.25 |
| 0.15 | 0.40 | 0.35 |
| 0.20 | 0.45 | 0.40 |
| 0.25 | 0.48 | 0.45 |
| 0.30 | 0.47 | 0.46 |
| 0.35 | 0.45 | 0.44 |
| 0.40 | 0.40 | 0.40 |
| 0.45 | 0.30 | 0.35 |
| 0.50 | 0.00 | 0.00 |
</details>

图 10-7 无摩擦补偿的正弦响应

![](image/628e93a6d947fdb41bf16d0071e18fd087f9752ce8acc4cc1a36f6421aeb045a.jpg)

<details>
<summary>line</summary>

| Time(s) | Ideal position signal | Position signal tracking |
| --- | --- | --- |
| 0.00 | 0.00 | 0.00 |
| 0.25 | 0.50 | 0.50 |
| 0.50 | 0.00 | 0.00 |
</details>

图 10-8 采用摩擦补偿的正弦响应

![](image/b3e134f6620103d8ce789a92ab415227b557b2e0ef73ef975935defae138a962.jpg)

<details>
<summary>line</summary>

| Times | Best J |
| --- | --- |
| 0 | 22.5 |
| 5 | 5.5 |
| 10 | 5.5 |
| 15 | 4.0 |
| 20 | 4.0 |
| 25 | 4.0 |
| 30 | 4.0 |
| 35 | 4.0 |
| 40 | 4.0 |
| 45 | 4.0 |
| 50 | 4.0 |
</details>

图10-9 代价函数值 $J$ 的优化过程

〖仿真程序〗 主程序为差分进化程序，子程序为带有摩擦模型的 PD 控制程序。

(1) 主程序: chap10\_4.m

%PD control based on DE Friction parameters estimation

clear all;

close all;

globalyd y timef

F=0.80; % 变异因子：[1,2]

cr=0.6; % 交叉因子

Size=30;

CodeL=2;

```matlab
MinX=zeros(CodeL,1);
MaxX=3.0*ones(CodeL,1);

fori=1:1:CodeL
kxi(:,i)=MinX(i)+(MaxX(i)-MinX(i))*rand(Size,1);
end

BestS=kxi(1,:); %全局最优个体
BsJ=0;
fori=2:Size
if chap10_4plant(kxi(i,:),BsJ)<chap10_4plant(BestS,BsJ)
BestS=kxi(i,:);
end
end
BsJ=chap10_4plant(BestS,BsJ); 
```
