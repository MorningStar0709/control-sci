$$
u = - \left[ K _ {\mathrm{a}} \quad \mathbf {K} _ {\mathrm{b}} \right] \left[ \begin{array}{l} x _ {\mathrm{a}} \\ \hat {\mathbf {x}} _ {\mathrm{b}} \end{array} \right] = - K _ {\mathrm{a}} y - \mathbf {K} _ {\mathrm{b}} \hat {\mathbf {x}} _ {\mathrm{b}} \tag {7.175}
$$

将式(7.175)代入式(7.171)，然后使用式(7.158)及一些代数方法，得到

$$\dot {\boldsymbol {x}} _ {\mathrm{c}} = \boldsymbol {A} _ {\mathrm{r}} \boldsymbol {x} _ {\mathrm{c}} + \boldsymbol {B} _ {\mathrm{r}} y \tag {7.176a}u = C _ {\mathrm{r}} x _ {\mathrm{c}} + D _ {\mathrm{r}} y \tag {7.176b}$$

其中：

$$\mathbf {A} _ {\mathrm{r}} = \mathbf {A} _ {\mathrm{bb}} - \mathbf {L A} _ {\mathrm{ab}} - \left(\mathbf {B} _ {\mathrm{b}} - \mathbf {L B} _ {\mathrm{a}}\right) \mathbf {K} _ {\mathrm{b}} \tag {7.177a}\boldsymbol {B} _ {\mathrm{r}} = \boldsymbol {A} _ {\mathrm{r}} \boldsymbol {L} + \boldsymbol {A} _ {\mathrm{ba}} - \boldsymbol {L A} _ {\mathrm{aa}} - \left(\boldsymbol {B} _ {\mathrm{b}} - \boldsymbol {L B} _ {\mathrm{a}}\right) K _ {\mathrm{a}} \tag {7.177b}\mathbf {C} _ {\mathrm{r}} = - \mathbf {K} _ {\mathrm{b}} \tag {7.177c}D _ {\mathrm{r}} = - K _ {\mathrm{a}} - \mathbf {K} _ {\mathrm{b}} \mathbf {L} \tag {7.177d}$$

该动态补偿器具有传递函数为

$$D _ {\mathrm{cr}} (s) = \frac {U (s)}{Y (s)} = C _ {\mathrm{r}} \left(s I - A _ {\mathrm{r}}\right) ^ {- 1} B _ {\mathrm{r}} + D _ {\mathrm{r}} \tag {7.178}$$

当我们针对一个具体例子计算出 $D_{\mathrm{c}}(s)$ 或 $D_{\mathrm{cr}}(s)$ 时，会发现虽然使用的是与第 5 章和第 6 章所提出的经典补偿器完全不同的方法，但相应结果却非常类似。
