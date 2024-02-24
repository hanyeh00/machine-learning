import pandas as pd

def main():
    x="hello"+str(5)
    dictionary={"name":["Jhon","nour","gatsby"],
                "age":[12,14,24]}
    f=pd.DataFrame(dictionary)
    print(f.columns)
if __name__=="__main__":
    main()