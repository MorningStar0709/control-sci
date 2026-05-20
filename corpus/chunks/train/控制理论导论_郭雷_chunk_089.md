$$
\begin{array}{l} \boldsymbol {a} _ {0} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {B} _ {c} = \boldsymbol {e} _ {\nu_ {0} - 2} ^ {\mathrm{T}} + \theta_ {\nu_ {0} - 2} \boldsymbol {e} ^ {\mathrm{T}}, \\ \boldsymbol {a} _ {\mathbf {1}} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \boldsymbol {B} _ {c} = e _ {\nu_ {0} - 3} ^ {\mathrm{T}} + \theta_ {\nu_ {0} - 3} \boldsymbol {e} ^ {\mathrm{T}} + \theta_ {\nu_ {0} - 2} \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {B} _ {c}, \\ \boldsymbol {a} _ {2} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {2} \boldsymbol {B} _ {c} = \boldsymbol {e} _ {\nu_ {0} - 4} ^ {\mathrm{T}} + \theta_ {\nu_ {0} - 4} \boldsymbol {e} ^ {\mathrm{T}} + \theta_ {\nu_ {0} - 3} \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {B} _ {c} + \theta_ {\nu_ {0} - 2} \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \boldsymbol {B} _ {c}, \tag {1.6.31} \\ \boldsymbol {a} _ {\nu_ {0} - 2} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \boldsymbol {B} _ {c} = e _ {0} ^ {\mathrm{T}} + \theta_ {0} e ^ {\mathrm{T}} + \theta_ {1} h ^ {\mathrm{T}} \boldsymbol {B} _ {c} + \dots + \theta_ {\nu_ {0} - 2} h ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 3} \boldsymbol {B} _ {c}. \\ \end{array}
$$

•
•
•

由于矩阵

$$
\left[ \begin{array}{c} \boldsymbol {h} ^ {\mathrm{T}} \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \\ \vdots \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \end{array} \right]
$$

是非奇异的，因此，可以从式(1.6.31)解出

$$
\boldsymbol {B} _ {c} = \left[ \begin{array}{c} \boldsymbol {h} ^ {\mathrm{T}} \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \\ \vdots \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} a _ {0} \\ a _ {1} \\ \vdots \\ a _ {\nu_ {0} - 2} \end{array} \right], \tag {1.6.32}
$$

然后再从等式 (1.6.23) 和式 (1.6.24) 得出递推公式
