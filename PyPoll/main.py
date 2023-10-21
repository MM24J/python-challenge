# Import os module
import os

#Import CSV module to read file
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Define variables
total_votes = 0
candidate_votes = {}
candidate_list = []
vote_count = []
percent_won_list = []
winner = ""
winner_vote_count = 0
cleaned_output = []

#Read CSV file

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    #Loop through each row in CSV file
    
    for row in csvreader:

        #Count the total number of votes
        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name in candidate_list:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1

    #Loop through each candidate and get percentage of votes won by each candidate

    for key, value in candidate_votes.items():
        vote_count.append(value)
        votes = candidate_votes[candidate_name]
        percent_won = round((int(value)/total_votes * 100),2)
        percent_won_list.append(percent_won)

    #Find the winner with the highest vote total
        if (value > winner_vote_count):
            winner_vote_count = value
            winner=key

    #Create list to print
    cleaned_output = zip(candidate_list, percent_won_list, vote_count)
    cleaned_output = list(cleaned_output)

    #Display results in terminal
    print()
    print("Election Results")    
    print()
    print("-----------------------")
    print()
    print(f"Total Votes:", f"{total_votes}")
    print()
    print("-----------------------")
    print()
    for item in cleaned_output:
       print(f"{item[0]}: {item[1]}% ({item[2]})")
    print()
    print("------------------------")
    print()
    print(f"Winner: {winner}")
    print()
    print("------------------------")
    print()

# Create a text file
output_path = os.path.join("analysis", "pypoll_results.csv")
with open(output_path, "w", newline = "") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",")

#Display Results

    csvwriter.writerow(["Election Results"])

    csvwriter.writerow(["-----------------------"])

    csvwriter.writerow([f"Total Votes: " f"{total_votes}"])

    

    for item in cleaned_output:
        csvwriter.writerow([f"{item[0]}: " f"{item[1]}% ({item[2]})"])

    csvwriter.writerow(["-----------------------"])

    csvwriter.writerow([f"Winner: " f"{winner}"])

    csvwriter.writerow(["-----------------------"])





    


