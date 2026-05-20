# 1. 线性连续控制系统

这类系统可以用线性微分方程式描述,其一般形式为

$$a _ {0} \frac {\mathrm{d} ^ {n}}{\mathrm{d} t ^ {n}} c (t) + a _ {1} \frac {\mathrm{d} ^ {n - 1}}{\mathrm{d} t ^ {n - 1}} c (t) + \dots + a _ {n - 1} \frac {\mathrm{d}}{\mathrm{d} t} c (t) + a _ {n} c (t)= b _ {0} \frac {\mathrm{d} ^ {m}}{\mathrm{d} t ^ {m}} r (t) + b _ {1} \frac {\mathrm{d} ^ {m - 1}}{\mathrm{d} t ^ {m - 1}} r (t) + \dots + b _ {m - 1} \frac {\mathrm{d}}{\mathrm{d} t} r (t) + b _ {m} r (t)$$

式中， $c(t)$ 是被控量； $r(t)$ 是系统输入量。系数 $a_{0},a_{1},\cdots,a_{n},b_{0},b_{1},\cdots,b_{m}$ 是常数时，称为定常系统；系数 $a_{0},a_{1},\cdots,a_{n},b_{0},b_{1},\cdots,b_{m}$ 随时间变化时，称为时变系统。线性定常连续系统按其输入量的变化规律不同又可分为恒值控制系统、随动系统和程序控制系统。
