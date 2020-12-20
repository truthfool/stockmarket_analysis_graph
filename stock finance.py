
from pandas_datareader import data
import datetime 
from bokeh.plotting import figure,show,output_file 

start=datetime.datetime(2019,3,1)
end=datetime.datetime(2019,4,10)
df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)
def inc_dec(o,c):
    if o>c:
        return "Decrease"
    elif c>o:
        return "Increase"
    else:
        return "Equal"
    

df["Status"]=[inc_dec(o,c) for o,c in zip(df.Open,df.Close)]
df["Height"]=abs(df.Open-df.Close)
df["Middle"]=(df.Open+df.Close)/2

p=figure(x_axis_type='datetime',plot_width=1000,plot_height=300,sizing_mode="scale_width")

p.title.text="Stock Graph"
p.grid.grid_line_alpha=0.4

width_h=12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,color="black")
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],width_h,df.Height,fill_color="#CCFFFF",line_color="black")
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],width_h,df.Height,fill_color="#FF3333",line_color="black")


output_file("Stock_Data.html")

show(p)

