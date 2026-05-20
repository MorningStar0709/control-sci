# 2.10.2 仿真实例

被控对象传递函数为

$$G (s) = \frac {1 . 5}{5 0 s ^ {2} + a _ {2} s ^ {2} + a _ {1} s + 1}$$

式中， $a_{2}=43$ ; $a_{1}=3$ 。

系统包含控制输入饱和环节 $\pm1.0$ 和速度限制环节 $\pm0.8$ 两个非线性环节。系统含有不确定因素： $a_{2}$ 在 40～50 之间变化， $a_{1}$ 在 $(0.5\sim2.0)\times3$ 之间变化。采用 PID 控制器，PID 的优化指标为：

(1) 最大超调量不大于 20%;  
(2) 上升时间不大于 20s;  
（3）调整时间不大于30s；  
(4) 系统具有鲁棒性。

仿真程序包括两个部分：Simulink 程序及初始化的 M 函数程序。采用 MATLAB 中的非线性系统设计工具箱 NCD 可实现 PID 控制器的优化。

基于 NCD 的 PID 控制器优化步骤如下。

第一步：参数初始化，首先运行初始化程序 chap2\_12int.m，实现 PID 控制算法中 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 和被控对象 $a_{2}$ 、 $a_{1}$ 的初始化。

第二步：运行 Simulink 主程序 chap2\_12sim.mdl，可得到初始 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 下的 PID 控制响应结果。

第三步：打开 NCD 环境，如果是第一次 NCD 优化，则需要进行参数的初始化，否则可调用以前的优化参数文件\*.mat。

第四步：单击 Start 功能，实现 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 的优化，优化完成后，可在 Matlab 环境下得到 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 的优化结果。

第五步：再运行 Simulink 主程序 chap2\_12sim.mdl，可得到优化 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 下的 PID 控制响应结果。每次优化结果需要通过 NCD 环境下的 Save 功能保存在 \*.mat 文件中，

仿真的关键是 NCD 功能的使用。在 Simulink 环境中双击 NCD Output 模块，弹出 NCD Blockset 约束窗口，通过 Options 菜单和 Parameters 菜单实现该功能的使用。具体说明

如下：

(1) Options 菜单的使用

① 通过 Step Response 命令定义阶跃响应性能指标，如图 2-30 所示。

Setting time: 调整时间，选 30s。

Rise time: 上升时间，选 20s。

Persent setting: 稳态误差百分数，取 5。

Persent overshot: 超调量百分数，取 20。

Persent undershot: 振荡负幅值百分数，取 1。

Step time: 启动时间，取 0。

Final time: 终止时间，取 100。

Initial output: 初始值，取 0。

Final output: 最终值，取 1。

![](image/651089d95fcadcadb980410efe244a3689807c4dc77bd709cd5785fe4c51c1fe.jpg)

<details>
<summary>text_image</summary>

Step Response
Input step response characteristics.
Settling time 30 Rise time 20
Percent settling 5 Percent rise 90
Percent overshoot 20 Percent undershoot 1
Step time 0 Final time 100
Initial output 0 Final output 1
Done Revert Help
</details>

图 2-30 Step Response 设置图

② 通过 Time range 命令，设置优化时间，取 0～100s

③ 通过选择 Y-Axis 命令，设置阶跃响应范围，取 [-0.131, 1.321]

(2) Optimization 菜单的使用

① 选择 Parameters 项，定义调整变量及有关参数，如图 2-31 所示。

输入：待调整优化变量 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 及它们的上下限，可取为

下限：0 0 0

上限：100 100 100

变量允差：0.001

约束允差：0.001

![](image/fe622e46173b1da427aaacf41dfd1fc083409fa412bb02df9e8f21a709d432ca.jpg)

<details>
<summary>text_image</summary>
