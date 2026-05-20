# 1）建立模型。

① 新建模型编辑窗口。在 MATLAB 的命

令窗口中键入 simulink 命令,或用鼠标点击 MATLAB 主界面的图标,打开系统模型库,如图 B-27 所示。这一模型库包含了 Continuous(连续环节),Discontinuities(非线性环节),Discrete(离散环节),Math Operations(数学运算环节),Sinks(输出方式),Sources(输入源)等控制系统分析与设计过程中常用的子模型库。

利用系统模型库界面的 File|New|Model 菜单项或 □ 图标新建一个空白的模型编辑窗口，如图 B-28 所示。

② 建立开环系统模型。对于本题，点击 Continuous(连续环节)子模型库，选择其模型库中的 Transfer Fcn(传递函数)模块 $\frac{1}{s+1}$ ，并将其拖到模型窗口中，再释放鼠标。该模块传递函

![](image/7dc1194cfe76c03c83236e5f85b973c736f141d9297d961e0e3f86a43850b630.jpg)

<details>
<summary>text_image</summary>

Simulink Library Browser
File Edit View Help
Find
Transfer Fcn: Matrix expression for numerator, vector expression for denominator. Output width equals the number of rows in the numerator.
Coefficients are for descending powers of s.
Simulink
Continuous
Discontinuities
Discrete
Look-Up Tables
Math Operations
Model Verification
Model-Wide Utilities
Ports & Subsystems
Signal Attributes
Signal Routing
Sinks
Sources
User-Defined Functions
Aerospace Blockset
CDMA Reference Blockset
Communications Blockset
Control System Toolbox
du/dt Derivative
1/s Integrator
x' = Ax+Bu State-Space
y = Cx+Du
1/s+1 Transfer Fcn
Transport Delay
Variable Transport Delay
(s-1)/s(s+1) Zero-Pole
Ready
</details>

图 B-27 Simulink 模型库

![](image/0700865198b8371688d1a999ddba885392e6fe06888f6811b99362c811f04c2e.jpg)

<details>
<summary>text_image</summary>

untitled
File Edit View Simulation Format Tools Help
Normal
Ready 100% ode45
</details>

图 B-28 新建模型窗口

数的初始形式为 $1 / (s + 1)$ ，若要改变其形式，双击该图标，出现如图B-29所示的模块参数对话框，分别在Numerator(分子)和Denominator(分母)引导的编辑框中填写系统传递函数降幂排列的分子、分母多项式系数向量[0.5]和[1220]，然后选择OK按钮，即可建立无延迟系统的开环传递函数。

由于本题系统存在延迟环节, 因此, 同样在 Continuous(连续环节) 子模型库中选择 Transport Delay(传递函数延迟环节) 模块 ☐, 也将其拖到模型窗口中, 双击图标, 然后在如图 B-30 所示的模块参数对话框 Time delay(延迟时间) 引导的编辑框中输入 0.5, 选择 OK 按钮即完成设置。

![](image/3b56930a6f7e86c70276488df9b69acc2ac9f568f7a47f06a2dfab88982ebb0e.jpg)

<details>
<summary>text_image</summary>

Block Parameters: Transfer Fcn
Transfer Fcn
Matrix expression for numerator, vector expression for denominator. Output width equals the number of rows in the numerator. Coefficients are for descending powers of s.
Parameters
Numerator:
[0.5]
Denominator:
[1 2 2 0]
Absolute tolerance:
auto
OK    Cancel    Help    Apply
</details>

图 B-29 传递函数模块对话框
