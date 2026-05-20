$\mathbf{Vty} = \mathbf{Vt}*\cos (\mathbf{ThetaT})$

% 导弹位置

```txt
Rmx = Rmx + TimeStep * Vmx; 
```

```txt
Rmy = Rmy + TimeStep * Vmy; 
```

% 导弹速度

$\mathrm{Vmx} = \mathrm{Vmx} + \text{TimeStep} * \mathrm{Amx}$ ;

```txt
Vmy = Vmy + TimeStep * Amy; 
```

$\mathrm{Vm} = \mathrm{sqrt}(\mathrm{Vmx}^2 + \mathrm{Vmy}^2)$ ;

% 弹目相对位移

```txt
Rtmx = Rtx - Rmx ; 
```

```txt
Rtmy = Rty - Rmy; 
```

%上一步的脱靶量

```txt
Rtm0 = Rtm ; 
```

```javascript
Rtm = sqrt(Rtmx^2 + Rtmy^2); 
```

```txt
SightAngle = atan(Rtmx/Rtmy); % 视线角
```

% 弹目相对速度

$\mathbf{V}\mathrm{tmx} = \mathbf{Vtx} - \mathbf{Vmx};$

```txt
Vtmy = Vty - Vmy ; 
```

$\mathrm{Vc} = -(\mathrm{Rtmx}*\mathrm{Vtmx} + \mathrm{Rtmy}*\mathrm{Vtmy}) / \mathrm{Rtm};$

% 数据写入文件

fprintf(file,'%f%f%f%f%f\n',Time,Rmx,Rmy,Rtx,Rty,sqrt(Amx^2+Amy^2),Rtm);

end

end

status = fclose(file);

仿真结果：

![](image/9a3bb3939a5a6b18774c1c1a524b889468a1bd918aabbeb5e3e887f220d2194d.jpg)

<details>
<summary>line</summary>

| y/m | x/m |
| --- | --- |
| 0 | 0 |
| 1000 | 1000 |
| 2000 | 2000 |
| 3000 | 3000 |
| 4000 | 4000 |
| 5000 | 5000 |
| 6000 | 5000 |
| 7000 | 5000 |
| 8000 | 5000 |
| 9000 | 5000 |
| 10000 | 5000 |
</details>

图12-9 $0^{\circ}$ 指向误差，目标不机动的攻击情况

![](image/4c288b6bb9de0dc0ab74db19a145441a562fc44d9bd8f78301c4683f8ab996c3.jpg)

<details>
<summary>line</summary>

| 时间 (s) | 加速度 (m/s²) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
</details>

图12-10 $0^{\circ}$ 指向误差，目标不机动时导弹的加速度

![](image/c112d8dc85f7bb26fd841e04c6977db822dab901a4a467b5fe5c009b9cc2ad4b.jpg)

<details>
<summary>line</summary>

| y/m | x/m |
| --- | --- |
| 0 | 0 |
| 1000 | 500 |
| 2000 | 1000 |
| 3000 | 1800 |
| 4000 | 2800 |
| 5000 | 3800 |
| 6000 | 5000 |
| 7000 | 5000 |
| 8000 | 5000 |
| 9000 | 5000 |
| 10000 | 5000 |
</details>

图12-11 $-20^{\circ}$ 指向误差，目标不机动时攻击情况  
![](image/901c26e47a488cbbb1895c6f5d449470e47c1a3935a3cc5ebf8f62fb3e97026c.jpg)

<details>
<summary>line</summary>

| 时间 (s) | 加速度 (m/s²) |
| --- | --- |
| 0 | 138 |
| 1 | 120 |
| 2 | 100 |
| 3 | 80 |
| 4 | 60 |
| 5 | 40 |
| 6 | 20 |
| 7 | 10 |
| 8 | 5 |
</details>

图12-12 $-20^{\circ}$ 指向误差，目标不机动时导弹加速度
