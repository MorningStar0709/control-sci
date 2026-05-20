# 4. 系统的可控性与可观测性分析

在 MATLAB 的控制系统工具箱中提供了 ctrbf() 函数。该函数可以求出系统的可控阶梯变换，该函数的调用格式为

$$[ \mathrm{Ac}, \mathrm{Bc}, \mathrm{Cc}, \mathrm{Dc}, \mathrm{Tc}, \mathrm{Kc} ] = \operatorname{ctrbf} (\mathrm{A}, \mathrm{B}, \mathrm{C})$$

在 MATLAB 的控制系统工具箱中提供了 obsvf() 函数。该函数可以求出系统的可观测阶梯变换，该函数的调用格式为

$$[ \mathrm{Ao}, \mathrm{Bo}, \mathrm{Co}, \mathrm{Do}, \mathrm{To}, \mathrm{Ko} ] = \operatorname{obsvf} (\mathrm{A}, \mathrm{B}, \mathrm{C})$$
