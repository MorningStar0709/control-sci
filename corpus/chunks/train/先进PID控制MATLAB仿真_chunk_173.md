# 1. 分析 $K_{\mathrm{p}}$ 的设计

闭环系统可写为

$$G (s) K (s) = \frac {K _ {\mathrm{g}}}{s \left(T _ {\mathrm{g}} s + 1\right)} K _ {\mathrm{p}} \left(1 + \frac {1}{T _ {\mathrm{i}} s}\right) = K _ {\mathrm{g}} K _ {\mathrm{p}} \frac {1}{s} \frac {1}{s} \frac {1}{T _ {\mathrm{i}}} \frac {1}{T _ {\mathrm{g}} s + 1} \left(T _ {\mathrm{i}} s + 1\right)$$

根据典型环节的频率特性可知，积分环节 $\frac{1}{s}$ 的幅频为 $\frac{1}{\omega}$ ，一阶惯性环节 $\frac{1}{T_{\mathrm{g}} s + 1}$ 的幅频为 $\frac{1}{\sqrt{\left(T_{\mathrm{g}} \omega\right)^2 + 1}}$ ，一阶微分环节 $T_{\mathrm{i}} s + 1$ 的幅频为 $\sqrt{\left(T_{\mathrm{i}} \omega\right)^2 + 1}$ ，则闭环系统 $G(s) K(s)$ 的幅频 $A(\omega)$ 为 $K_{\mathrm{g}} K_{\mathrm{p}} \frac{1}{\omega} \frac{1}{\omega} \frac{1}{T_{\mathrm{i}}} \frac{1}{\sqrt{\left(T_{\mathrm{g}} \omega\right)^2 + 1}} \sqrt{\left(T_{\mathrm{i}} \omega\right)^2 + 1}$ 。

由图 2-17 可知，当闭环系统相位裕度为最大时， $\lg A(\omega_{\mathrm{c}})=0$ ，即 $A(\omega_{\mathrm{c}})=1$ ，此时

$$K _ {\mathrm{g}} K _ {\mathrm{p}} \frac {1}{\omega_ {\mathrm{c}}} \frac {1}{\omega_ {\mathrm{c}}} \frac {1}{T _ {\mathrm{i}}} \frac {\sqrt {(T _ {\mathrm{i}} \omega_ {\mathrm{c}}) ^ {2} + 1}}{\sqrt {(T _ {\mathrm{g}} \omega_ {\mathrm{c}}) ^ {2} + 1}} = 1 \tag {2.20}$$

由于

$$\frac {1}{T _ {\mathrm{i}}} \frac {\sqrt {\left(T _ {\mathrm{i}} \omega_ {\mathrm{c}}\right) ^ {2} + 1}}{\sqrt {\left(T _ {\mathrm{g}} \omega_ {\mathrm{c}}\right) ^ {2} + 1}} = \omega_ {\mathrm{i}} \frac {\sqrt {\left(\frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{i}}}\right) ^ {2} + 1}}{\sqrt {\left(\frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{g}}}\right) ^ {2} + 1}} = \omega_ {\mathrm{i}} \frac {\sqrt {\left(\frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{i}}}\right) ^ {2} + 1}}{\sqrt {\left(\frac {\omega_ {\mathrm{i}}}{\omega_ {\mathrm{c}}}\right) ^ {2} + 1}} = \omega_ {\mathrm{i}} \frac {\frac {1}{\omega_ {\mathrm{i}}} \sqrt {\omega_ {\mathrm{c}} ^ {2} + \omega_ {\mathrm{i}} ^ {2}}}{\frac {1}{\omega_ {\mathrm{c}}} \sqrt {\omega_ {\mathrm{i}} ^ {2} + \omega_ {\mathrm{c}} ^ {2}}} = \omega_ {\mathrm{c}}$$

则式（2.20）变为
