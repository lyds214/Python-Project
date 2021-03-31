#Lydia Yang and Michael Nguyen

#In case if the user enters a DNA sequence that has white space,
#we removed it to prevent any errors.
def remove_white_space_and_capitalize(sequence):
    sequence = sequence.strip()
    sequence = sequence.upper()
    return sequence


#This prints the main menu of DNA Sequence program.
def print_menu():
    print("Main Menu")
    print("1. Insert an indel")
    print("2. Remove an indel")
    print("3. Score similarity")
    print("4. Suggest indel")
    print("5. Quit")


#This function is to check to see if the user's input is 1, 2, 3, or, 5
#since there are only five options in the main menu. It'll continually ask
#the user if they input a number that's not within the range.
def get_menu_choice():
    user_input = float(input("Please choose an option: "))
    
    while (user_input <= 0 or user_input > 5) or (user_input != int(user_input)):
        user_input = float(input("Please choose an option: "))
    return user_input


#This function is to check to see if the user's input is 1 or 2 since there are
#only two DNA sequences that the user will input at the beginning of the program.
#It'll continually ask the user if they input a number that's not 1 or 2.
def get_sequence_number():
    user_input = float(input("Sequence 1 or 2? "))

    while user_input != 1 and user_input != 2:
        user_input = float(input("Sequence 1 or 2? "))
    return user_input

#This function gets the position of a DNA sequence so that an indel can be inserted
#at that position. It'll continually ask the user to input a number that's within
#the length of a DNA sequence plus 1.
def get_insert_position(sequence):
    dna_length = len(sequence) + 1
    user_input = float(input("Please choose a position: "))
    
    while (user_input <= 0 or user_input > dna_length) or (user_input != int(user_input)):
        user_input = float(input("Please choose a position: "))
    return user_input

#This function gets the position of a DNA sequence of where the user wants an indel
#to be removed. It'll continually ask the user to input a number that's within the length
#of the DNA sequence.
def get_remove_position(sequence):
    dna_length = len(sequence)
    user_input = float(input("Please choose a position: "))
    
    while (user_input <= 0 or user_input > dna_length) or ((sequence[int(user_input - 1)] != "-")):
        user_input = float(input("Please choose a position: "))
    return user_input

#This function removes an indel of a DNA sequence.
def remove_indel(sequence, index):
    return sequence[:int(index)] + sequence[int(index + 1):]

#This function inserts an indel of the DNA sequences if the inputted DNA sequences differ in length.
def pad_with_indels(sequence, num):
    sequence += "-" * num
    return sequence

#This function inserts an indel of a DNA sequence.
def insert_indel(sequence, index):
    return sequence[:int(index)] + "-" + sequence[int(index):]

#This function counts the number of matching nucleotides.
def count_matches(sequence1, sequence2):
    counter = 0

    for x in range(min(len(sequence1), len(sequence2))):
        if (sequence1[x].lower() == sequence2[x].lower()) and (sequence1[x] != "-"):
            counter += 1
    return counter      

#This function lowers each nucleotides for both of the DNA sequences if the matching nucleotide
#are int the same position. The nucleotides would be capitalized if they're different.
def lower_sequence(sequence1, sequence2):
    lower_user1 = ""
    lower_user2 = ""
    
    for x in range(len(sequence1)):
        if sequence1[x].lower() == sequence2[x].lower():
            lower_user1 += sequence1[x].lower()
            lower_user2 += sequence2[x].lower()

        else:
            lower_user1 += sequence1[x].upper()
            lower_user2 += sequence2[x].upper()
            
    sequence1 = lower_user1
    sequence2 = lower_user2

    return [sequence1, sequence2]
#This function finds the optimal position by inserting an indel to every position to find which position 
#will maximize the amount of similarities between the DNA sequences. The function inserts an indel in every 
#position and checks the similarity between them and removes the previous indel when it moves on to the next 
#position.
def find_optimal_indel_position(sequence, other_sequence):
    position = 0
    MAX = -1

    for x in range(len(sequence)):
        sequence = insert_indel(sequence, x)
        counter = count_matches(sequence, other_sequence)
        sequence = remove_indel(sequence, x)

        if counter > MAX:
            MAX = counter
            position = x 
    
    return position
 


