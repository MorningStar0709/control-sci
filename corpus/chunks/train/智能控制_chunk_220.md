# 7. 仿真实例

采用 Matlab6.5 中模糊控制工具箱可设计洗衣机模糊控制系统。洗衣机模糊控制系统仿真程序见附录程序 chap4\_6.m。

取 x = 60, y = 70，反模糊化采用重心法，模糊推理结果为 24.9。利用命令 showrule 可观察规则库，利用命令 ruleview 可实现模糊控制的动态仿真，动态仿真环境如图 4-19 所示。

![](image/3dd96b53146b78a298679d80ed7c4499dd28f0f97b68ee8e37b45e4ae584a787.jpg)

<details>
<summary>text_image</summary>

Rule Viewer: wash
File Edit View Options
x = 60 y = 70 z = 33.7
1
2
3
4
5
6
7
8
9
0 100 0 100 0 60
Input: 160 701 Plot 101 Move: left right down up
Opening FIS Editor for new Sugeno system Help Close
</details>

图 4-19 动态仿真模糊系统
