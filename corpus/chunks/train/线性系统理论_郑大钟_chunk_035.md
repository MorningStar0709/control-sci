我们转而讨论离散动态过程的状态空间描述。离散时间动态过程的一个基本特点是，系统的各个变量都被处理成为只在离散的时刻取值，其状态空间描述只反映离散时刻的变量组间的因果关系和转换关系。用 $k = 0, 1, 2, \cdots$ 来表示离散的时刻，那么离散时间系统的状态方程和输出方程的最一般的形式为：

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = \boldsymbol {f} (\boldsymbol {x} (k), \boldsymbol {u} (k), k), \quad k = 0, 1, 2, \dots \\ \boldsymbol {y} (k) = \boldsymbol {g} (\boldsymbol {x} (k), \boldsymbol {u} (k), k) \end{array} \right. \tag {1.17}
$$

对于线性的离散时间系统,则上述状态方程和输出方程还可进而化为如下的形式:

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = G (k) \boldsymbol {x} (k) + H (k) \boldsymbol {u} (k), \quad k = 0, 1, 2, \dots \\ \boldsymbol {y} (k) = C (k) \boldsymbol {x} (k) + D (k) \boldsymbol {u} (k) \end{array} \right. \tag {1.18}
$$

通常,可以采用两条可能的途径来组成系统的状态空间描述。一是分析的途径,适用于结构和参数为已知的系统。它先直接运用相应的物理原理组成系统的动力学方程,然后通过选取合适的状态变量组,进一步把系统原始方程化为上述形式的状态方程和输出方程。另一是辨识的途径,适用于结构和参数难于搞清楚的系统。它通过实验手段取得数据并采用适当方法确定系统的输入-输出模型,然后再由所得到的系统输入-输出描述来导出相应的状态空间描述。这里,前一个步骤称为系统辨识和参数估计,其内容已超出了本书的范围。后一个步骤称为实现问题,在后几节中将就单输入-单输出的情况来讨论这一问题,而有关实现问题的更一般和更完整的论述将在第9章中给出。

系统状态空间描述的列写举例 下面，就一些简单的系统讨论其状态空间描述的组成问题，意在阐明列写系统的状态方程和输出方程的一般步骤。

例1 考察图1.3所示的简单电路，电路各组成元件的参数值为已知，输入变量取为电压源 $e(t)$ ，输出变量取为电阻 $R_{2}$ 的端电压 $u_{R20}$ 。

![](image/3a6de5007403192ee6adbab1381f7c36b68d42b87a5d6ace3bdbf6e96029b555.jpg)

<details>
<summary>text_image</summary>

R₁
C
+
u_c
i_c
L
i_L
R₂
u_{R₂}
+
e(t)
-
</details>

图1.3 一个简单电路

确定状态变量：根据电路理论可知，此电路最多有2个线性无关的变量；因此，可选取独立储能元件的变量，即电容端电压 $u_{c}$ 和流经电感的电流 $i_{L}$ ，作为电路的状态变量。

列出原始电路方程：运用电路定律，对图中两个回路分别列出电路方程为：

右回路 $u_{c} + R_{2}i_{c} = L\frac{di_{L}}{dt}$

左回路 $R_{1}(i_{L} + i_{c}) + L\frac{di_{L}}{dt} = e(t)$

考虑到规定 $u_{c}$ 和 $i_L$ 为状态变量，并有 $i_c = Cdu_c / dt$ ，所以将上述方程组进而改写为只包

含未知变量 $u_{c}$ 和 $i_{L}$ 的方程组：

$$R _ {2} G \frac {d u _ {c}}{d t} - L \frac {d i _ {L}}{d t} = - u _ {c}R _ {1} C \frac {d u _ {e}}{d t} + L \frac {d i _ {L}}{d t} = - R _ {1} i _ {L} + e (t)$$

导出状态方程：首先，以 $du_{c}/dt$ 和 $di_{L}/dt$ 为待定变量求解上述联立方程，得到：

$$\frac {d u _ {c}}{d t} = - \frac {1}{\left(R _ {1} + R _ {2}\right) C} u _ {c} - \frac {R _ {1}}{\left(R _ {1} + R _ {2}\right) C} i _ {L} + \frac {1}{\left(R _ {1} + R _ {2}\right) C} e (t)\frac {d i _ {L}}{d t} = \frac {R _ {1}}{L \left(R _ {1} + R _ {2}\right)} u _ {\bullet} - \frac {R _ {1} R _ {2}}{L \left(R _ {1} + R _ {2}\right)} i _ {L} + \frac {R _ {2}}{L \left(R _ {1} + R _ {2}\right)} e (t)$$

进而,将其表为向量方程的形式,就导出了此电路的状态方程为:
