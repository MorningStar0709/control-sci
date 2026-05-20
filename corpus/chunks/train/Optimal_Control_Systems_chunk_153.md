# 3.1 Problem Formulation

3. If we try to keep the output or state near a desired state or output, then we are dealing with a tracking system. We see that in both state and output regulator systems, the desired or reference state is zero and in tracking system the error is to be made zero. For example, consider again the antenna control system to track an aircraft.

Let us consider the various matrices in the cost functional (3.1.3) and their implications.

1. The Error Weighted Matrix $\mathbf{Q}(t)$ : In order to keep the error $\mathbf{e}(t)$ small and error squared non-negative, the integral of the expression $\frac{1}{2}\mathbf{e}'(t)\mathbf{Q}(t)\mathbf{e}(t)$ should be nonnegative and small. Thus, the matrix $\mathbf{Q}(t)$ must be positive semidefinite. Due to the quadratic nature of the weightage, we have to pay more attention to large errors than small errors.

2. The Control Weighted Matrix $\mathbf{R}(t)$ : The quadratic nature of the control cost expression $\frac{1}{2}\mathbf{u}'(t)\mathbf{R}(t)\mathbf{u}(t)$ indicates that one has to pay higher cost for larger control effort. Since the cost of the control has to be a positive quantity, the matrix $\mathbf{R}(t)$ should be positive definite.

3. The Control Signal $\mathbf{u}(t)$ : The assumption that there are no constraints on the control $\mathbf{u}(t)$ is very important in obtaining the closed loop optimal configuration.

Combining all the previous assumptions, we would like on one hand, to keep the error small, but on the other hand, we must not pay higher cost to large controls.

4. The Terminal Cost Weighted Matrix $\mathbf{F}(t_f)$ : The main purpose of this term is to ensure that the error $\mathbf{e}(t)$ at the final time $t_f$ is as small as possible. To guarantee this, the corresponding matrix $\mathbf{F}(t_f)$ should be positive semidefinite.

Further, without loss of generality, we assume that the weighted matrices $\mathbf{Q}(t), \mathbf{R}(t)$ , and $\mathbf{F}(t)$ are symmetric. The quadratic cost functional described previously has some attractive features:

(a) It provides an elegant procedure for the design of closed-loop optimal controller.

(b) It results in the optimal feed-back control that is linear in state function.

That is why we often say that the “quadratic performance index fits like a glove” [6].

5. Infinite Final Time: When the final time $t_{f}$ is infinity, the terminal cost term involving $\mathbf{F}(t_{f})$ does not provide any realistic sense since we are always interested in the solutions over finite time. Hence, $\mathbf{F}(t_{f})$ must be zero.
