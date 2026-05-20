```matlab
function dc=sys1(t,c)
dc1=c(2);
dc2=c(3);
if (c(1)>1)
    dc3=-0.15*c(3)-0.005*c(2)-20*c(1)+20;
elseif (abs(c(1))<1)
    dc3=-0.15*c(3)-0.005*c(2);
else
    dc3=-0.15*c(3)-0.005*c(2)-20*c(1)-20;
end
dc=[dc1 dc2 dc3]'; 
```

调用函数：当仪表伺服系统 $G(s)=\frac{20}{s(10s+1)}$

```matlab
function dc=sys2(t,c)
dc1=c(2);
if (c(1)>1)
    dc2=-0.1*c(2)-2*c(1)+2;
elseif (abs(c(1))<1)
    dc2=-0.1*c(2);
else
    dc2=-0.1*c(2)-2*c(1)-2;
end
dc=[dc1 dc2]'; 
```

(4) 仿真结果

运行 M 文件, 作 $G(j\omega)=\frac{4000}{j\omega(1+j20\omega)(1+j10\omega)}$ 曲线与 $-\frac{1}{N(A)}$ 曲线, 如图 8-64(a) 所示; 当初始条件 $c(0)=2$ 时, 系统的零输入响应如图 8-64(b) 所示。由图可知, 仪表伺服系统在取

$G(s) = \frac{4000}{s(20s + 1)(10s + 1)}$ 时，存在不稳定自振。令 $\operatorname{Im} G(\mathrm{j}\omega) = 0$ ，得频率 $\omega_{c} = 0.0707$ 。同时由 $G(\mathrm{j}\omega_{c}) = -\frac{1}{N(A_{c})}$ ，得振幅 $A_{c} = 1.001$ 。

![](image/1517c983841a2a2e052f547f029a5bc43e6b21799b75605c8477f727d356a0de.jpg)

<details>
<summary>other</summary>

| Real Axis (×10⁴) | Imaginary Axis (×10⁴) |
| --- | --- |
| -6 | 3 |
| -3 | 0 |
| 0 | 0 |
| -6 | -3 |
| -3 | -1 |
| 0 | 0 |
</details>

(a) 系统的 $\Gamma_G$ 和 $-1 / N(A)$ 曲线

![](image/28e60b6d471a785cf1f43d5e79344f260b7ca133bb9462111965f1456e3d7bc3.jpg)

<details>
<summary>line</summary>

| Time/sec | c(t) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 10000 |
| 7 | -7000 |
| 8 | 15000 |
</details>

(b) 零输入时间响应  
图8-64 $G(s) = \frac{4000}{s(20s + 1)(10s + 1)}$ 时，有死区的仪表伺服系统特性(MATLAB)

同理，作 $G(s) = \frac{20}{s(10s + 1)}$ 曲线与 $-1 / N(A)$ 曲线，如图8-65(a)所示；当初始条件 $c(0) = 2$ 时，系统的零输入响应如图8-65(b)所示。由图可见， $\Gamma_G$ 曲线不包围 $-1 / N(A)$ 曲线，仪表伺服系统稳定。

![](image/5478532d7837c0d66fe74c6299427e1db82ce3add8ce3d163a2552dffbdf4c9e.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -2.0 | 0.0 |
| -1.0 | 0.0 |
| 0.0 | 0.0 |
</details>

(a) 系统的 $\Gamma_{G}$ 和 $-1/N(A)$ 曲线

![](image/f998f70b9da53b1d6d9cf69dcd33a0f614f6f0622a56ceb8e1006a93ecfbf8fe.jpg)

<details>
<summary>line</summary>

| Time/sec | c(t) |
| --- | --- |
| 0 | 2.0 |
| 10 | -1.8 |
| 20 | 1.2 |
| 40 | -1.0 |
| 60 | -0.5 |
| 80 | -0.5 |
| 100 | -0.5 |
| 120 | -0.5 |
</details>

(b) 零输入时间响应  
图 8-65 $G(s)=\frac{20}{s(10s+1)}$ 时，有死区的仪表伺服系统特性(MATLAB)
