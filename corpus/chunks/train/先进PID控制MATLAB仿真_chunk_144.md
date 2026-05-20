# 1.4.4 实例说明

在控制系统仿真中，通常采用 S 函数描述控制律、自适应律和被控对象。本章采用 S 函数进行控制系统仿真的例子见 1.2.1 节的仿真之三和仿真之四，1.2.2 节的仿真之二和 1.3.2 节的仿真之三。

以 1.2.1 节的仿真之三为例，采用 S 函数实现了控制系统的 Simulink 仿真，仿真主程序为 chap1\_3.mdl。分别采用 S 函数描述控制律和被控对象，介绍如下：

（1）采用 S 函数描述被控对象，见程序 chap1\_3plant.m。利用 S 函数的微分子模块描述被控对象

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - a x _ {2} + b u$$

仿真程序如下：

```matlab
function sys=mdlDerivatives(t,x,u)
sys(1)=x(2);
sys(2)=-(25+10*rands(1))*x(2)+(133+30*rands(1))*u; 
```

（2）采用 S 函数描述 PID 控制器，见程序 chap1\_3s.m。利用 S 函数的输出子模块描述 PID 控制算法，程序如下：

```matlab
function sys=mdlOutputs(t,x,u)
error=u(1);
derror=u(2);
errori=u(3);

kp=60;
ki=1;
kd=3;
ut=kp*error+kd*derror+ki*errori;
sys(1)=ut; 
```

![](image/c7016a48d899607d670c20f4fde1f3a033a77bdcdc1819bc1361223351206b17.jpg)
