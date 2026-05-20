and checks the following inequality, which tests if $V ( u ^ { p } )$ is convex-like

$$V (u ^ {p + 1}) \leq \sum_ {i \in \mathbb {I} _ {1: M}} w _ {i} V (u _ {i} ^ {p} + \alpha_ {i} ^ {p} v _ {i} ^ {p}, u _ {- i} ^ {p}) \tag {5}$$

in which $\textstyle \sum _ { i \in \mathbb { I } _ { 1 : M } } w _ { i } = 1$ and $w _ { i } > 0$ for all $i \in \mathbb { I } _ { 1 : M }$ . If condition (5) is not satisfied, then we find the direction with the worst cost improvement $i _ { \mathrm { m a x } } = \mathrm { a r g }$ max $\{ V ( u _ { i } ^ { p } + \alpha _ { i } ^ { p } v _ { i } ^ { p } , u _ { - i } ^ { p } ) \}$ }, and eliminate this direction by setting $\boldsymbol { w } _ { i _ { \mathrm { m a x } } }$ to zero and repartitioning the remaining $w _ { i }$ so that they sum to 1. We then reform the candidate step (4) and check condition (5) again. We repeat until (5) is satisfied. At worst, condition (5) is satisfied with only one direction.

Notice that the test of inequality (5) does not require a coordinator. Each subsystem has a copy of the plantwide model and can evaluate the objection function independently. Therefore, the set of comparisons can be run on each controller. This computation represents a small overhead compared to a coordinating optimization.
