$$p _ {k} (\mathbf {A}) = \frac {\left(\mathbf {A} - \lambda_ {1} \mathbf {I}\right) \cdots \left(\mathbf {A} - \lambda_ {k - 1} \mathbf {I}\right) \left(\mathbf {A} - \lambda_ {k + 1} \mathbf {I}\right) \cdots \left(\mathbf {A} - \lambda_ {m} \mathbf {I}\right)}{\left(\lambda_ {k} - \lambda_ {1}\right) \cdots \left(\lambda_ {k} - \lambda_ {k - 1}\right) \left(\lambda_ {k} - \lambda_ {k + 1}\right) \cdots \left(\lambda_ {k} - \lambda_ {m}\right)}$$

Notice that $p _ { k } ( { \bf A } )$ is a polynomial in A of degree $m - 1$ . Notice also that

$$
p _ {k} \big (\lambda_ {i} \mathbf {I} \big) = \left\{ \begin{array}{l l} \mathbf {I}, & \quad \text { if } i = k \\ \mathbf {0}, & \quad \text { if } i \neq k \end{array} \right.
$$

Now define

$$
\begin{array}{l} f (\mathbf {A}) = \sum_ {k = 1} ^ {m} f \left(\lambda_ {k}\right) p _ {k} (\mathbf {A}) \\ = \sum_ {k = 1} ^ {m} f (\lambda_ {k}) \frac {\left(\mathbf {A} - \lambda_ {1} \mathbf {I}\right) \cdots \left(\mathbf {A} - \lambda_ {k - 1} \mathbf {I}\right) \left(\mathbf {A} - \lambda_ {k + 1} \mathbf {I}\right) \cdots \left(\mathbf {A} - \lambda_ {m} \mathbf {I}\right)}{\left(\lambda_ {k} - \lambda_ {1}\right) \cdots \left(\lambda_ {k} - \lambda_ {k - 1}\right) \left(\lambda_ {k} - \lambda_ {k + 1}\right) \cdots \left(\lambda_ {k} - \lambda_ {m}\right)} \tag {9-102} \\ \end{array}
$$

Equation (9–102) is known as Sylvester’s interpolation formula. Equation (9–102) is equivalent to the following equation:

$$
\left| \begin{array}{c c c c c} 1 & 1 & \dots & 1 & \mathbf {I} \\ \lambda_ {1} & \lambda_ {2} & \dots & \lambda_ {m} & \mathbf {A} \\ \lambda_ {1} ^ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {m} ^ {2} & \mathbf {A} ^ {2} \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \lambda_ {1} ^ {m - 1} & \lambda_ {2} ^ {m - 1} & \dots & \lambda_ {m} ^ {m - 1} & \mathbf {A} ^ {m - 1} \\ f (\lambda_ {1}) & f (\lambda_ {2}) & \dots & f (\lambda_ {m}) & f (\mathbf {A}) \end{array} \right| = \mathbf {0} \tag {9-103}
$$

Equations (9–102) and (9–103) are frequently used for evaluating functions $f ( \mathbf { A } )$ of matrix A— for example, $( \lambda \mathbf { I } - \mathbf { A } ) ^ { - 1 } , e ^ { \mathbf { A } t }$ t, and so forth. Note that Equation (9–103) can also be written as
