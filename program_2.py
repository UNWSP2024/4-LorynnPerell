# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    num_movies = int(input("How many movies do you want to enter? "))
    total_tickets = 0

    for i in range (num_movies):
        movie=input(f"Enter the name of movie #{i+1}: ")
        tickets = int(input(f"How many tickets for {movie}? "))
        total_tickets += tickets

    print(f"\nTotal tickets desired: {total_tickets}")
    ######################


if __name__ == '__main__':
    main()