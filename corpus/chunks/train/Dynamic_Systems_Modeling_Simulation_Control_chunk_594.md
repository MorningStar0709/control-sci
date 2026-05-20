# Controller Design Using Root Locus

The previous examples illustrate how the closed-loop root locations change as the control gain increases. In Example 10.10, a P-controller cannot provide a good closed-loop response for the given plant because the root locus (Fig. 10.36) shows that two branches move toward and eventually cross the imaginary axis as gain increases. By contrast, Example 10.11 and Fig. 10.38 demonstrate that a fast, well-damped transient response can be obtained (for a different plant) by a simple gain adjustment. The cause of this performance difference is the plant system dynamics. The plant in Example 10.10 did not have any open-loop zeros, while the second-order plant in Example 10.11 included a single open-loop zero at s = –6. Open-loop zeros act as “sinks” and tend to attract the root-locus branches (recall that a branch will terminate at the open-loop zero as the gain increases to infinity). Therefore, in many cases where the plant does not have sufficient damping, it is possible to introduce an open-loop zero by adding a PD controller to the forward path. Recall that the transfer function for a PD controller is

$$G _ {C} (s) = K _ {P} + K _ {D} s \tag {10.45}$$

which has two adjustable gains $K _ { P }$ and $K _ { D }$ and one zero at $s = - K _ { P } / K _ { D }$ . Another way to express the PD controller is

$$G _ {C} (s) = K \left(s + z _ {D}\right) \tag {10.46}$$

where $K = K _ { D }$ is the single gain and $z _ { D } = K _ { P } / K _ { D }$ . Therefore, the open-loop zero is $s = - z _ { D }$ . Consequently, by adding the PD transfer function (10.46) to the forward path, the control engineer has altered the open-loop pole-zero map and changed the structure of the root locus. If the open-loop zero $- z _ { D }$ is properly selected, then it may be possible to “bend” the root-locus branches to the left and therefore obtain a fast, well-damped closed-loop response. We demonstrate this aspect of root-locus design with the following example.
