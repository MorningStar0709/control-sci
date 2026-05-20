# 9–6 CONTROLLABILITY

Controllability and Observability. A system is said to be controllable at time $t _ { 0 }$ if it is possible by means of an unconstrained control vector to transfer the system from any initial state $\mathbf { x } \big ( t _ { 0 } \big )$ to any other state in a finite interval of time.

A system is said to be observable at time $t _ { 0 }$ if, with the system in state $\mathbf { x } \big ( t _ { 0 } \big )$ , it is possible to determine this state from the observation of the output over a finite time interval.

The concepts of controllability and observability were introduced by Kalman. They play an important role in the design of control systems in state space. In fact, the conditions of controllability and observability may govern the existence of a complete solution to the control system design problem. The solution to this problem may not exist if the system considered is not controllable. Although most physical systems are controllable and observable, corresponding mathematical models may not possess the property of controllability and observability.Then it is necessary to know the conditions under which a system is controllable and observable. This section deals with controllability and the next section discusses observability.

In what follows, we shall first derive the condition for complete state controllability. Then we derive alternative forms of the condition for complete state controllability followed by discussions of complete output controllability. Finally, we present the concept of stabilizability.

Complete State Controllability of Continuous-Time Systems. Consider the continuous-time system.

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {9-51}$$

where x = state vector (n-vector)

u = control signal (scalar)

A = n \* n matrix

B = n \* 1 matrix

The system described by Equation (9–51) is said to be state controllable at $t = t _ { 0 }$ if it is possible to construct an unconstrained control signal that will transfer an initial state to any final state in a finite time interval $t _ { 0 } \leq t \leq t _ { 1 }$ If every state is controllable, then the. system is said to be completely state controllable.

We shall now derive the condition for complete state controllability. Without loss of generality, we can assume that the final state is the origin of the state space and that the initial time is zero, or $t _ { 0 } = 0$ .

The solution of Equation (9–51) is
