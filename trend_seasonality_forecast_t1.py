import pandas as pd
import numpy as np
import matplotlib.pyplot
import torch
import torch.optim
from torch.utils.data import Dataset, DataLoader
from datetime import date

#loading the dataset
df_1=pd.read_csv("Nat_Gas.csv", parse_dates=["Dates"])
# parse_dates is used to parse the "Dates" as datetime
prices = df_1["Prices"].valies
dates = df_1["Dates"].values

# converting the dtaes to the days                                       
d_s = df_1["Dates"].min()  # d_s refers to the start date
time = np.array([(d-start_date) for d in df_1.["Dates"]])

#GENERAL LINEAR REGRESSION TREND

def lin_reg(x,y):
  x_,y_=np.mean(x),np.mean(y)
  slp= np.sum((x-x_)*(y-y_))/np.sun((x-x_)**2) # slope of the linear pattern
  itcpt= y_ - (slp*x_) # intercept of the line
  return (slp,itcpt)

slp_1,itcpt_1 = lin_reg(time, prices)
lin_tr= slp*time  + intcpt                                                                              


# trignometic regression

sin_time = np.
