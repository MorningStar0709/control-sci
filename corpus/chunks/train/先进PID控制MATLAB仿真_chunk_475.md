# 11.1.2 伺服系统的 LuGre 摩擦模型

LuGre 摩擦模型可描述如下。

对于伺服系统，用下面的微分方程表示：

$$J \ddot {\theta} = u - F \tag {11.1}$$

式中，J 为转动惯量； $\theta$ 为转角；u 为控制力矩；F 为摩擦力矩。设状态变量 z 代表接触面鬃毛的平均变形（bristle deform），则 F 可由下面的 LuGre 模型来描述：

$$F = \sigma_ {0} z + \sigma_ {1} \dot {z} + \alpha \dot {\theta} \tag {11.2}\dot {z} = \dot {\theta} - \frac {\sigma_ {0} | \dot {\theta} |}{g (\dot {\theta})} z \tag {11.3}g (\dot {\theta}) = F _ {\mathrm{c}} + (F _ {\mathrm{s}} - F _ {\mathrm{c}}) \mathrm{e} ^ {- \left(\frac {\dot {\theta}}{V _ {\mathrm{s}}}\right) ^ {2}} + \alpha \dot {\theta} \tag {11.4}$$

在式（11.2）～式（11.4）中， $\sigma_{0}$ 、 $\sigma_{1}$ 为动态摩擦参数； $F_{c}$ 、 $F_{s}$ 、 $\alpha$ 、 $V_{s}$ 为静态摩擦参数，其中 $F_{c}$ 为库仑摩擦， $F_{s}$ 为静摩擦， $\alpha$ 为黏性摩擦系数， $V_{s}$ 为切换速度。

![](image/e836448aa2b41304e05b388500b992fdd106f570ed0f8744e6065d37881dabbf.jpg)
