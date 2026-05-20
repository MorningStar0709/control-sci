# Gain Changers

External feedback loops, which adjust the relay amplitude, may be used to resolve the compromise between a high tracking rate and a small limit cycle amplitude. The so-called up-logic used in the first SOAS can be described as follows:

$$
d = \left\{ \begin{array}{l l} d _ {1} & \text { if } | e | > e _ {l} \\ d _ {2} + (d _ {1} - d _ {2}) e ^ {- (t - t _ {0}) / T} & \text { if } | e | <   e _ {i} \end{array} \right.
$$

The time $t_{0}$ is the last time that $|e| < e_{l}$ . The relay amplitude is thus increased to $d_{1}$ when the error exceeds a limit $e_{l}$ . The relay amplitude then decreases to a lower level $d_{2}$ when the error is less than $e_{l}$ . This gain changer increases the relay amplitude and the response rate when large reference signals are applied.

Another type of gain changer has been used to control the amplitude of the limit cycle. The limit cycle amplitude at the process output is measured by a band-pass filter and a rectifier. The relay amplitude is then adjusted to keep the limit cycle amplitude constant at the process output.
