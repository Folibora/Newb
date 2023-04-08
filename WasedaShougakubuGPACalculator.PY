aplus = input("Number of credits of A+ you have")
a = input("Number of credits of a you have")
b = input("Number of credits of b you have")
c = input("Number of credits of c you have")
f = input("Number of credits of f you have")

totalcred = float(aplus) + float(a) + float(b) + float(c) + float(f)
GPA = float(((float(aplus)*4) + (float(a)*3) + (float(b)*2) + (float(c)*1) + (float(f)*0))/ totalcred)

print("Your total cred ",totalcred)
print("Your Current GPA is", GPA, "単位落とさないように頑張りましょう！")
