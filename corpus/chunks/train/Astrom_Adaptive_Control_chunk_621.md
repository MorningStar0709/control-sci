# Smooth Control Laws

The control law (10.10) has the drawback that the relay chatters. One way to avoid this is to make the relay characteristics smoother. To do this, introduce a boundary layer around the switching surface

$$B (t) = \left\{x (t) \mid | \sigma (x (t)) | \leq \varepsilon \right\} \quad \varepsilon > 0$$

The parameter $\varepsilon$ can be interpreted as a measure of the thickness of the boundary layer. The sign function in Eq. (10.10) is now replaced by the saturation function

$$
\operatorname{sat} (\sigma , \varepsilon) = \left\{ \begin{array}{l l} 1 & \quad \sigma > \varepsilon \\ \sigma / \varepsilon & \quad - \varepsilon \leq \sigma \leq \varepsilon \\ - 1 & \quad \sigma <   - \varepsilon \end{array} \right.
$$

The control law is then

$$u (t) = \frac {p ^ {T} f}{p ^ {T} g} - \frac {\mu}{p ^ {T} g} \operatorname{sat} (\sigma (x), \varepsilon) \tag {10.12}$$

The width of the boundary layer will influence the tracking performance and the bandwidth of the closed-loop system.
