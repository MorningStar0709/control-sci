I=A⁰
A × × × 0
A² × 0
A³ 0
A⁴
A⁵
A⁶
</details>

图3.4 列搜索方案的格栅图(图中， $l = 3, \nu_{1} = 3, \nu_{2} = 2, \nu_{3} = 1$ )

![](image/8a4c691b1d0c60193290cc57180676b8827616e2112b94db8aa8f64f098cee8e.jpg)

<details>
<summary>text_image</summary>

I=A⁰
A
A²
A³
A⁴
A⁵
A⁶
b₁ b₂ b₃ b₄
× × × ○
× ○ ×
×
○
○
○
○
○
○
○
○
○
○
○
</details>

图3.5 行搜索方案的格栅图(图中， $r = 3, \mu_1 = 3, \mu_2 = 1, \mu_3 = 2$ )

以上的讨论是针对能控性矩阵 $Q_{e}$ 进行的。对于能观测矩阵 $Q_{o}$ ，搜索其 n 个线性无关的行的方案和步骤与上述相类似，故在这里不再重复。

旺纳姆规范形 考虑多输入-多输出的线性定常系统(3.178)，来分别介绍由旺纳姆(W. M. Wonham)所提出的能控规范形和能观测规范形。

先讨论旺纳姆能控规范形。给定系统的状态空间描述（3.178），且知系统为完全能控，再表 $B = [b_{1}, b_{2}, \cdots, b_{p}]$ ，并按照上面指出的搜索方案 I 或 II 来找出能控性矩阵

$$Q _ {c} = \left[ \boldsymbol {b} _ {1}, \boldsymbol {b} _ {2}, \dots , \boldsymbol {b} _ {p} \mid A \boldsymbol {b} _ {1}, A \boldsymbol {b} _ {2}, \dots , A \boldsymbol {b} _ {p} \mid \dots \mid A ^ {n - 1} \boldsymbol {b} _ {1}, A ^ {n - 1} \boldsymbol {b} _ {2}, \dots , A ^ {n - 1} \boldsymbol {b} _ {p} \right] \tag {3.181}$$

中的 $n$ 个线性无关的列向量。假设按方案I进行搜索，得到 $n$ 个线性无关的向量为

$$\boldsymbol {b} _ {1}, A \boldsymbol {b} _ {1}, \dots , A ^ {\nu_ {1} - 1} \boldsymbol {b} _ {1}; \boldsymbol {b} _ {2}, A \boldsymbol {b} _ {2}, \dots , A ^ {\nu_ {2} - 1} \boldsymbol {b} _ {2}; \dots ; \boldsymbol {b} _ {l}, A \boldsymbol {b} _ {l}, \dots , A ^ {\nu_ {l} - 1} \boldsymbol {b} _ {l} \tag {3.182}$$

其中 $v_{1} + v_{2} + \cdots + v_{l} = n$ 。再知， $A^{v_{1}}b_{1}$ 可表为 $\{b_{1}, Ab_{1}, \cdots, A^{v_{1}-1}b_{1}\}$ 的线性组合， $A^{v_{2}}b_{2}$ 可表为 $\{b_{1}, Ab_{1}, \cdots, A^{v_{1}-1}b_{1}; b_{2}, Ab_{2}, \cdots, A^{v_{2}-1}b_{2}\}$ 的线性组合，如此等等。最后， $A^{v_{l}}b_{l}$ 则可表为 (3.182) 的向量组的线性组合。于是，就进一步可导出：
