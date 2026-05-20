# 4.1 Linear Quadratic Tracking System: Finite-Time Case

In this section, we discuss the linear quadratic tracking (LQT) system to maintain the output as close as possible to the desired output with minimum control energy [6]. We are given a linear, observable system

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t)\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) \tag {4.1.1}$$

where, $\mathbf{x}(t)$ is the nth order state vector, $\mathbf{u}(t)$ is the rth order control vector, and $\mathbf{y}(t)$ is the mth order output vector. Let $\mathbf{z}(t)$ be the mth order desired output and the various matrices $\mathbf{A}(t), \mathbf{B}(t)$ and $\mathbf{C}(t)$ be of appropriate dimensionality. Our objective is to control the system (4.1.1) in such a way that the output $\mathbf{y}(t)$ tracks the desired output $\mathbf{z}(t)$ as close as possible during the interval $[t_{0}, t_{f}]$ with minimum expenditure of control effort. For this, let us define the error vector as

$$\mathbf {e} (t) = \mathbf {z} (t) - \mathbf {y} (t) \tag {4.1.2}$$

and choose the performance index as

$$
\begin{array}{l} J = \frac {1}{2} \mathbf {e} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {e} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {e} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {e} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {4.1.3} \\ \end{array}
$$

with $t_{f}$ specified and $\mathbf{x}(t_{f})$ not specified. In this way we are dealing with free-final state system. Also, we assume that $\mathbf{F}(t_{f})$ and $\mathbf{Q}(t)$ are mxm symmetric, positive semidefinite matrices, and $\mathbf{R}(t)$ is rxr symmetric, positive definite matrix. We now use the Pontryagin Minimum Principle in the following order.

- Step 1: Hamiltonian   
- Step 2: Open-Loop Optimal Control   
- Step 3: State and Costate System   
- Step 4: Riccati and Vector Equations   
- Step 5: Closed-Loop Optimal Control   
- Step 6: Optimal State
