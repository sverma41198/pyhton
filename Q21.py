data={
    "priya": {
          "location" : "Hyderabad",
          "joining_date ": "05/09/2022"
    },
    "mahi": {
          "location" : "Bangalore",
          "joining_date ": "20/02/2023"
    },
    "raja": {
          "location" : "Hyderabad",
          "joining_date ": "14/10/2022"
    },
    "prabhu": {
          "location" : "Bangalore",
          "joining_date ": "02/01/2023"
    }
  }
# print(len(employee_data))

for i in data:
    d,m,y=map(int,data[i]["joining_date "].split("/"))
    if y==2022 and data[i]["location"]=="Hyderabad" :
        if  m>=9 and d>2:
            print(i)
    elif y==2023 and data[i]["location"]=="Hyderabad":
        print(i)