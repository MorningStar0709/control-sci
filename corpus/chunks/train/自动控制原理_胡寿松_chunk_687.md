$$
\det (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) = \det (s \boldsymbol {I} - \overline {{{\boldsymbol {A}}}} + \overline {{{\boldsymbol {B K}}}})
\begin{array}{l} = \det \left[ \begin{array}{c c} s I - \bar {A} _ {c} + \bar {B} _ {c} \bar {K} _ {1} & - \bar {A} _ {1 2} + \bar {B} _ {c} \bar {K} _ {2} \\ 0 & s I - \bar {A} _ {c} \end{array} \right] \\ = \det (s I - \overline {{A}} _ {c} + \overline {{B}} _ {o} \overline {{K}} _ {1}) \det (s I - \overline {{A}} _ {c}) \tag {9-226} \\ \end{array}
$$

由于 $\{\overline{A}_c, \overline{B}_c\}$ 为可控子系统，故必存在 $\overline{K}_1$ 使 $(\overline{A}_c - \overline{B}_c \overline{K}_1)$ 的特征值均具有负实部。又因为状态反馈对不可控子系统的极点毫无影响，从而可知欲使 $(A - BK)$ 的特征值均具有负实部，只有使不可控部分 $\overline{A}_c$ 的特征值均具有负实部。这表明系统由状态反馈可镇定的充分必要条件是不可控部分渐近稳定。证毕。
