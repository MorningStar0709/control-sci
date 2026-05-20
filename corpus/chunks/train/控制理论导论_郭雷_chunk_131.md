$$\boldsymbol {E} \boldsymbol {L} = \lim _ {s \rightarrow \infty} \left[ \boldsymbol {E} + \boldsymbol {F} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} \right]\left[ \boldsymbol {I} - \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} \right] \boldsymbol {L}$$

亦为对角阵，并且 $EL$ 的对角线上各元素非零。事实上，由于 $L$ 非奇异，若 $EL$ 对角线的第 $i$ 个元为零，则由 $E = (EL)L^{-1}$ 知 $E$ 的第 $i$ 行为零。此与 $E$ 的定义矛盾。所以 $EL$ ，进而 $E$ 非奇异。

充分性. 设 $\pmb{E}$ 非奇异, 取

$$\boldsymbol {K} = \boldsymbol {E} ^ {- 1} \boldsymbol {F}, \quad \boldsymbol {L} = \boldsymbol {E} ^ {- 1}. \tag {1.9.6}$$

由引理1.9.1知，相应闭环系统的传递函数 $G_{KL}(s)$ 为

$$
\begin{array}{l} \boldsymbol {G} _ {K L} (s) = \boldsymbol {G} (s) [ \boldsymbol {I} + \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} ] ^ {- 1} \boldsymbol {L} \\ = G (s) \left[ L ^ {- 1} + L ^ {- 1} K (s I - A) ^ {- 1} B \right] ^ {- 1} \\ = G (s) \left[ E + F (s I - A) ^ {- 1} B \right] ^ {- 1}. \\ \end{array}
$$

将式 (1.9.5) 代入上式即得

$$\boldsymbol {G} (s) = \operatorname{diag} \left(\frac {1}{s ^ {d _ {1} + 1}}, \dots , \frac {1}{s ^ {d _ {m} + 1}}\right). \tag {1.9.7}$$

这说明能对系统 (1.9.1) 实现解耦控制.

根据定理 1.9.1, 受控系统 (1.9.1) 可否采用形如式 (1.9.2) 的状态反馈和非奇异输入变换实现解耦控制, 关键在于矩阵 E 的非奇异性, 而与系统的能控性、能镇定性或能观测性无关. 但是, 从解耦后的系统要能正常地运行并具有良好的动态性能而言, 仍需要求受控系统是能控的, 或至少是能镇定的. 否则, 甚至不能保证闭环系统的稳定性, 此时解耦也就失去了实际意义.

通过定理1.9.1的充分性证明部分，可以看出如果选取形如式(1.9.6)所示的状态反馈阵 $K$ 和非奇异输入变换 $\pmb{L}$ ，则闭环控制系统可以实现解耦，且有形如(1.9.7)的传递函数。此时，由于解耦后每个单输入单输出闭环控制系统的传递函数均具有多重积分器的特性，因此通常称这类形式的解耦为积分型解耦。积分型解耦系统虽然因其不能令人满意的动态性能，本身没有多少实际应用价值，但它常常是综合具有满意性能的解耦控制的一个中间性步骤，因而仍有研究的价值。事实上，可以做到在实现闭环解耦的同时任意配置极点。方法也多种多样，例如，可以采用附加反馈法，在积分解耦的基础上为各个子系统配置极点 $^{[7,9,17]}$ ；也可以根据所配极点，适当选取式(1.9.5)中的F，进而利用式(1.9.6)给出状态反馈阵K和非奇异输入变换L，直接完成输入输出解耦和极点配置两项任务。

定理 1.9.2 设在采用形如式 (1.9.2) 的态反馈加非奇异输入变换控制，使系统 (1.9.1) 输入输出解耦，则可选

$$\boldsymbol {K} = \boldsymbol {E} ^ {- 1} \boldsymbol {F}, \quad \boldsymbol {L} = \boldsymbol {E} ^ {- 1}, \tag {1.9.8}$$

使得闭环系统传递函数阵为

$$\boldsymbol {G} _ {K L} (s) = \operatorname{diag} \left(\frac {1}{\Delta_ {1} (s)}, \dots , \frac {1}{\Delta_ {m} (s)}\right),$$

其中 $\Delta_{i}(s)=s^{d_{i}+1}+\alpha_{i1}s^{d_{i}}+\cdots+\alpha_{i(d_{i}+1)},\alpha_{jk}(j=1,\cdots,m;k=1,\cdots,d_{m}+1)$ 为实数，可按配置所希望极点的要求任意选择，F 为由下式定义的 $m\times n$ 阵：
