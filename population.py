import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")
lat_lon  = pd.read_csv("lat_lon.csv")
top10 = df.head(10)
top10

ct_name = top10["Country (or dependency)"]
top10_pp = top10["Population (2020)"]

title_font = {'family':'serif','color':'blue','size':20}
label_font = {'family':'serif','color':'darkred','size':15}

"""#### 10 đất nước có diện tích lớn nhất thế giới"""

area10 = df[['Country (or dependency)', 'Land Area (Km²)']]
area10.sort_values("Land Area (Km²)", axis = 0,ascending = False, inplace = True)
top10 = area10.head(10)

# area_df = df.copy()
# area_df.sort_values("Land Area (Km²)", axis = 0,ascending = False, inplace = True)
# area_df = area_df.head(10)
top_area = top10["Land Area (Km²)"]
area_name = top10["Country (or dependency)"]

plt.figure(figsize=(15, 8))
plt.bar(area_name, top_area)
plt.title("Top 10 largest countries", fontdict = title_font)
plt.xlabel("Country", fontdict = label_font)
plt.ylabel("Land Area (million)", fontdict = label_font)
ax1 = plt.subplot(1,1,1)
# for y,x in enumerate(top_area):
  # ax1.annotate("{:,}".format(x), xy=(x,y))
for x,y in zip(area_name,top_area):
    label = "{:,}".format(y)
    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points", 
                 xytext=(0,10),
                 ha='center',)
    
plt.show()

"""#### 10 Đất nước có dân số nhiều nhất thế giới"""

plt.figure(figsize=(15, 8))
plt.bar(ct_name, top10_pp)
plt.title("Top 10 most populous countries", fontdict = title_font)
plt.xlabel("Country name", fontdict = label_font)
plt.ylabel("Population (billion)", fontdict = label_font)
ax1 = plt.subplot(1,1,1)
for x,y in zip(ct_name,top10_pp):
    label = "{:,}".format(y)
    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points", 
                 xytext=(0,10),
                 ha='center')
    
plt.show()

"""#### Nước có mật độ dân số đông nhất thế giới """

top1_density = df.loc[df["Density (P/Km²)"].idxmax()]
top1_density["Country (or dependency)"]

top_density = df.loc[df["Density (P/Km²)"].idxmin()]
top_density["Country (or dependency)"]

"""#### Đất nước có tỉ lệ gia tăng dân số tự nhiên lớn nhất"""

top10_change = df['Net Change'].nlargest(n=10)
top10_change



"""#### Chiếm phần trăm dân số thế giới"""

name_population= list(df["Country (or dependency)"].head(10))
worldshare_population= list(df["World Share"].head(10))
labels=[]
for i in name_population:
  labels.append(i)
labels.append("others")
sections=[]
for i in worldshare_population:
  a = float(i[:-1])
  sections.append(a)
sum=0
for i in range (0,len(sections)):
  sum=sum+sections[i]
c=100-sum
sections.append(c)

colors = ['c', 'g', 'y',"orange", "blue", "green", "red", "gray","black", "purple", 'y']

fig, ax = plt.subplots(figsize = (20,12))
ax.pie(sections, labels=labels,colors = colors, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('World Share Percentage of 10 most populated countries and others')
plt.show()