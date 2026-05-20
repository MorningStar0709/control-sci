# 2–4 MODELING IN STATE SPACE

In this section we shall present introductory material on state-space analysis of control systems.

Modern Control Theory. The modern trend in engineering systems is toward greater complexity, due mainly to the requirements of complex tasks and good accuracy. Complex systems may have multiple inputs and multiple outputs and may be time varying. Because of the necessity of meeting increasingly stringent requirements on the performance of control systems, the increase in system complexity, and easy access to large scale computers, modern control theory, which is a new approach to the analysis and design of complex control systems, has been developed since around 1960.This new approach is based on the concept of state. The concept of state by itself is not new, since it has been in existence for a long time in the field of classical dynamics and other fields.

Modern Control Theory Versus Conventional Control Theory. Modern control theory is contrasted with conventional control theory in that the former is applicable to multiple-input, multiple-output systems, which may be linear or nonlinear, time invariant or time varying, while the latter is applicable only to linear timeinvariant single-input, single-output systems. Also, modern control theory is essentially time-domain approach and frequency domain approach (in certain cases such as H-infinity control), while conventional control theory is a complex frequency-domain approach. Before we proceed further, we must define state, state variables, state vector, and state space.

State. The state of a dynamic system is the smallest set of variables (called state variables) such that knowledge of these variables at $t = t _ { 0 }$ , together with knowledge of the input for $t \geq t _ { 0 }$ , completely determines the behavior of the system for any time $t \geq t _ { 0 }$ .

Note that the concept of state is by no means limited to physical systems. It is applicable to biological systems, economic systems, social systems, and others.
