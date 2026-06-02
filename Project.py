import numpy as np
import matplotlib.pyplot as plt
#Assets names
assets_name=np.array([
    "Gold",
    "Silver",
    "Oil",
    "Wheat"
])

#Assets current value in US dollar
assets= np.array([
   4500,  #Gold in $
   76,    #Silver in $
   96,    #Oil in $
   6,     #wheat in $
])
price_history=[assets.copy()]
  
#Impact on assets due to different economic events
#We will deal with three events
#1.Inflation 
#2.Recession
#3.War

#Impact of inflation
def inflation(prices):
    prices[0] *=1.10
    prices[2] *=1.08
    return prices

#Impact of Recession
def recession(prices):
    prices[1] *=0.90
    prices[2] *=0.85
    return prices

#Impact of war
def war(prices):
    prices[0] *=1.20
    prices[2] *=1.25
    return prices

#Finally calculating the overall impact on assets due to various events
for day in range(365):
    #Normal day movement    
    daily_return=np.random.normal(
    loc=0.001,
    scale=0.02,
    size=4)
    assets=assets*(1+daily_return)

    event=np.random.random()

    #Crisis day
    if event<0.03:
        print(f"Day {day}: Inflation Crisis")
        assets=inflation(assets)
    elif event<0.05:
        print(f"Day {day}: Recession Crisis") 
        assets=recession(assets) 
    elif event<0.06:
        print(f"Day {day}: War Crisis")  
        assets=war(assets) 

    #Saving the finall price
    price_history.append(assets.copy()) 
price_history=np.array(price_history) 

#Calculate growth 
initial = price_history[0]
final = price_history[-1]
growth = ((final-initial)/initial)*100

#Better representation of outcome
for name,start,end,g in zip(
    assets_name,
    initial,
    final,
    growth):
    print(
        f"{name}: "
        f"${start:.2f} -> ${end:.2f}"
        f"({g:.2f}%)"
 )
    
#Graphical representation
plt.figure(figsize=(10, 6))
#Gold
plt.subplot(2, 2, 1)
plt.plot(price_history[:, 0])
plt.title("Gold")
plt.grid()
#Silver
plt.subplot(2, 2, 2)
plt.plot(price_history[:, 1])
plt.title("Silver")
plt.grid()
#Oil
plt.subplot(2, 2, 3)
plt.plot(price_history[:, 2])
plt.title("Oil")
plt.grid()
#Wheat
plt.subplot(2, 2, 4)
plt.plot(price_history[:, 3])
plt.title("Wheat")
plt.grid()
plt.tight_layout()
plt.show()  
     
