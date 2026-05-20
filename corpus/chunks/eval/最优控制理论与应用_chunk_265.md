但是实际上导弹不可能确切地在碰撞三角区发射,所以不能精确地得到拦截点。因为不知道目标将会如何机动,所以拦截点位置只能大概地估计。事实上,这也是需要导航系统的原因。初始时刻导弹偏离碰撞三角的角度称之为指向角误差(Head-Error)。考虑了导弹初始时刻的指向角和指向角误差之后,导弹的初始速度分量可以表示为

$$\boldsymbol {V} _ {M \gamma} (0) = \boldsymbol {V} _ {M} \cos (\boldsymbol {q} - \boldsymbol {L} + \text {HeadError}) \tag {12-54}\boldsymbol {V} _ {M x} (0) = \boldsymbol {V} _ {M} \sin (\boldsymbol {q} - \boldsymbol {L} + \text {HeadError}) \tag {12-55}$$

使用 MATLAB 编程, 具体代码如下:

% \* \* \* \* \* \* \* \* \* \* \* \* \* MATLAB 程序 \* \* \* \* \* \* \* \* \* \* \* \* %

%最优制导律仿真,初始化系统的参数

clear all; % 清除所有内存变量

global SignVc;

pi = 3.14159265;

Vm = 1000; Vt = 500; % 导弹和目标的速度

HeadError = 0; % 指向角误差

ThetaT = pi; % 目标的速度方向

$\mathrm{Rmx} = 0; \mathrm{Rmy} = 0;$ % 导弹的位置

$\mathrm{Rtx} = 5000; \mathrm{Rty} = 10000; \%$ 目标的位置

At = 0; % 目标法向加速度

$\mathrm{Vtx} = \mathrm{Vt}*\sin (\mathrm{ThetaT})$ ； $\%$ 目标的速度分量

$\mathrm{Vty} = \mathrm{Vt}*\cos (\mathrm{ThetaT})$

Rtmx = Rtx - Rmx; % 弹目相对距离

Rtmy = Rty - Rmy ;

$\mathrm{AmMax} = 15 * 9.8; \%$ 导弹的最大机动能力为 $15 \mathrm{G}$

Rtm = sqrt(Rtmx^2 + Rtmy^2);

SightAngle = atan(Rtmx/Rtmy);% 视线角

LeadAngle = asin(Vt \* sin(SightAngle - ThetaT)/Vm); % 指向角

$\mathrm{Vmx} = \mathrm{Vm}*\sin (\mathrm{SightAngle} - \mathrm{LeadAngle} + \mathrm{HeadError})$ ;%导弹的速度分量

Vmy = Vm \* cos(SightAngle - LeadAngle + headsError);

$\mathbf{Vtmx} = \mathbf{Vtx} - \mathbf{Vmx}$ ;

Vtmy = Vty - Vmy;

% 弹目的相对运动速度

$\mathrm{Vc} = -(\mathrm{Rtmx}*\mathrm{Vtmx} + \mathrm{Rtmy}*\mathrm{Vtmy}) / \mathrm{Rtm};$

$\mathrm{SignVc} = \mathrm{sign(Vc)}$ ； $\% \mathrm{Vc}$ 的符号

Time = 0; TimeStep = 0.1; % 时间和时间步长

file = fopen('output.txt', 'w'); % 将数据写入文件

% 循环

while(1)

% Vc 改变符号仿真结束

if( sign( Vc) \~ = SignVc )

break;

else

if(Rtm $< 100$ )

TimeStep = 0.005 ;

end

$\mathrm{SignVc} = \mathrm{sign(Vc)}$ ； $\% \mathrm{Vc}$ 的符号

% 视线角速率

dSightAngle = (Rtmy \* Vtmx - Rtmx \* Vtmy) / (Rtm^2);

dTheta = 3 \* Vc \* dSightAngle/Vm;

Theta = atan(Vmx/Vmy);

%导弹加速度

$\mathrm{Am} = \mathrm{Vm}*\mathrm{dTheta};$

%限制机动能力

```txt
if(Am > AmMax) 
```

```javascript
Am = AmMax; 
```

```txt
end 
```

%加速度分量

```javascript
Amx = Am * cos(SightAngle); 
```

```javascript
Amy = - Am * sin(SightAngle); 
```

```txt
Time = Time + TimeStep; 
```

% 目标位置

```txt
Rtx = Rtx + TimeStep * Vtx; 
```

```txt
Rty = Rty + TimeStep * Vty; 
```

```typescript
dThetaT = At/Vt; 
```

```txt
ThetaT = ThetaT + TimeStep * dThetaT; 
```

$\mathrm{Vtx} = \mathrm{Vt} * \sin (\mathrm{ThetaT}) ; \%$ 目标的速度分量
