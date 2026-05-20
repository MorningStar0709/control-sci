# 8.1 INTRODUCTION

During the past 15 to 20 years, developments in linear control theory have concentrated on the control of multivariable systems. Many systems, particularly in technologically advanced areas such as aerospace systems, are represented by models with several inputs, with each input having a significant effect on several outputs. Such cross-coupling makes the use of single-input, single-output (SISO) methods difficult.

In parallel with developments in multi-input, multi-output (MIMO) systems, the past 15 years have seen a renewed emphasis on frequency response. The ability of the state framework to handle uncertainty, especially nonparametric uncertainty, proved deficient. In contrast, uncertainty fits quite naturally in an input–output setting such as frequency response. The state framework has not been cast aside; rather, connections have been made between it and the frequency-response approach.

Developments in frequency-response design have been greatly abetted by the introduction of $H^{\infty}$ theory. Quadratic performance indices do lead to integrals in the frequency domain, through Parseval's integral. However, engineers are usually concerned with specifications expressed pointwise in the frequency domain, not with the averages yielded by integrals. The $H^{\infty}$ theory provides a direct handle on this type of specification.

In this chapter, we introduce the basic closed-loop expressions for the multivariable case. We then discuss norms, with emphasis on the 2-norm and the $\infty$ -norm. Stability, uncertainty, and robust stability follow. The standard design problem is defined, and $H^{2}$ and $H^{\infty}$ solutions are worked out.
