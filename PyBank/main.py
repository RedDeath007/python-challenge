#importing os and csv
import os
import csv


#reading the file
budget = os.path.join("Resources/budget_data.csv")
#budget = os.path.join("/Users/dylan/Documents/Data_Analytics/Module_Challenges/Module3/python-challenge/PyBank/Resources/budget_data.csv")
budget_output = os.path.join("analysis/budget_analysis.txt")

#variable
total_months = 0
total = 0
change_list = []
month_list = []
change = 0
change_count = 0
stored_change = 0
max_prof = 0
min_loss = 0
prof_month = 0
loss_month = 0
    

with open(budget, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)



#loop for total months and total, and append row[1] to list
    
    for row in csvreader:
        total_months = total_months + 1
        total = total + int(row[1])
        change_list.append(row[1])
        month_list.append(row[0])

#loop for changes in each month
    
    for i in range(1,len(change_list)):
        #changes per month
        change = int(change_list[i]) - int(change_list[i-1])
        change_count = change_count + 1 
        #overall change
        stored_change = stored_change + change
        
        #is it maximum profit per month
        if change > max_prof:
            max_prof = change
            prof_month = month_list[i]
        #is it maximum loss per month
        if change < min_loss:
            min_loss = change
            loss_month = month_list[i]

    

    #average change per month
    avg_change = round(stored_change/change_count, 2)
       
 
output = (f'Financial Analysis \n'
f'---------------------------- \n'
          
f'Total Months:  {total_months} \n'
f'Total:  {total}\n'
f'Average change:   {avg_change}\n'
f'Greatest Increase in profit:  {prof_month},  {max_prof}\n'
f'Greatest Decrease in profit: {loss_month} , {min_loss}')

print(output)

with open(budget_output, "w") as txtfile:
    txtfile.write(output)