# THEOREM 3.1

The optimal value of the PI (3.2.2) is given by

$$J ^ {*} (\mathbf {x} ^ {*} (t), t) = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t). \tag {3.2.24}$$

Proof: First let us note that

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} \frac {d}{d t} \left(\mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t)\right) d t = - \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {0}) \mathbf {P} (t _ {0}) \mathbf {x} ^ {*} (t _ {0}) \\ + \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {f}) \mathbf {P} (t _ {f}) \mathbf {x} ^ {*} (t _ {f}). \tag {3.2.25} \\ \end{array}
$$

Substituting for $\frac{1}{2}\mathbf{x}^{*\prime}(t_f)\mathbf{P}(t_f)\mathbf{x}^*(t_f)$ from (3.2.25) into the PI (3.2.2), and noting that $\mathbf{P}(t_f) = \mathbf{F}(t_f)$ from (3.2.19) we get

$$
\begin{array}{l} J ^ {*} (\mathbf {x} ^ {*} (t _ {0}), t _ {0}) = \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {0}) \mathbf {P} (t _ {0}) \mathbf {x} ^ {*} (t _ {0}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {* \prime} (t) \mathbf {Q} (t) \mathbf {x} ^ {*} (t) + \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) \right. \\ \left. + \frac {d}{d t} \left(\mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t)\right) \right] d t \\ = \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {0}) \mathbf {P} (t _ {0}) \mathbf {x} (t _ {0}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {* \prime} (t) \mathbf {Q} (t) \mathbf {x} ^ {*} (t) + \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) \right. \\ + \dot {\mathbf {x}} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) + \mathbf {x} ^ {* \prime} (t) \dot {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) \\ \left. + \mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \dot {\mathbf {x}} ^ {*} (t) \right] d t. \tag {3.2.26} \\ \end{array}
$$

Now, using the state equation (3.2.14) for $\dot{\mathbf{x}}^*(t)$ , we get

$$
\begin{array}{l} J ^ {*} (\mathbf {x} ^ {*} (t _ {0}), t _ {0}) = \frac {1}{2} \mathbf {x} ^ {* \prime} (t _ {0}) \mathbf {P} (t _ {0}) \mathbf {x} ^ {*} (t _ {0}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \mathbf {x} ^ {* \prime} (t) [ \mathbf {Q} (t) + \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {P} (t) \mathbf {A} (t) \\ \left. - \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) + \dot {\mathbf {P}} (t) \right] \mathbf {x} ^ {*} (t) d t. \tag {3.2.27} \\ \end{array}
$$
