where $W _ { 1 }$ and $W _ { 2 }$ are stable transfer matrices that characterize the spatial and frequency structure of the uncertainty, confines the matrix $P _ { \Delta }$ to a neighborhood of the nominal model P . In particular, if $W _ { 1 } = I$ and $W _ { 2 } = w ( s ) I$ , where $w ( s )$ is a scalar function, then $P _ { \Delta }$ describes a disk centered at P with radius $w ( j \omega )$ at each frequency, as shown in Figure 8.1. The statement does not imply a mechanism or structure that gives rise to $\Delta$ . The uncertainty may be caused by parameter changes, as mentioned previously or by neglected dynamics, or by a host of other unspecified effects. An alternative statement to equation (8.1) is the so-called multiplicative form:

$$P _ {\Delta} (s) = \left(I + W _ {1} (s) \Delta (s) W _ {2} (s)\right) P (s). \tag {8.2}$$

This statement confines $P _ { \Delta }$ to a normalized neighborhood of the nominal model P . An advantage of equation (8.2) over (8.1) is that in equation (8.2) compensated transfer functions have the same uncertainty representation as the raw model (i.e., the weighting functions apply to $P K$ as well as P ). Some other alternative set membership statements will be discussed later.

![](image/4a6226c1d5496bbb8b9f78e346b66ebae52a86934242d49b3001602d067fd2c2.jpg)

<details>
<summary>text_image</summary>

P(jω)
w(jω)
</details>

Figure 8.1: Nyquist diagram of an uncertain model

The best choice of uncertainty representation for a specific FDLTI model depends, of course, on the errors the model makes. In practice, it is generally possible to represent some of these errors in a highly structured parameterized form. These are usually the low-frequency error components. There are always remaining higher-frequency errors, however, which cannot be covered this way. These are caused by such effects as infinite-dimensional electromechanical resonance, time delays, diffusion processes, etc. Fortunately, the less structured representations, such as equations (8.1) and (8.2), are well suited to represent this latter class of errors. Consequently, equations (8.1) and (8.2) have become widely used “generic” uncertainty representations for FDLTI models. An important point is that the construction of the weighting matrices $W _ { 1 }$ and $W _ { 2 }$ for multivariable systems is not trivial.
