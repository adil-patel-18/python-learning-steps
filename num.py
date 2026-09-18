# 🟢 NumPy Basic Practice

#**Q1.** NumPy import karke ek 1D array banao:
#[10, 20, 30, 40, 50]
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)

#Q2. Ek NumPy array ke saare elements print karo.
arr=np.array([10,20,30,40,50])
print(arr)

#Q3. Array ka **size** find karo.
print(arr.size)

#Q4. Array ka **shape** find karo.
print(arr.shape)

#Q5. Array ka **data type (`dtype`)** print karo.
print(arr.dtype)

#Q6. `0` se `10` tak numbers ka NumPy array banao.
arr1=np.arange(0,11)
print(arr1)

#Q7. `1` se `20` tak even numbers ka array banao.
arr1=np.arange(2,21,2)
print(arr1)

#Q8. Ek array ke elements ka **sum** find karo.
arr1=np.arange(1,11)
print(arr1.sum())

#Q9. Array ka **maximum** aur **minimum** value find karo.
arr1=np.arange(1,11)
print(arr1.max())
print(arr1.min())

#Q10. Array ka **mean (average)** find karo.
arr1=np.arange(1,11)
print(arr1.mean())
'''
### 🟡 Array Practice

**Q11.** `[1,2,3,4,5]` ko reverse karo.

**Q12.** Array mein har element ko `2` se multiply karo.

**Q13.** Array ke har element mein `10` add karo.

**Q14.** Do NumPy arrays ko add karo.

**Q15.** Do NumPy arrays ko multiply karo.

**Q16.** 10 random numbers ka NumPy array generate karo.

**Q17.** `3 × 3` matrix banao:

```text
1 2 3
4 5 6
7 8 9
```

**Q18.** Matrix ki **rows aur columns** find karo.

**Q19.** Matrix ka **transpose** find karo.

**Q20.** Matrix mein se second row aur second column print karo.

**Q21.** NumPy array mein `25` value present hai ya nahi, check karo.

**Q22.** Array mein even numbers filter karo.

**Q23.** Array ko ascending order mein sort karo.

**Q24.** Array ko descending order mein sort karo.

**Q25.** Array mein duplicate values remove karo.

Pehle **Q1–Q10** solve karo. Tum code bhejna, main **marks + correction** dunga.
'''