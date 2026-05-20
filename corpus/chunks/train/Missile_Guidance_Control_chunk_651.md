$$
\begin{array}{l} \frac {d \mathbf {e} _ {r}}{d t} = \left(\frac {d \theta}{d t}\right) \mathbf {e} _ {\theta}, \\ \frac {d \mathbf {e} _ {\theta}}{d t} = - \left(\frac {d \theta}{d t}\right) \mathbf {e} _ {r}, \\ \frac {d \mathbf {r}}{d t} = r \left(\frac {d \theta}{d t}\right) \mathbf {e} _ {\theta} + \left(\frac {d r}{d t}\right) \mathbf {e} _ {r}, \\ \frac {d ^ {2} \mathbf {r}}{d t ^ {2}} = \left(\frac {d r}{d t}\right) \left(\frac {d \mathbf {e} _ {r}}{d t}\right) + \mathbf {e} _ {r} \left(\frac {d ^ {2} r}{d t ^ {2}}\right) + r \left(\frac {d \theta}{d t}\right) \left(\frac {d \mathbf {e} _ {\theta}}{d t}\right) \\ + r \mathbf {e} _ {\theta} \left(\frac {d ^ {2} \theta}{d t ^ {2}}\right) + \left(\frac {d r}{d t}\right) \left(\frac {d \theta}{d t}\right) \mathbf {e} _ {\theta}, \\ \end{array}
$$

or

$$\mathbf {a} = \frac {d ^ {2} \mathbf {r}}{d t ^ {2}} = \left[ \left(\frac {d ^ {2} r}{d t ^ {2}}\right) - r \left(\frac {d \theta}{d t}\right) ^ {2} \right] \mathbf {e} _ {r} + \left[ r \left(\frac {d ^ {2} \theta}{d t ^ {2}}\right) + 2 \left(\frac {d r}{d t}\right) \left(\frac {d \theta}{d t}\right) \right] \mathbf {e} _ {\theta}. \tag {6.237}$$

The velocity components u and v are now given by

$$u = \frac {d s}{d t}, \quad v = \frac {d r}{d t},s = r \theta , \qquad a = \frac {d v}{d t} = \frac {d ^ {2} r}{d t ^ {2}},$$

and therefore,

$$u = r \left(\frac {d \theta}{d t}\right), \tag {6.238}$$

where r is a constant. Now let y be the altitude. Then

$$y = r _ {o} + r,$$

where $r _ { o }$ is the radius of the Earth, which is constant. Next, we have

$${\frac {d y}{d t}} = {\frac {d r}{d t}}$$

and

$$\left(\frac {d \theta}{d t}\right) = u / r, \quad \frac {d ^ {2} \theta}{d t ^ {2}} = \left[ r \left(\frac {d u}{d t}\right) - u \left(\frac {d r}{d t}\right) \right] / r ^ {2}.$$

Therefore,

$$
\begin{array}{l} \mathbf {a} = \left[ \left(\frac {d v}{d t}\right) - r (u / r) ^ {2} \right] \mathbf {e} _ {r} + \left\{r \left[ \left(\left(\frac {d u}{d t}\right) - u \left(\frac {d r}{d t}\right)\right) / r ^ {2} \right] + 2 v (u / r) \right\} \mathbf {e} _ {\theta} \\ = \left[ \left(\frac {d v}{d t}\right) - (u ^ {2} / r) \right] \mathbf {e} _ {r} + \left[ \left(\frac {d u}{d t}\right) - (u / r) \left(\frac {d r}{d t}\right) + 2 (u v / r) \right] \mathbf {e} _ {\theta} \\ = \left[ \left(\frac {d v}{d t}\right) - (u ^ {2} / r) \right] \mathbf {e} _ {r} + \left[ \left(\frac {d u}{d t}\right) + (u v / r) \right] \mathbf {e} _ {\theta}. \tag {6.239} \\ \end{array}
$$
