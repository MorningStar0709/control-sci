$$
G = \left[ \begin{array}{l l l} e _ {1 1} & e _ {1 2} & e _ {1 3} \\ e _ {2 1} & e _ {2 2} & e _ {2 3} \\ e _ {3 1} & e _ {3 2} & e _ {3 3} \\ e _ {4 1} & e _ {4 2} & e _ {4 3} \end{array} \right] \left[ \begin{array}{l} 1 \\ 1 \\ 1 \\ 1 \end{array} \right] \tag {7.23}
$$

The unit vector from the GPS receiver to each satellite is defined as

$$
e _ {i} = \left[ \begin{array}{c} e _ {i 1} \\ e _ {i 2} \\ e _ {i 3} \end{array} \right].
$$

Therefore, the elements $e _ { i 1 } , e _ { i 2 } , e _ { i 3 } ( i = 1 , \dots , 4 )$ denote the direction cosines from the user to the satellites in question (or view). Specifically, the user will try to select the four visible satellites with minimum GDOP in order to reduce the error of the navigation fix induced by measurement errors. Note that by taking into account the fact that

$$e _ {i 1} ^ {2} + e _ {i 2} ^ {2} + e _ {i 3} ^ {2} = 1,$$

a closed-form solution of (7.22) is thus possible. Furthermore, the matrix product $( G ^ { T } G ) ^ { - 1 }$ can be expressed as

$$
(G ^ {T} G) ^ {- 1} = \left[ \begin{array}{c c c c} \sigma_ {x x} ^ {2} & \sigma_ {x y} ^ {2} & \sigma_ {x z} ^ {2} & \sigma_ {x t} ^ {2} \\ \sigma_ {y x} ^ {2} & \sigma_ {y y} ^ {2} & \sigma_ {y z} ^ {2} & \sigma_ {y t} ^ {2} \\ \sigma_ {z x} ^ {2} & \sigma_ {z y} ^ {2} & \sigma_ {z z} ^ {2} & \sigma_ {z t} ^ {2} \\ \sigma_ {t x} ^ {2} & \sigma_ {t y} ^ {2} & \sigma_ {t z} ^ {2} & \sigma_ {t t} ^ {2} \end{array} \right], \tag {7.24}
$$

where the diagonal values (or trace) are the variances of the estimated user position in each axis and in the user time offset. Thus, the GDOP can be expressed in the form

$$G D O P = (\sigma_ {x x} ^ {2} + \sigma_ {y y} ^ {2} + \sigma_ {z z} ^ {2} + \sigma_ {t t} ^ {2}) ^ {1 / 2}. \tag {7.25}$$

The GDOP is used as a figure of merit (or selection criterion) for selecting the best geometry from the satellites in view, and as stated above, the goal is to select a satellite configuration that minimizes the scalar value of GDOP. The GDOP can be further broken down into horizontal dilution of precision (HDOP), vertical dilution of precision (VDOP), position dilution of precision (PDOP), and time dilution of precision (TDOP). Mathematically, these terms are expressed in the form

$$H D O P = (\sigma_ {x x} ^ {2} + \sigma_ {y y} ^ {2}) ^ {1 / 2}, \tag {7.26}V D O P = \sigma_ {z z}, \tag {7.27}P D O P = \left(\sigma_ {x x} ^ {2} + \sigma_ {y y} ^ {2} + \sigma_ {z z} ^ {2}\right) ^ {1 / 2}, \tag {7.28}T D O P = \sigma_ {t t}, \tag {7.29}G D O P = (\sigma_ {x x} ^ {2} + \sigma_ {y y} ^ {2} + \sigma_ {z z} ^ {2} + \sigma_ {t t} ^ {2}) ^ {1 / 2}. \tag {7.25}$$
