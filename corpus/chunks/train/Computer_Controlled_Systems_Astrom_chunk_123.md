# Shift-Operator Calculus

Differential-operator calculus is a convenient tool for manipulating linear differential equations with constant coefficients. An analogous operator calculus can be developed for systems described by linear difference equations with constant coefficients. In the development of operator calculus, the systems are viewed as operators that map input signals to output signals. To specify an operator it is necessary to give its range—that is, to define the class of input signals and to describe how the operator acts on the signals. In shift-operator calculus, all signals are considered as doubly infinite sequences $\{f(k):k=\cdots-1,0,1,\ldots\}$ . For convenience the sampling period is chosen as the time unit.

The forward-shift operator is denoted by q. It has the property

$$q f (k) = f (k + 1)$$

If the norm of a signal is defined as

$$\| f \| = \sup _ {k} | f (k) |$$

Or

$$\| f \| ^ {2} = \sum_ {k = - \infty} ^ {\infty} f ^ {2} (k)$$

it follows that the shift operator has unit norm. This means that the calculus of shift operators is simpler than differential-operator calculus, because the differential operator is unbounded. The inverse of the forward-shift operator is called the backward-shift operator or the delay operator and is denoted by $q^{-1}$ . Hence

$$q ^ {- 1} f (k) = f (k - 1)$$

Notice that it is important for the range of the operator to be doubly infinite sequences; otherwise, the inverse of the forward-shift operator may not exist. In discussions of problems related to the characteristic equation of a system, such as stability and system order, it is more convenient to use the forward-shift operator. In discussions of problems related to causality, it is more convenient to use the backward-shift operator. Operator calculus gives compact descriptions of systems and makes it easy to derive relationships among system variables, because manipulation of difference equations is reduced to a purely algebraic problem.

The shift operator is used to simplify the manipulation of higher-order difference equations. Consider the equation

$$
\begin{array}{l} y (k + n \alpha) + a _ {1} y (k + n \alpha - 1) + \dots + a _ {n \alpha} y (k) \tag {2.21} \\ = b _ {0} u (k + n b) + \dots + b _ {n b} u (k) \\ \end{array}
$$

where $na \geq nb$ . Use of the shift operator gives

$$(q ^ {n a} + a _ {1} q ^ {n a - 1} + \dots + a _ {n a}) y (k) = (b _ {0} q ^ {n b} + \dots + b _ {n b}) u (k)$$

With the introduction of the polynomials
