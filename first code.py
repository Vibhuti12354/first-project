
#%%
file="demo.txt"
word="hello"
c=0
with open(file,'r')as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
               c=c+1
print("occurence of word",word)
print(c)


# %%
