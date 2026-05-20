# 7.6.1 Introduction

Up to now in this chapter, we have assumed that the state vector (system or disturbance) is available for use in a state feedback law. In practice, more often than not, the complete state vector is not measured; sensors are not always available and, furthermore, they add to the system's cost and complexity.

It might appear that state feedback methods have very limited applicability, being restricted to those few cases where all components of the state are available. Fortunately, it is possible to estimate the state of a system, provided the system is observable. This is done by designing a dynamical system called a state observer, whose inputs are the system inputs and outputs and that produces as outputs estimates of the unmeasured states of the system. It is possible to recover much of the behavior of a state feedback law by using state estimates instead of states in the feedback law.
