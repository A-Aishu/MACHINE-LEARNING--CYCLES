str = "Sathyabama 2019 @"
alp = dig = spcl = lc = uc =0
for i in range(len(str)):
    if(str[i].isalpha()):
        alp = alp + 1
        if(str[i]>='a' and str[i]<='z'):
            lc = lc + 1
        elif(str[i]>='A' and str[i]<='Z'):
            uc = uc + 1
    elif(str[i].isdigit()):
        dig = dig + 1
    else:
        spcl = spcl + 1
        if(str[i]== ''):
            spcl = spcl - 1
print("Digits:{0} Alphabets:{1} Special Characers:{2} Lowercase:{3} Uppercase{4}". format(dig,alp,spcl,lc,uc))
