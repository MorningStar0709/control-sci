# 7.4.1 Introduction

The rather puzzling term “linear–quadratic” (LQ) is shorthand for “optimal linear regulator for a quadratic performance index.” The LQ regulator is possibly the most important result of modern control. Many practical problems can be cast in the LQ framework, and there are excellent numerical algorithms for their solution.

In the LQ regulator, performance is assessed by a scalar performance index, of the form

$$J = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} (t) Q \mathbf {x} (t) + \mathbf {u} ^ {T} (t) R \mathbf {u} (t) ] d t \tag {7.19}$$

where Q and R, both symmetric matrices, are positive semidefinite and positive definite, respectively.

The expressions $\mathbf{x}^T Q\mathbf{x}$ and $\mathbf{u}^T R\mathbf{u}$ are quadratic forms. It is useful to recall that

$$
\begin{array}{l} \mathbf {x} ^ {T} Q \mathbf {x} = Q _ {1 1} x _ {1} ^ {2} + 2 Q _ {1 2} x _ {1} x _ {2} + \dots + 2 Q _ {1 n} x _ {1} x _ {n} \\ + Q _ {2 2} x _ {2} ^ {2} + \dots + 2 Q _ {2 n} x _ {2} x _ {n} \\ + \dots \\ + Q _ {n n} x _ {n} ^ {2}. \\ \end{array}
$$

If $Q$ is positive semidefinite (in shorthand, $Q \geq 0$ ) then $\mathbf{x}^T Q\mathbf{x} \geq 0$ for all $\mathbf{x}$ . If $Q$ is positive definite ( $Q > 0$ ), then $\mathbf{x}^T Q\mathbf{x} > 0$ for all $\mathbf{x} \neq 0$ .

The problem to be solved is assumed to be a regulation problem where the objective is to drive the state from some initial value to zero. The term $\mathbf{x}^{T}(t)Q\mathbf{x}(t)$ penalizes departures of $\mathbf{x}(t)$ from zero. The penalty is quadratic, so large errors are penalized much more than small ones; for example, $Q_{11}(.1)^{2}=0.01Q_{11}$ , whereas $Q_{11}(10)^{2}=1000Q_{11}$ . The integral accumulates $\mathbf{x}^{T}(t)Q\mathbf{x}(t)$ over time, so long-lasting departures from $\mathbf{x}(t)=0$ are penalized more than short-lived ones. It is desirable to have a small value for the term $\int_{0}^{\infty}\mathbf{x}^{T}(t)Q\mathbf{x}(t)dt$ , because that implies that, on average, $\mathbf{x}(t)$ is relatively near zero.
