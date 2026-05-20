# Techniques for Controller Design

Regulation problems are often solved by feedback, but feedforward techniques can be very useful if disturbances can be measured.

If the specifications are given in terms of the transfer function, relating the output to the disturbance, it is natural to apply methods that admit control of this transfer function. One method is pole placement, which allows specification of the complete transfer function. This straightforward design technique was discussed in detail in Chapters 4 and 5. It is often too restrictive to specify the complete closed-loop transfer function, which is a drawback.

Another possibility is to use a frequency-response method, which admits control of the frequency response from the disturbance to the output. Such problems are most conveniently expressed in terms of continuous-time theory. The controllers obtained can then be translated to digital-control algorithms using the techniques described in Chapter 8.

If the criteria are expressed as optimization criteria, it is natural to use design techniques based on optimization. Techniques based on minimizing the variance of the process output and other types of quadratic criteria are discussed in Chapters 11 and 12.
