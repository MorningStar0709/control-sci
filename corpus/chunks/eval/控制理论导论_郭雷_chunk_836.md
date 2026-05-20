$$
\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) \left[ \begin{array}{c c} t _ {1} (k - 1) & t _ {1} (k - 1) t _ {1} (k) \\ \varepsilon & t _ {2} (k - 1) \end{array} \right] \oplus u (k) [ 0, t _ {1} (k) ], \tag {11.3.5}
$$

而式 (11.3.3) 为

$$
y (k) = \boldsymbol {X} (k) \left[ \begin{array}{c} \varepsilon \\ t _ {2} (k) \end{array} \right]. \tag {11.3.6}
$$

如果每个工件在 $m_{1}$ 上加工的时间都为 $t_{1}$ ，在 $m_{2}$ 上加工的时间都为 $t_{2}$ ，则式(11.3.5)\~(11.3.6)变为

$$
\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) \left[ \begin{array}{l l} t _ {1} & t _ {1} ^ {2} \\ \varepsilon & t _ {2} \end{array} \right] \oplus u (k) [ 0, t _ {1} ], \tag {11.3.7}

y (k) = \boldsymbol {X} (k) \left[ \begin{array}{l} \varepsilon \\ t _ {2} \end{array} \right]. \tag {11.3.8}
$$

对于有多台机器的串行生产线，可以用类似于式(11.3.7)\~(11.3.8)的方程来描述。一般地，一个事件图总可以用如下极大代数方程描述：

$$\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) \boldsymbol {A} \oplus \boldsymbol {u} (k) \boldsymbol {B}, \boldsymbol {y} (k) = \boldsymbol {X} (k) \boldsymbol {C}. \tag {11.3.9}$$

这个模型可简记为 $(A, B, C)$ .

文献[17]提出了一种不经过Petri网，直接用极大代数建模的方法，文献[10]介绍了这种方法，并应用于轧钢厂．限于篇幅，不详述.
