# (8) 模糊运算的基本性质

模糊集合除具有上述基本运算性质外,还具有如表 3-1 所示的运算性质。

表 3-1 模糊运算的基本性质

<table><tr><td>名称</td><td>运算法则</td></tr><tr><td>1.幂等律</td><td> $A \cup A = A, A \cap A = A$ </td></tr><tr><td>2.交换律</td><td> $A \cup B = B \cup A, A \cap B = B \cap A$ </td></tr><tr><td>3.结合律</td><td> $(A \cup B) \cup C = A \cup (B \cup C)$  $(A \cap B) \cap C = A \cap (B \cap C)$ </td></tr><tr><td>4.吸收律</td><td> $A \cup (A \cap B) = A$  $A \cap (A \cup B) = A$ </td></tr><tr><td>5.分配律</td><td> $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$  $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ </td></tr><tr><td>6.复原律</td><td> $\overline{A} = A$ </td></tr><tr><td>7.对偶律</td><td> $\overline{A \cup B} = \overline{A} \cap \overline{B}$  $\overline{A \cap B} = \overline{A} \cup \overline{B}$ </td></tr><tr><td>8.两极律</td><td> $A \cup E = E, A \cap E = A$  $A \cup \varnothing = A, A \cap \varnothing = \varnothing$ </td></tr></table>

【例 3.3】设 $A=\frac{0.9}{u_{1}}+\frac{0.2}{u_{2}}+\frac{0.8}{u_{3}}+\frac{0.5}{u_{4}}$ ， $B=\frac{0.3}{u_{1}}+\frac{0.1}{u_{2}}+\frac{0.4}{u_{3}}+\frac{0.6}{u_{4}}$ ，求 $A\cup B, A\cap B$ 。

解 $A \cup B = \frac{0.9}{u_1} + \frac{0.2}{u_2} + \frac{0.8}{u_3} + \frac{0.6}{u_4}, A \cap B = \frac{0.3}{u_1} + \frac{0.1}{u_2} + \frac{0.4}{u_3} + \frac{0.5}{u_4}$

【例 3.4】试证明普通集合中的互补律在模糊集合中不成立，即 $\mu_{A}(u) \vee \mu_{\overline{A}}(u) \neq 1, \mu_{A}(u) \wedge \mu_{\overline{A}}(u) \neq 0$ 。

证明 设 $\mu_A(u) = 0.4$ ，则 $\mu_{\overline{A}}(u) = 1 - 0.4 = 0.6$ ，则

$$\mu_ {A} (u) \vee \mu_ {\overline {{{A}}}} (u) = 0. 4 \vee 0. 6 = 0. 6 \neq 1\mu_ {A} (u) \wedge \mu_ {\overline {{{A}}}} (u) = 0. 4 \wedge 0. 6 = 0. 4 \neq 0$$
