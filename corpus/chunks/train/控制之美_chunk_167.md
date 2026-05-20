# 9.3 一阶系统的频率响应

如图 9.3.1(a) 所示, 一阶系统的传递函数为 $G(s)=\frac{a}{s+a}$ , 其中, a>0 时系统稳定。

![](image/797108e70691a950e72ecebfe5f6716f40918a715171bff2aeb49df88802736b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["U(s)"] --> B["G(s)=a/(s+a)"]
    B --> C["X(s)"]
```
</details>

(a) 一阶系统框图

![](image/7d42e2e7516dae1fbf89c6652822749c06e77a5fb77e7b71ac034f166c6c2402.jpg)

<details>
<summary>text_image</summary>

Im
O
a²/ω₁²+a²
Re
-aωᵢ/ω₁²+a²
G(jωᵢ)
</details>

(b)一阶系统 $G(\mathbf{j}\omega_{\mathrm{i}})$ 的复平面表达  
图 9.3.1 一阶系统框图和其 $G(j\omega_{1})$ 的复平面表达

为分析其频率响应,先计算 $G(j\omega_{i})$ , 得到

$$
G (\mathrm{j} \omega_ {\mathrm{i}}) = \frac {a}{\mathrm{j} \omega_ {\mathrm{i}} + a} = \frac {a (a - \mathrm{j} \omega_ {\mathrm{i}})}{(\mathrm{j} \omega_ {\mathrm{i}} + a) (a - \mathrm{j} \omega_ {\mathrm{i}})} = \frac {a ^ {2} - a \mathrm{j} \omega_ {\mathrm{i}}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}} = \frac {a ^ {2}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}} - \frac {a \omega_ {\mathrm{i}}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}} \mathrm{j} \tag {9.3.1}
$$

在式(9.3.1)中， $G(j\omega_{i})$ 的实部部分为 $\frac{a^{2}}{\omega_{i}^{2}+a^{2}}$ ，虚部部分为 $-\frac{a\omega_{i}}{\omega_{i}^{2}+a^{2}}$ 。其在复平面中的表达如图 9.3.1(b) 所示。根据三角几何关系，可得

$$
\mid G (\mathrm{j} \omega_ {\mathrm{i}}) \mid = \sqrt {\left(\frac {a ^ {2}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}}\right) ^ {2} + \left(- \frac {a \omega_ {\mathrm{i}}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}}\right) ^ {2}} = \sqrt {\frac {a ^ {2}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}}} = \sqrt {\frac {1}{\left(\frac {\omega_ {\mathrm{i}}}{a}\right) ^ {2} + 1}} \tag {9.3.2a}
$$

$$
\angle G (\mathrm{j} \omega_ {\mathrm{i}}) = \arctan \frac {- \frac {a \omega_ {\mathrm{i}}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}}}{\frac {a ^ {2}}{\omega_ {\mathrm{i}} ^ {2} + a ^ {2}}} = - \arctan \frac {\omega_ {\mathrm{i}}}{a} \tag {9.3.2b}
$$

分析式(9.3.2a)，可得：
