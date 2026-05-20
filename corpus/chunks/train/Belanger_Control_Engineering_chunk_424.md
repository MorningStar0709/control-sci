# 7.6.3 The Full-Order Observer

We add a measurement to the system of Equation 7.54, i.e.,

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}\mathbf {y} = C \mathbf {x} \tag {7.59}$$

with $\mathbf{x}$ of dimension $n$ and $\mathbf{y}$ of dimension $m$ . We try the observer structure

$$\dot {\widehat {\mathbf {x}}} = A \widehat {\mathbf {x}} + B \mathbf {u} + G (\mathbf {y} - C \widehat {\mathbf {x}}). \tag {7.60}$$

Here, $\dim (\widehat{\mathbf{x}}) = n$ [same as $\dim (\mathbf{x})]$ and $G$ is a constant $n\times m$ matrix, the observer gain. This structure adds a correction term, $G(\mathbf{y} - C\widehat{\mathbf{x}})$ , to the previous observer.

If $\widehat{\mathbf{x}} = \mathbf{x}$ , then $\mathbf{y} - C\widehat{\mathbf{x}} = \mathbf{y} - C\mathbf{x} = \mathbf{0}$ , and there is no correction. On the other hand, if $C\widehat{\mathbf{x}} \neq \mathbf{y}$ , a correction will be applied. We must show that this correction can be made so as to drive the error to zero.
