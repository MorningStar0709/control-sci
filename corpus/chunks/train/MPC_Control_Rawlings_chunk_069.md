# 1.3.1 Linear Quadratic Problem

We start by designing a controller to take the state of a deterministic, linear system to the origin. If the setpoint is not the origin, or we wish to track a time-varying setpoint trajectory, we will subsequently make modifications of the zero setpoint problem to account for that. The system model is

$$x ^ {+} = A x + B uy = C x \tag {1.5}$$

In this first problem, we assume that the state is measured, or $C = I$ . We will handle the output measurement problem with state estimation in the next section. Using the model we can predict how the state evolves given any set of inputs we are considering. Consider N time steps into the future and collect the input sequence into u,

$$\mathbf {u} = \{u (0), u (1), \dots , u (N - 1) \}$$

Constraints on the u sequence (i.e., valve saturations, etc.) are covered extensively in Chapter 2. The constraints are the main feature that distinguishes MPC from the standard linear quadratic (LQ) control.

We first define an objective function V (·) to measure the deviation of the trajectory of x(k), u(k) from zero by summing the weighted squares

$$V (x (0), \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left[ x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) \right] + \frac {1}{2} x (N) ^ {\prime} P _ {f} x (N)$$

subject to

$$x ^ {+} = A x + B u$$

The objective function depends on the input sequence and state sequence. The initial state is available from the measurement. The remainder of the state trajectory, ${ \boldsymbol { x } } ( k ) , k = 1 , \ldots , N$ , is determined by the model and the input sequence u. So we show the objective function’s explicit dependence on the input sequence and initial state. The tuning parameters in the controller are the matrices Q and R. We allow the final state penalty to have a different weighting matrix, $P _ { f }$ , for generality. Large values of $Q$ in comparison to R reflect the designer’s intent to drive the state to the origin quickly at the expense of large control action. Penalizing the control action through large values of R relative to Q is the way to reduce the control action and slow down the rate at which the state approaches the origin. Choosing appropriate values of $Q$ and R (i.e., tuning) is not always obvious, and this difficulty is one of the challenges faced by industrial practitioners of LQ control. Notice that MPC inherits this tuning challenge.

We then formulate the following optimal LQ control problem

$$\min _ {\mathbf {u}} V (x (0), \mathbf {u}) \tag {1.6}$$

The Q, $P _ { f }$ and R matrices often are chosen to be diagonal, but we do not assume that here. We assume, however, that $Q , P _ { f }$ , and R are real and symmetric; Q and $P _ { f }$ are positive semidefinite; and R is positive definite. These assumptions guarantee that the solution to the optimal control problem exists and is unique.
