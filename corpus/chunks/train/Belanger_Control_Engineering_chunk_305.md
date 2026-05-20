# 6.2.1 Introduction

It is assumed that design objectives have been established for the closed-loop system in terms of (i) the dc steady-state response, (ii) the transient response, and (iii) the frequency response. In Chapter 4, the approach was to select a suitable closed-loop transfer function (e.g., S or T), subject to interpolation constraints, and to solve for the controller, $F(s)$ . This almost always yields an $F(s)$ whose order is comparable with that of the plant. We cannot use that approach if the structure of $F(s)$ is predetermined (e.g., a pure gain); rather, we must work directly with $F(s)$ ,

It therefore becomes necessary to translate closed-loop design requirements to open-loop requirements, i.e., requirements on the loop gain $L(s) = F(s)P(s)$ . Then $L(s)$ [and hence $F(s)$ ] is designed according to the open-loop specifications.
