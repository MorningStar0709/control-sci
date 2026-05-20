# 例6.6 复零极点的计算机辅助伯德图

利用 Matlab 重新完成例 6.5 的内容。

解答。要使用 Matlab 得到伯德图，我们要调用函数 bode，其语句如下。

```matlab
s = tf('s');
sysG = 0.01*(s^2 + 0.01*s + 1) / ((s^2)*(s^2)/4 + 0.01*s + 1));
[mag, phase, w] = bode(sysG);
loglog(w, squeeze(mag))
semilogx(w, squeeze(phase)) 
```

这些命令会得到一个与图 6.11 所示的极为相符的伯德图。若要得到以 dB 为单位的幅值曲线，最后的三行可用如下语句替换。

```prolog
bode(sysG). 
```
