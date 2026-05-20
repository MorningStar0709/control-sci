Now, since $\theta _ { r } = f ( \theta _ { h } )$ ,

$$d \theta_ {r} = \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) d \theta_ {h},$$

where $( \partial \theta _ { r } / \partial \theta _ { h } )$ is the radome error slope; that is,

$$R = \frac {\partial \theta_ {r}}{\partial \theta_ {h}}. \tag {3.75}$$

Also, the following relation holds:

$$\frac {d \theta_ {r}}{d t} = \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \theta_ {h}}{d t}\right) \Rightarrow \frac {d \theta_ {r}}{d t} = \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \theta_ {h}}{d t}\right).$$

The gimbal angle, $\theta _ { h }$ , can be obtained from Figure 3.23 as follows:

$$\theta_ {h} = (\lambda - \theta_ {m}) - \varepsilon ,$$

or

$$\theta_ {h} = \lambda - (\theta_ {m} + \varepsilon), \tag {3.76}$$

where $\left( \lambda - \theta _ { m } \right)$ is the look angle, and

$$\frac {d \theta_ {h}}{d t} = \frac {d \lambda}{d t} - \frac {d \theta_ {m}}{d t} - \frac {d \varepsilon}{d t}. \tag {3.77}$$

Therefore, from (3.74a) and (3.74b) we have

$$
\begin{array}{l} \frac {d \lambda_ {m}}{d t} = \frac {d \lambda}{d t} + \frac {d \theta_ {r}}{d t} = \frac {d \lambda}{d t} + \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) d \theta_ {h} \\ = \frac {d \lambda}{d t} + \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left[ \left(\frac {d \lambda}{d t}\right) - \left(\frac {d \theta_ {m}}{d t}\right) - \left(\frac {d \varepsilon}{d t}\right) \right] \\ = \frac {d \lambda}{d t} + \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \lambda}{d t}\right) - \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \theta_ {m}}{d t}\right) - \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \varepsilon}{d t}\right) \\ = \left[ 1 + \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \right] \frac {d \lambda}{d t} - \left(\frac {\partial \theta_ {r}}{\partial \theta_ {h}}\right) \left(\frac {d \theta_ {m}}{d t}\right) \\ = [ 1 + R ] \left(\frac {d \lambda}{d t}\right) - R \left(\frac {d \theta_ {m}}{d t}\right). \tag {3.78} \\ \end{array}
$$
