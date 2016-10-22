Binary Division

```

When our divisor has a decimal point, we can shift it along on both sides until it has gone.


     _________
11.1|10010.011

becomes

     _________
 111|100100.11
 
 36.75/7
 
 
 ---
 Use the same 4 steps as Long Division

1. Is 111 greater than 1? Yes, we put a 0 as the result
2. 111 x 0 = 0
3. 1 - 0 = 1
4. Bring next down!

     0________
 111|100100.11
     0
     ---------
     10
     
---

1. Is 111 greater than 10? Yes, we put a 0 as the result
2. 111 x 0 = 0
3. 10 - 0 = 0
4. Bring next down!

     00_______
 111|100100.11
     0
     ---------
     10
     -0
     --------
     100
---


1. Is 111 greater than 100? Yes, we put a 0 as the result
2. 111 x 0 = 0
3. 100 - 0 = 0
4. Bring next down!

     00_______
 111|100100.11
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
---

1. Is 111 greater than 1001? Nope, we put a 1 as the result
2. 111 x 1 = 101
3. 1001 - 101 = 1001 + 10110 = (1)1111 (ignore extra bit)
4. Bring next down!

     0001_____
 111|100100.11
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
    +1001
     --------
  (1)11110     

---
1. Is 111 greater than 100? Yup, we put a 0 as the result.
2. 111 x 0 = 0
3. 100 - 0 = 0
4. Bring next down!

     00010____ 
 111|100100.11 
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
    +1001
     --------
       100
     -   0
     --------
       1000
       
---

1. Is 111 greater than 1000? Nope, we put a 1 as the result.
2. 111 x 1 = 111
3. 1000 - 111 =  1000 + 1001
4. Bring next down!

     000101.__ 
 101|100100.11 
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
    +1001
     --------
       100
     -   0
     --------
       1000
     + 1001
     ---------
    (1)00011
    
    
---

1. Is 111 greater than 11? Yep, we put a 0 as the result.
2. 111 x 0 = 0
3. 11 - 0 =  11
4. Bring next down!

     000101.0_ 
 101|100100.11 
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
    +1001
     --------
       100
     -   0
     --------
       1000
     + 1001
     ---------
    (1)00011
      -    0
      ---------
           111
           
---

1. Is 111 greater than 111? They are equal! So we add a 1
2. 111 x 1 = 111
3. 111 - 111 =  111 + 1001 = 10000
4. Bring next down!

     000101.01 
 101|100100.11 
     0
     ---------
     10
     -0
     --------
     100
     - 0
     --------
     1001
    +1001
     --------
       100
     -   0
     --------
       1000
     + 1001
     ---------
    (1)00011
      -    0
      ---------
           111
          -111
          -----
        (1)000
        
        
Answer: 101.01 (5.25)

```


