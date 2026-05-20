# END

3.6 Consider the simulation of the indirect self-tuning regulator in Example 3.5. Investigate how the transient behavior of the algorithm depends on the initial values of $\theta$ and P and the forgetting factor.

3.7 Consider the indirect self-tuning regulator in Example 3.5. Make a simulation over longer time periods, and investigate how the parameters approach their true values. Also explore how the convergence rate depends on the forgetting factor $\lambda$ .

3.8 Consider the indirect self-tuning regulator in Example 3.5. Show that no steady-state error is obtained if

$$\hat {a} _ {1} + \hat {a} _ {2} = 1$$

Modify the simulation used to generate Figs. 3.6 and 3.7, plot the parameter combination $\hat{a}_1 + \hat{a}_2$ , and check how well the above condition is satisfied.

3.9 Consider the indirect self-tuning regulator in Example 3.5. Change the specifications on the closed-loop system, and investigate how the behavior of the system changes.

3.10 Consider the indirect self-tuning regulator in Example 3.5. Modify the simulation program so that the parameters of the process can be changed. Investigate experimentally how well the adaptive system can follow reasonable parameter variations.

3.11 Apply the indirect self-tuning regulator in Example 3.5 to a process with the transfer function

$$G (s) = \frac {1}{(s + 1) ^ {2}}$$

Study and explain the behavior of the error when the reference signal is a square wave.

3.12 The code for simulating Example 3.6 is listed below. Study the code and try to understand all the details.

CONTINUOUS SYSTEM reg

"Continuous time STR for the system b/[s(s+a)]

```txt
"Desired response given by am2/(s^2+am1*s+am2)
"Observer polynomial s+ao 
```

```txt
INPUT y ysp
OUTPUT u
STATE yf yf1 uf uf1 xu
STATE th1 th2
STATE p11 p12 p22
DER dyf dyf1 duf duf1 dxu
DER dth1 dth2
DER dp11 dp12 dp22 
```

```lisp
"Filter input and output
dyf=yf1
dyf1=-am1*yf1+am2*(y-yf)
duf=uf1
duf1=-am1*uf1+am2*(u-uf) 
```

```ini
"Update parameter estimate
f1=-yf1
f2=uf
e=dyf1-f1*th1-f2*th2
pf1=p11*f1+p12*f2
pf2=p12*f1+p22*f2
dth1=pf1*e
dth2=pf2*e 
```

```txt
"Update covariance matrix
dp11=alpha*p11-pf1*pf1
dp12=alpha*p12-pf1*pf2
dp22=alpha*p22-pf2*pf2
det=p11*p22-p12*p12 
```

```txt
"Control design
a=th1
b=th2
r1=am1+ao-a
s0=(am2+am1*ao-a*r1)/b
s1=am2*ao/b
t0=am2/b 
```

```txt
"Control signal computation
dxu=-ao*xu-(s1-ao*s0)*y+(ao-r1)*u
v=t0*ysp-s0*y+xu 
```
