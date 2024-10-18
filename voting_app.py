# voting_app.py

def cast_vote(candidate):
    votes[candidate] += 1
    print(f"Vote cast for {candidate}. Total votes for {candidate}: {votes[candidate]}")

def show_results():
    print("Election Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

# Dictionary to hold candidate names and their vote counts
votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

# Set to keep track of voters
voters = set()

def main():
    while True:
        voter_id = input("Enter your voter ID: ")
        
        if voter_id in voters:
            print("You have already voted. Thank you!")
            continue

        voters.add(voter_id)

        print("\n1. Cast Vote")
        print("2. Show Results")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            candidate = input("Enter candidate name (Candidate A, Candidate B, Candidate C): ")
            if candidate in votes:
                cast_vote(candidate)
            else:
                print("Invalid candidate.")
        elif choice == '2':
            show_results()
        elif choice == '3':
            print("Exiting the voting app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
