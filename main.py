import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

print("==========================================")
print("Welcome TO The World happiness Report ")
print("==========================================")

print("1. Explore Data ")
print("2. Clear Data ")
print("3. Perfirm Data Analysis ")
print("4. Visualization Data ")
print("5. Data Analysis Report ")

choice = int(input("Enter The Number Wetween (1-5) :- "))

print(" Load Data ")

data = input("Enter The File Name Eg(happiness.csv):- ")
data = pd.read_csv(data)
print("Data Loaded Successfully !")

if choice == 1:
    print("=== Explore Data ===")
    print(" ")
    print("1. Top 5 Data Entry ")
    print("2. Last 5 Data Entry ")
    print("3. Information Of Data ")
    print("4. Datatype")
    
    choice = int(input("Enter The Number Between (1-4) :- "))
    
    if choice == 1:
        print(data.head(5))
    elif choice == 2:
        print(data.tail(5)) 
    elif choice == 3 :
        print(data.info())
    elif choice == 4 :
        print(data.dtypes)
    else:
        print("Invalid Choiced Between (1-4) ! ")
elif choice == 2:
    print("=== Clear Data ===")
    print(" ")
    print("1. check Miss Data ")
    print("2. Handal Miss Data   ")
    print("3. Show Dulicate Data  ")
          
    choice = int(input("Enter The Number Between (1-3) :- "))
    
    if choice == 1 :
        d = data.isnull().sum()
        print("Check Miss Data !")
        print(d)
    
 
    elif choice == 2:
        print("=== Handle Miss Data ===")
        print(" ")
        print("1. Delete Miss Data ")
        print("2. Fill Miss Data ")
        
        choice = int(input("Enter The Number Between (1-2) :- "))
        
        if choice == 1 :
            data = data.dropna()
            print("Delete All Missing Data !")
            print(data)
            
        elif choice == 2:
            fill = input("Enter The Word/Number To Fill A Missing Place :- ")
            data = data.fillna(fill)
            print("Filled All Missing Data !")
            print(data)
            
        else:
            print("Invalid Choice between (1-2)")
            
            
    elif choice == 3:
        print(data.duplicated())
        
    else:
        print("Invalid Choice Between (1-3) ! ")      
elif choice == 3 :
    print("=== Data Analysis ===")
    print(" ")
    print("1. Sum Of Happiness Rank ")
    print("2. Sum Of Happiness Score ")
    print("3. Maximun Of Family")
    print("4. Average Of GDP Per Capita ")
    print("5. Average Of Health (Life Expectancy)")
    
    choice = int(input("Enter The Number OF Between (1-5) :- "))
    
    if choice == 1 :
        print(data["Happiness Rank"].sum())
        
    elif choice == 2:
        print(data["Happiness Score"].sum())
        
    elif choice == 3 :
        print(data["Family"].max())
        
    elif choice == 4:
        print(data["Economy (GDP per Capita)"].mean())
        
    elif choice == 5 :
        print(data["Health (Life Expectancy)"].mean())
        
    else:
        print("Invalid Choice Between (1-5) ! ") 
elif choice == 4:
    print("=== Data Visualization ===")
    print(" ")
    print("1. Bar Chat ")
    print("2. Pie chat ")
    print("3. Line Chat")
    print("4. Scatter Chat ")
    print("5. Histogram Chat ")
    
    choice = int(input("Enter The Number Between (1-5) :- "))
    
    if choice == 1 :
        data.head(10).plot.bar(x="Happiness Score",y="Happiness Rank")
        plt.show()
        
    elif choice == 2:
        data.head(10).plot.pie(y="Happiness Score",labels=data["Happiness Rank"])
        plt.show()
    
    elif choice == 3 :
        data.head(10).plot.line(x="Happiness Score",y="Happiness Rank")
        plt.show()
        
    elif choice == 4:
        data.head(10).plot.scatter(x="Happiness Score",y="Happiness Rank")
        plt.show()
        
    elif choice == 5:
        data.head(10).plot.hist(y="Happiness Score")
        plt.show()
        
    else:
        print("Invalid Choice Between (1-5) ! ")       
elif choice == 5:
    print("\n========== HAPPINESS ANALYSIS ==========")
    print("Total Happiness Rank       :", data["Happiness Rank"].sum())
    print("Total Happiness Score      :", round(data["Happiness Score"].sum(), 2))
    print("Maximum Family             :", data["Family"].max())
    print("Average GDP Per Capita     :", round(data["Economy (GDP per Capita)"].mean(), 2))
    print("Average Life Expectancy    :", round(data["Health (Life Expectancy)"].mean(), 2))
    print("\n========== DATASET INFORMATION ==========")
    print("Total Countries            :", len(data))
    print("Total Columns              :", len(data.columns))
    print("Missing Values             :", data.isnull().sum().sum())
    print("Duplicate Records          :", data.duplicated().sum())
    
else:
    print("Invalid Choice Between (1-5) ! ")
    