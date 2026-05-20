The argument of a signal is thus not real time but instead the number of sampling intervals. We call this the sampling-time convention. We will use real time whenever there are possibilities for confusion.

Disturbances. Initially it will be assumed that the disturbances acting on the process are impulses that occur irregularly, and that the impulses are so widely spread that the system settles between the impulses. Because the impulses are far apart and the effect of an impulse is simply to change the process state, the disturbance can be represented by an initial state. Later we will extend the results to much more general disturbances that are generated from dynamic systems whose inputs are impulses. Typical examples are steps, ramps, and sinusoidal signals.

Process uncertainty. Uncertainties in the elements of the matrices A and B can be dealt with in the state-space formulation, but it is not easy to deal with other forms of unmodeled dynamics. A discussion of process uncertainties therefore will be given later when more appropriate tools have been developed.

The criterion. When discussing regulation problems it will be assumed that the criterion is to bring the state to zero after perturbations in the initial condition. In the pole-placement formulation, the rate of decay of the state is given indirectly by specifying the poles of the closed-loop system. Servo problems will be dealt with by requiring that the signal transmission from command signal to process variables is close to a behavior specified by a model.

Admissible controls. Because feedback solutions are desired, it is necessary to specify the information available for generating the control signal. When the properties of the system are specified by its closed-loop poles, it is natural to require that the feedback is linear. Several different versions will be discussed. We will start with the case when all state variables are measured directly without error. The admissible controls are then a linear feedback of the form

$$u (k) = - L x (k) \tag {4.3}$$

This assumption will be relaxed later in Sec. 4.5, where it will be assumed that only outputs are available for control. For discrete-time systems it is also of interest to consider the case when there are delays in the measurements.