if __name__ == "__main__":
    

    #User inputs 2 DNA sequences
    user_input1 = input("Please enter DNA Sequence 1: ")
    user_input2 = input("Please enter DNA Sequence 2: ")

    #Removes leading and trailing whitespace.
    user_input1 = remove_white_space_and_capitalize(user_input1)
    user_input2 = remove_white_space_and_capitalize(user_input2)

    #Compares the length of the sequences and adds indels for the shorter sequence.
    if len(user_input1) < len(user_input2):
        user_input1 = pad_with_indels(user_input1, len(user_input2) - len(user_input1))

    else:
        user_input2 = pad_with_indels(user_input2, len(user_input1) - len(user_input2))

    
    #Returns the elements with capital and lowercase DNA sequences.
    lower_list = lower_sequence(user_input1, user_input2)
    user_input1 = lower_list[0]
    user_input2 = lower_list[1]

    #Prints out the compared DNA sequences
    print(f"\nSequence 1:", user_input1)
    print(f"Sequence 2:", user_input2)
    print()

    #Program will continue to run until the user enters 5 when asked to input a main menu choice.
    sentinel = 5
    
    while sentinel == 5:
        print_menu()
        print()
        choice = get_menu_choice()

        #Insert an indel (option 1)
        if choice == 1:
            ask_sequence = get_sequence_number()

            #Inserts an indel for Sequence 1
            if ask_sequence == 1:
                ask_position = get_insert_position(user_input1)
                user_input1 = insert_indel(user_input1, ask_position - 1)
                user_input2 += "-"
                
                lower_list = lower_sequence(user_input1, user_input2)
                user_input1 = lower_list[0]
                user_input2 = lower_list[1]
                
                print(f"\nSequence 1: {user_input1}")
                print(f"Sequence 2: {user_input2}")

            #Inserts an indel for Sequence 2
            if ask_sequence == 2:
                ask_position = get_insert_position(user_input2)
                user_input2 = insert_indel(user_input2, ask_position - 1)
                user_input1 += "-"
                
                lower_list = lower_sequence(user_input1, user_input2)
                user_input1 = lower_list[0]
                user_input2 = lower_list[1]
                
                print(f"\nSequence 1: {user_input1}")
                print(f"Sequence 2: {user_input2}")
                
        #Remove an indel (option 2)
        if choice == 2:
            ask_sequence = get_sequence_number()

            #DNA Sequence 1
            if ask_sequence == 1:
                ask_position = get_remove_position(user_input1)
                user_input1 = remove_indel(user_input1, ask_position - 1)

                #If other string has an indel at the end, remove it.
                if user_input2[-1] == "-":
                    user_input2 = remove_indel(user_input2, len(user_input2) - 1)

                    lower_list = lower_sequence(user_input1, user_input2)
                    user_input1 = lower_list[0]
                    user_input2 = lower_list[1]
                    
                    print("\nSequence 1:", user_input1) 
                    print("Sequence 2:", user_input2)

                #If other string doesn't have an indel at the end, insert the indel at end of the string
                #that has its indel removed.
                else:
                    user_input1 = insert_indel(user_input1, len(user_input1) + 1)

                    lower_list = lower_sequence(user_input1, user_input2)
                    user_input1 = lower_list[0]
                    user_input2 = lower_list[1]
                    
                    print("\nSequence 1:", user_input1)
                    print("Sequence 2:", user_input2)

            #DNA Seqeunce 2
            if ask_sequence == 2:
                ask_position = get_remove_position(user_input2)
                user_input2 = remove_indel(user_input2, ask_position - 1)

                #If other string has an indel at the end, remove it.
                if user_input1[-1] == "-":
                    user_input1 = remove_indel(user_input1, len(user_input1) - 1)

                    lower_list = lower_sequence(user_input1, user_input2)
                    user_input1 = lower_list[0]
                    user_input2 = lower_list[1]
                    
                    print("\nSequence 1:", user_input1)
                    print("Sequence 2:", user_input2)

                #If other string doesn't have an indel at the end, insert the indel at end of the string
                #that has its indel removed.
                else:
                    user_input2 = insert_indel(user_input2, len(user_input2) + 1)

                    lower_list = lower_sequence(user_input1, user_input2)
                    user_input1 = lower_list[0]
                    user_input2 = lower_list[1]
                    
                    print("\nSequence 1:", user_input1)
                    print("Sequence 2:", user_input2)


        #Score similarity (option 3)
        if choice == 3:
        
            #Prints out the number of matches and mismatches; calculated the match rate by percentange.
            not_matches = min(len(user_input1), len(user_input2)) - count_matches(user_input1, user_input2)

            print("\nSimilarity:", count_matches(user_input1, user_input2), "matches,", end = ' ')
            print(not_matches, "mismatches.", end = ' ')
            print('{:.1f}%'.format(((count_matches(user_input1, user_input2) / len(user_input1)) * 100)), "match rate.")
            print("\nSequence 1:", user_input1)
            print("Sequence 2:", user_input2)

        #Suggest indel (option 4)
        if choice == 4:
            ask_sequence = get_sequence_number()

            #Sequence 1
            if ask_sequence == 1:
                optimal_position = find_optimal_indel_position(user_input1, user_input2)
                user_input1 = insert_indel(user_input1, optimal_position)
                user_input2 += "-"
                matching_sequence = count_matches(user_input1, user_input2) 
                
                print("Insert an indel into Sequence 1 at position", optimal_position + 1, ".")
                
                not_matches = min(len(user_input1), len(user_input2)) - count_matches(user_input1, user_input2)
                
                print("\nSimilarity:", count_matches(user_input1, user_input2), "matches,", end = ' ')
                print(not_matches, "mismatches.", end = ' ')
                print('{:.1f}%'.format(((count_matches(user_input1, user_input2) / len(user_input1)) * 100)), "match rate.")

                user_input1 = remove_indel(user_input1, optimal_position)
                user_input2 = remove_indel(user_input2, len(user_input2) - 1)
                
                print("Sequence 1: ", user_input1)
                print("Sequence 2: ", user_input2)

            #Sequence 2
            if ask_sequence == 2:
                optimal_position = find_optimal_indel_position(user_input2, user_input1)
                user_input2 = insert_indel(user_input2, optimal_position)
                user_input1 += "-"
                matching_sequence = count_matches(user_input1, user_input2) 
                
                print("Insert an indel into Sequence 2 at position", optimal_position + 1, ".")
                
                not_matches = min(len(user_input1), len(user_input2)) - count_matches(user_input1, user_input2)
                
                print("Similarity:", count_matches(user_input1, user_input2), "matches,", end = ' ')
                print(not_matches, "mismatches.", end = ' ')
                print('{:.1f}%'.format(((count_matches(user_input1, user_input2) / len(user_input1)) * 100)), "match rate.")

                user_input1 = remove_indel(user_input1, len(user_input1) - 1)
                user_input2 = remove_indel(user_input2, optimal_position)
                
                print("\nSequence 1:", user_input1)
                print("Sequence 2:", user_input2)

            
        #Quit
        if choice == 5:
            quit()
