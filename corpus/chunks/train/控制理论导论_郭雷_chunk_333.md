$$
\begin{array}{l} R _ {y _ {k + 1} \mid y ^ {k}} = E (y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}) (y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}) ^ {*} \\ = E \left[ C _ {k + 1} \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) + F _ {k + 1} w _ {k + 1} \right] \left[ C _ {k + 1} \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) + F _ {k + 1} w _ {k + 1} \right] ^ {*} \\ = E \left[ C _ {k + 1} \left(\Phi_ {k + 1, k} \left(x _ {k} - \hat {x} _ {k}\right) + D _ {k + 1} w _ {k + 1}\right) + F _ {k + 1} w _ {k + 1} \right] \\ \cdot \left[ C _ {k + 1} \left(\Phi_ {k + 1, k} \left(x _ {k} - \hat {x} _ {k}\right) + D _ {k + 1} w _ {k + 1}\right) + F _ {k + 1} w _ {k + 1} \right] ^ {*} \\ = C _ {k + 1} P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {*} + C _ {k + 1} D _ {k + 1} F _ {k + 1} ^ {*} + \dot {F} _ {k + 1} D _ {k + 1} ^ {*} D _ {k + 1} ^ {*} + F _ {k + 1} F _ {k + 1} ^ {*} \tag {4.4.21} \\ \end{array}
$$

把式 (4.4.20), 式 (4.4.21) 和式 (4.4.17) 比较后, 便知为了得到式 (4.4.17), 还要证明

$$
R _ {x _ {k + 1}, y _ {k + 1} | y _ {k}} = P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {*} + D _ {k + 1} F _ {k + 1} ^ {*}.
\begin{array}{l} \text { 上   式   左   端 } = E \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) \left(y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}\right) \\ = E \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) \left(C _ {k + 1} \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) + F _ {k + 1} w _ {k + 1}\right) ^ {*} \\ = P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {*} + E \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) w _ {k + 1} ^ {*} F _ {k + 1} ^ {*} \\ = P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {*} + E \left(\phi_ {k + 1, k} \left(x _ {k} - \hat {x} _ {k}\right) + D _ {k + 1} w _ {k + 1}\right) w _ {k + 1} ^ {*} F _ {k + 1} ^ {*} \\ = P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {*} + D _ {k + 1} F _ {k + 1} ^ {*}. \\ \end{array}
$$

这样我们证明了式 (4.4.15)\~(4.4.17) 及式 (4.4.19), 还要验证式 (4.4.18).

从式 (4.4.15) 知

$$x _ {k + 1} - \hat {x} _ {k + 1} = x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime} - K _ {k + 1} (y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}). \tag {4.4.22}$$

注意到

$$
\begin{array}{l} K _ {k + 1} E \left(y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}\right) \left(y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}\right) K _ {k + 1} ^ {*} \\ = K _ {k + 1} \left(C _ {k + 1} P _ {k + 1} ^ {\prime} + F _ {k + 1} D _ {k + 1} ^ {*}\right) = E \left(x _ {k + 1} - \hat {x} _ {k + 1} ^ {\prime}\right) \left(y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}\right) K _ {k + 1} ^ {*}, \\ \end{array}
$$

取式 (4.4.22) 两端的协方差阵，便得式 (4.4.18).
