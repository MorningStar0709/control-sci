# 10–5 STATE OBSERVERS

In the pole-placement approach to the design of control systems, we assumed that all state variables are available for feedback. In practice, however, not all state variables are available for feedback. Then we need to estimate unavailable state variables.

Estimation of unmeasurable state variables is commonly called observation.A device (or a computer program) that estimates or observes the state variables is called a state observer, or simply an observer. If the state observer observes all state variables of the system, regardless of whether some state variables are available for direct measurement, it is called a full-order state observer.There are times when this will not be necessary, when we will need observation of only the unmeasurable state variables, but not of those that are directly measurable as well. For example, since the output variables are observable and they are linearly related to the state variables, we need not observe all state variables, but observe only n-m state variables, where n is the dimension of the state vector and m is the dimension of the output vector.

An observer that estimates fewer than n state variables, where n is the dimension of the state vector, is called a reduced-order state observer or, simply, a reduced-order observer. If the order of the reduced-order state observer is the minimum possible, the observer is called a minimum-order state observer or minimum-order observer. In this section, we shall discuss both the full-order state observer and the minimum-order state observer.

State Observer. A state observer estimates the state variables based on the measurements of the output and control variables. Here the concept of observability discussed in Section 9–7 plays an important role. As we shall see later, state observers can be designed if and only if the observability condition is satisfied.

In the following discussions of state observers, we shall use the notation toxdesignate the observed state vector. In many practical cases, the observed state vector is used in the state feedback to generate the desired control vector.x-

Consider the plant defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-55}y = \mathbf {C x} \tag {10-56}$$
