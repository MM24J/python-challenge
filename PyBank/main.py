#Import os module
import os

#Import CSV module to read file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Define variables
total_months = 0
total = total_months = change = greatest_increase = greatest_decrease = 0
greatest_increase_month = greatest_decrease_month = ("")
data = []

#Read CSV file

with open(csvpath) as csvfile:

    #Specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        
    print(csvreader)

    #Read header row first
    csv_header = next(csvreader)
    

    #Loop through each row in CSV file
    
    for row in csvreader:
        
        #Count the total number of months
        total_months += 1
        
        #Calculate the total
        total = int(total) + int(row[1])

        data.append(row)
    
    
    #Loop through the list and get the monthly change
    for i in range(len(data)-1):
        monthly_change = int((data)[i + 1][1]) - int((data)[i][1])

        #Find the greatest increase and decrease in profits
        if greatest_increase < monthly_change:
            greatest_increase = monthly_change
            greatest_increase_month = data[i + 1][0]

        if greatest_decrease > monthly_change:
            greatest_decrease = monthly_change
            greatest_decrease_month = data[i + 1][0]

        #Calculate the average change over the entire period
        average_change = round((int((data)[-1][1]) - int((data)[0][1])) / (len(data)-1),2)



#Create a text file
   
output_path = os.path.join("analysis", "pybank_results.csv")
with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",") 

#Display Results

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["--------------------------"]) 

    csvwriter.writerow([f"Total Months: " f"{total_months}"])

    csvwriter.writerow([f"Total: " f"${total}"])

    csvwriter.writerow([f"Average Change: " f"${average_change}"])

    csvwriter.writerow([f"Greatest Increase in Profits: " f"{greatest_increase_month} (${greatest_increase})"])

    csvwriter.writerow([f"Greatest Decrease in Profits: " f"{greatest_decrease_month} (${greatest_decrease})"])

#Print Analysis to Terminal

print()
print("Financial Analysis")

print()

print("-----------------------")

print()



print(f"Total Months: " f"{total_months}")
print()

print(f"Total: " f"${total}")
print()
    
print(f"Average Change: " f"${average_change}")

print()

print(f"Greatest Increase in Profits: " f"{greatest_increase_month} (${greatest_increase})")
print()
print(f"Greatest Decrease in Profits: " f"{greatest_decrease_month} (${greatest_decrease})") 
print()           
    





    


