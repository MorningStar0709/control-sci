# Example 2.9

Verify that the straight line represents the minimum distance between two points.

Solution: This is an obvious solution, however, we illustrate the second variation. Earlier in Example 2.7, we have formulated a functional for the distance between two points as

$$J = \int_ {t _ {0}} ^ {t _ {f}} \sqrt {1 + \dot {x} ^ {2} (t)} d t = \int_ {t _ {0}} ^ {t _ {f}} V (\dot {x} (t)) d t \tag {2.4.8}$$

and found that the optimum is a straight line $x^{*}(t) = C_{1}t + C_{2}$ . To satisfy the sufficiency condition (2.4.7), we find

$$\left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} = \frac {\dot {x} ^ {*} (t)}{\sqrt {1 + \dot {x} ^ {* 2} (t)}} \text {and} \left(\frac {\partial^ {2} V}{\partial \dot {x} ^ {2}}\right) _ {*} = \frac {1}{[ 1 + \dot {x} ^ {* 2} (t) ] ^ {3 / 2}}. \tag {2.4.9}$$

Since $\dot{x}^{*}(t)$ is a constant (+ve or -ve), the previous equation satisfies the condition (2.4.7). Hence, the distance between two points as given by $x^{*}(t)$ (straight line) is minimum.

Next, we begin the second stage of optimal control. We consider optimization (or extremization) of a functional with a plant, which is considered as a constraint or a condition along with the functional. In other words, we address the extremization of a functional with some condition, which is in the form of a plant equation. The plant takes the form of state equation leading us to optimal control of dynamic systems. This section is motivated by $[6, 79, 120, 108]$ .
