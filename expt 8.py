T=int(input("Enter the number of credit cards to be tested"))
for _ in range(T):
  cNum=input()
  merge=".join(cNum.split('-'))"
  if cNum[0] in ['4','5','6']:
      if(len(cNum)==16)or(len(cNum)==19 and cNum('-')==3):
          if all([len(each)==4 for each in cNum.split('-')]) or cNum.isdigit():
              if any(merge.count((i*4))>=1 for i in('0123456789')):
                  pass
              else:
                    print("valid")
                    continue
  print("invalid")
