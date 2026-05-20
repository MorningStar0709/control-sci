# (1) 连续系统的离散化

用 c2d 命令和 d2c 命令可以实现连续系统模型和离散系统模型之间的转换。c2d 命令用于将连续系统模型转换成离散系统模型，d2c 命令用于将离散系统模型转换为连续系统模型。

命令格式：sysd = c2d(sys, Ts, 'zoh')

$$\mathrm{sys} = \mathrm{d} 2 \mathrm{c} (\text { sysd }, ^ {\prime} \mathrm{zoh} ^ {\prime})$$

其中，sys 表示连续系统模型；sysd 表示离散系统模型；Ts 表示离散化采样时间；'zoh'表示采用零阶保持器，可缺省。
