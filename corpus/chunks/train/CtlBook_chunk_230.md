# 2.) The s is a transfer function Trick

Python control transfer function objects are quite smart and they can be added, subtracted, multiplied, and divided with each other and with constants. Plain old s could be a transfer function so in fact we can build up interesing transfer functions using it as follows:

```python
s = ctl.TransferFunction.s # official way to create LaPlace 's'
num = 1.0E5*(s+20)
den = (s+500)*(s+3000)*(s*s + 4*s + 32)
system = num/den # note use of division for numerator and demoniator 
```

Since s is already a ctl.TransferFunction() (from the rst line), then the variable system is as well(!)
