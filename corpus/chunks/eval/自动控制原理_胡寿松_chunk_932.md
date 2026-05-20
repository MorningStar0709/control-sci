![](image/923b9f49eddb8c2d410e328a970c525cbcaf13f1d58ef34071f404ab3f7531ba.jpg)

<details>
<summary>text_image</summary>

Block Parameters: Transport Delay
Transport Delay
Apply specified delay to the input signal. Best accuracy
is achieved when the delay is larger than the simulation
step size.
Parameters
Time delay:
1.5
Initial input:
0
Initial buffer size:
1024
Pade order (for linearization):
0
Direct feedthrough of input during linearization
OK	Cancel	Help	Apply
</details>

图 B-30 传递函数延迟环节对话框

③ 确立负反馈信号输入。对于负反馈系统，可首先在 Math Operations(数学运算环节)子模型库中选择 Sum(综合)模块⊕，将其拖入模型窗口中。双击该图标得到如图 B-31 所示对话框，在 List of sign(符号列表)引导的编辑框中键入+-符号(缺省为++)，符号数目表示综合模块输入个数(缺省为 2 输入)，然后选择 OK 按钮，完成反馈属性的(正、负)修正。另外在 Icon shape 引导框中可选择综合模块的样式(圆形或方形，缺省为圆形)。

另外，由于反馈增益为2，同样可在Math Operations(数学运算环节)子模型库中选择Gain（增益）模块1，将其拖入模型窗口后双击该图标，在Gain(增益)引导的编辑框中输入2，然后选择OK按钮，完成增益设置。为使下面模型连接方便，用鼠标右键单击该图标，选择Format|Flip Block菜单项，可实现模块 $180^{\circ}$ 翻转。

④ 确定输入信号。在 Sources(输入源)子模型库中包含了 Step(阶跃输入信号)，Ramp(斜坡输入信号)和 Sine Wave(正弦输入信号)等。本题需要将 Sources(输入源)子模型库中的 Step(阶跃输入信号)模块拖入模型窗口。由于 Simulink 缺省的阶跃输入模块的跳跃时间是在 1s，而经常使用的是在 0 时刻，完成这一步骤需要双击该模块图标，在如图 B-32 所示对话框的 Step time(阶跃时刻)编辑框中输入 0。当然用户还可以修改 Initial value(初始值)和 Final value(终止值)引导的编辑框来重新定义阶跃信号。

⑤ 确定仿真输出方式。输出模块是在 Sinks(输出方式)子模型库中给出的。从中选择 Scope(示波器)模块，将其拖到模型窗口即可，用户还可以根据自己的需要设定横、纵坐标的范围。

![](image/0c9b9b6540fa0c8c67daf7bc13158f5c2c094e05b29216fddb36fd9338301a9a.jpg)

<details>
<summary>text_image</summary>

Block Parameters: Sum
Sum
Add or subtract inputs. Specify one of the following:
a) string containing + or - for each input port, | for
spacer between ports (e.g. ++|-|++)
b) scalar >= 1. A value > 1 sums all inputs; 1 sums
elements of a single input vector
Parameters
Icon shape: round
List of signs:
|+-
Show additional parameters
OK    Cancel    Help    Apply
</details>

图 B-31 综合模块对话框

![](image/a79988cba7673ed80a53a06856b803b7131889cc0512b570991116ba18ecdb17.jpg)

<details>
<summary>text_image</summary>

Block Parameters: Step
Step
Output a step.
Parameters
Step time:
0
Initial value:
0
Final value:
1
Sample time:
0
Interpret vector parameters as 1-D
Enable zero crossing detection
OK	Cancel	Help	Apply
</details>

图 B-32 阶跃输入对话框
