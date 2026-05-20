（1） $k_{p}$ 整定原则：当响应在上升过程时（e 为 P）， $\Delta k_{p}$ 取正，即增大 $k_{p}$ ；当超调时（e 为 N）， $\Delta k_{p}$ 取负，即降低 $k_{p}$ 。当误差在零附近时（e 为 Z），分三种情况：ec 为 N 时，超调越来越大，此时 $\Delta k_{p}$ 取负；ec 为 Z 时，为了降低误差， $\Delta k_{p}$ 取正；ec 为 P 时，正向误差越来越大， $\Delta k_{p}$ 取正。 $k_{p}$ 整定的模糊规则表见表 8-3。  
（2） $k_{i}$ 整定原则：采用积分分离策略，即误差在零附近时， $\Delta k_{i}$ 取正，否则 $\Delta k_{i}$ 取零。 $k_{i}$ 整定的模糊规则表见表 8-4。

表 8-3 $k_{\mathrm{p}}$ 的模糊规则表

<table><tr><td> $\begin{array}{c} \Delta kp \\ e \end{array}$ </td><td>ec</td><td>N</td><td>Z</td><td>P</td></tr><tr><td>N</td><td></td><td>N</td><td>N</td><td>N</td></tr><tr><td>Z</td><td></td><td>N</td><td>P</td><td>P</td></tr><tr><td>P</td><td></td><td>P</td><td>P</td><td>P</td></tr></table>

表 8-4 $k_{i}$ 的模糊规则表

<table><tr><td> $\Delta {k}_{\mathrm{i}}$ e\ec</td><td>N</td><td>Z</td><td>P</td></tr><tr><td>N</td><td>Z</td><td>Z</td><td>Z</td></tr><tr><td>Z</td><td>P</td><td>P</td><td>P</td></tr><tr><td>P</td><td>Z</td><td>Z</td><td>Z</td></tr></table>

将系统误差 e 和误差变化率 ec 变化范围定义为模糊集上的论域。

$$e, \mathrm{ec} = \{- 1, 0, 1 \} \tag {8.28}$$

其模糊子集为 $e, ec = \{N, O, P\}$ ，子集中元素分别代表负、零、正。设 e、ec 和 $k_{p}$ 、 $k_{i}$ 均服从正态分布，因此可得出各模糊子集的隶属度，根据各模糊子集的隶属度赋值表和各参数模糊控制模型，应用模糊合成推理设计 PI 参数的模糊矩阵表，查出修正参数代入下式计算。

$$k _ {\mathrm{p}} = k _ {\mathrm{p0}} + \Delta k _ {\mathrm{p}}, \quad k _ {\mathrm{i}} = k _ {\mathrm{i0}} + \Delta k _ {\mathrm{i}} \tag {8.29}$$

在线运行过程中，控制系统通过对模糊逻辑规则的结果处理、查表和运算，完成对 PID 参数的在线自校正。其工作流程图如图 8-10 所示。

![](image/f98eeea6505d23fe038d3c8e97adfd5fdc00716eae6214ec4b5bcdb832a72a00.jpg)
