# 3.4 相平面案例分析——爱情故事

3.3 节详细讨论了使用相轨迹分析状态空间方程平衡点类型的方法。在本节中, 将通过一个案例帮助读者加深对这部分内容的理解, 希望这个有趣的例子可以引起读者的兴趣与思考。另外, 本节将介绍动态系统分析的思路与讨论方法, 这种思路和讨论方法可以作为模板使用在论文写作和学术报告中。动态系统的分析可以分为三个步骤: 第一步描述系统,即通过语言来描述系统的特性;第二步数学分析,即使用数学工具对系统进行量化解析;第三步结果与讨论,即根据第二步数学分析的结果,进行深层次的思考与讨论。

爱情是永恒的主题,每个人都有自己的故事。康奈尔大学应用数学系教授 Steven Strogatz 在 1988 年首先将爱情模型引入相轨迹分析的教学中。他当时在哈佛大学做博士后,根据课堂的经验引入了这一模型。他选用的是莎翁笔下的著名人物——罗密欧与朱丽叶。之后很多教师都纷纷使用这一概念来引起同学们的兴趣,而每一个教师也会在其中加入自己的思考与分析。

为了使本书读者有更好的代入感,我将选用两个中国人的名字,来自于我的两位朋友,男生叫雨飞,女生叫梦寒,如图3.4.1所示。其中,雨飞对梦寒的感情用 $Y(t)$ 来表示,梦寒对雨飞的感情用 $M(t)$ 来表示。 $Y(t)$ 与 $M(t)$ 大于零时说明他们是相爱的,小于零时说明他们心有怨恨,等于零时说明他们对对方无感。

![](image/e7e4c64432f6ec75afe877f20231045c59a242225c901d46798b5b2e4a88153c.jpg)

<details>
<summary>natural_image</summary>

Two stick figures with question marks above their heads, one pointing at a bow tie and the other holding a bow tie (no text or symbols present)
</details>

图 3.4.1 爱情故事：雨飞和梦寒

分以下几种情况进行讨论。

情况(1): $\frac{\mathrm{d}}{\mathrm{d}t}\begin{bmatrix}Y(t)\\M(t)\end{bmatrix}=A\begin{bmatrix}Y(t)\\M(t)\end{bmatrix}$ ，其中 $A=\begin{bmatrix}0&a\\-b&0\end{bmatrix},a>0$ 且 b>0。

第一步：描述系统。

从上式可以看出,雨飞是一个耿直男孩。他的表现是:如果你对我好(M(t)>0),我就会对你产生好感 $\left(\frac{\mathrm{d}Y(t)}{\mathrm{d}t}=aM(t)>0\right)$ ; 如果你讨厌我(M(t)<0),我也不搭理你 $\left(\frac{\mathrm{d}Y(t)}{\mathrm{d}t}=aM(t)<0\right)$ 。他属于“投桃报李”加“以牙还牙”的性格。这种性格过于直来直去,在现实生活中其实不太容易受到欢迎。

而梦寒则是一个多情甚至有些矫情的女孩。当雨飞向他嘘寒问暖时 $(Y(t)>0)$ ，她爱答不理，你越热情，她就越远离 $\left(\frac{\mathrm{d}M(t)}{\mathrm{d}t}=-bY(t)<0\right)$ 。而当雨飞开始疏远她时 $(Y(t)<0)$ ，她又发现了雨飞身上的优点，不可控制地开始爱上他 $\left(\frac{\mathrm{d}M(t)}{\mathrm{d}t}=-bY(t)>0\right)$ 。即“欲迎还

拒”加“若即若离”的性格。当这两种性格遇到一起，就会发生一些奇妙的事情。

第二步：数学分析。

首先求系统的平衡点，令 $\frac{\mathrm{d}}{\mathrm{d}t}\left[\begin{array}{l}Y(t)\\ M(t)\end{array}\right] = 0$ ，得到平衡点 $\left\{ \begin{array}{l}Y_{\mathrm{f}} = 0\\ M_{\mathrm{f}} = 0 \end{array} \right.$

求矩阵 $\mathbf{A}$ 的特征值, 可得 $\lambda_{1,2} = \pm \sqrt{ab} j$ 。根据表3.3.1, 判断出平衡点是一个中心点。它的相轨迹是图3.4.2所示的椭圆(参考例3.3.5)。根据初始状态的不同, 这个椭圆的大小会有所不同。

![](image/a846cf8c882b21a97fe112a170b80d54a02f021d5c845c9d144f8a469bea710e.jpg)

<details>
<summary>text_image</summary>
