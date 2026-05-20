# Dual Control

The schemes for adaptive control described so far look like reasonable heuristic approaches. Already from their description it appears that they have some limitations. For example, parameter uncertainties are not taken into account in the design of the controller. It is then natural to ask whether there are better approaches than the certainty equivalence scheme. We may also ask whether adaptive controllers can be obtained from some general principles. It is possible to obtain a solution that follows from an abstract problem formulation and use of optimization theory. The particular tool one could use is nonlinear stochastic control theory. This will lead to the notion of dual control. The approach will give a controller structure with interesting properties. A major consequence is that the uncertainties in the estimated parameters will be taken into account in the controller. The controller will also take special actions when it has poor knowledge about the process. The approach is so complicated, however, that so far it has not been possible to use it for practical problems. Since the ideas are conceptually useful, we will discuss them briefly in this section.

The first problem that we are faced with is to describe mathematically the idea that a constant or slowly varying parameter is unknown. An unknown constant can be modeled by the differential equation

$$\frac {d \theta}{d t} = 0 \tag {1.8}$$

with an initial distribution that reflects the parameter uncertainty. Parameter drift can be described by adding random variables to the right-hand side of Eq. (1.8). A model of a plant with uncertain parameters is thus obtained by augmenting the state variables of the plant and its environment by the parameter vector whose dynamics is given by Eq. (1.8). Notice that with this formulation there is no distinction between these parameters and the other state variables. This means that the resulting controller can handle very rapid parameter variations. An augmented state $z = \begin{pmatrix} x^{T} & \theta^{T} \end{pmatrix}^{T}$ consisting of the state of the process and the parameters can now be introduced. The goal of the control is then formulated to minimize a loss function

![](image/4dfe6d07f6702ff27798900379bbfed37474a934ba5a4c024f715b0a59b83ab2.jpg)

<details>
<summary>flowchart</summary>
