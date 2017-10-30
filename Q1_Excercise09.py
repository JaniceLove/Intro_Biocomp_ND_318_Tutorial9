#Exercise 9
#Authors: Janice Love and Melissa Stephens

#Load data and import packages
import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *

#need to populate dataframe with existing data
MyDataFrame=pandas.read_csv("ponzr1.csv",sep=",",header=0)

#make 3 data frames with the control and treatment we are interested in. Initialize x=0
#designate treatment group as x=1, and x=0 for control group

Var1=MyDataFrame.loc[MyDataFrame.mutation.isin(["WT","M124K"]),:]
Var2=pandas.DataFrame({'y':Var1.ponzr1Counts,'x':0})
Var2.loc[Var1.mutation=="M124K","x"]=1
print Var2
Var3=MyDataFrame.loc[MyDataFrame.mutation.isin(["WT","V456D"]),:]
Var4=pandas.DataFrame({'y':Var3.ponzr1Counts,'x':0})
Var4.loc[Var3.mutation=="V456D","x"]=1
print Var4
Var5=MyDataFrame.loc[MyDataFrame.mutation.isin(["WT","I213N"]),:]
Var6=pandas.DataFrame({'y':Var5.ponzr1Counts,'x':0})
Var6.loc[Var5.mutation=="I213N","x"]=1
print Var6