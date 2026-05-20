与 $t_{f}$ 固定时的情况不同，现在 $\delta J_{a}$ 由 $\delta U, \delta X, \delta X(t_{f})$ 和 $\delta t_{f}$ 所引起。这里 $\delta t_{f}$ 不再为 0，而 $\delta X(t_{f})$ 可计算如下（参见图 3-3）：

![](image/dc84bc20fc9773e181704a4a0d78e99dfa05283f866c96eb5c85185b20d8c644.jpg)  
图3-3 各种变分的表示

令 $t_{\mathrm{f}} = t_{\mathrm{f}}^{*} + \delta t_{\mathrm{f}}$

$$
\begin{array}{l} \delta \boldsymbol {X} \left(t _ {\mathrm{f}}\right) = \boldsymbol {X} \left(t _ {\mathrm{f}}\right) - \boldsymbol {X} ^ {*} \left(t _ {\mathrm{f}} ^ {*}\right) = \boldsymbol {X} \left(t _ {\mathrm{f}} ^ {*} + \delta t _ {\mathrm{f}}\right) + \delta \boldsymbol {X} \left(t _ {\mathrm{f}} ^ {*}\right) - \boldsymbol {X} \left(t _ {\mathrm{f}} ^ {*}\right) \\ \approx \delta X (t _ {\mathrm{f}} ^ {*}) + \dot {X} (t _ {\mathrm{f}} ^ {*}) \delta t _ {\mathrm{f}} \tag {3-52} \\ \end{array}
$$

注意,这里 $\delta X(t_{\mathrm{f}})$ 和 $\delta X(t_{\mathrm{f}}^{*})$ 不同,故 \* 号不能省去。上式表明 $\delta X(t_{\mathrm{f}})$ 由两部分组成:一是在 $t_{f}^{*}$ 时函数 $X(t_{\mathrm{f}})$ 相对 $X^{*}(t_{\mathrm{f}})$ 的变化 $\delta X(t_{\mathrm{f}}^{*})$ ,另一是因 $t_{f}$ 的变化所引起的函数值的变化量 $\left[X(t_{\mathrm{f}}^{*}+\delta t_{\mathrm{f}})-X(t_{\mathrm{f}}^{*})\right]$ 。后者可用

它的线性主部 $\dot{X}(t_{\mathrm{f}}^{*})\delta t_{\mathrm{f}}$ 来近似。

现在来计算 $\delta J_{a}$ （只计算到一阶小量）。

$$
\begin{array}{l} \Delta J _ {\mathrm{a}} = \theta [ X (t _ {\mathrm{f}}) + \delta X (t _ {\mathrm{f}}), t _ {\mathrm{f}} + \delta t _ {\mathrm{f}} ] * + \\ \int_ {t _ {0}} ^ {t _ {\mathrm{f}} ^ {*} + \delta t _ {\mathrm{f}}} \left[ H (\boldsymbol {X} + \delta \boldsymbol {X}, \boldsymbol {U} + \delta \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (\dot {\boldsymbol {X}} + \delta \dot {\boldsymbol {X}}) \right] _ {*} \mathrm{d} t - \\ \theta \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] - \int_ {t _ {0}} ^ {t _ {\mathrm{f}} ^ {*}} \left[ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {X}} \right] \mathrm{d} t \\ \end{array}
$$

上式中方括号外的下标 \* 表示 X、U、 $t_{f}$ 是最优值 $X^{*}$ 、 $U^{*}$ 、 $t_{f}^{*}$ 。 $\delta J_{a}$ 是上式的线性主部，故
