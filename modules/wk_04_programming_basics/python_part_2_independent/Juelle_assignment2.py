### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will grade your submissions myself with this exact script.

# This function takes an input list and an item, and adds the item to the beginning of the list.

Dog_breeds = ["German Sheperd","Pit Bull", "Terrier", "Boxer"]

Disney_movies = ["Alddin", "HSM","Teen Beach", "Tangled","Mulan","Hercules", "HSM"]

def add_to_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    input_list.insert (0,item)

    print("Adding your item to the beginning of the list")

    print(input_list)

    ### YOUR CODE ABOVE HERE ###
    
    return input_list


# This function takes two input lists and combines them.
def merge_lists(list_1, list_2):

    ### YOUR CODE BELOW HERE ###

    new_list = list_1 + list_2

    print("Merging lists now")

    print(new_list)

    ### YOUR CODE ABOVE HERE ###

    return merge_lists


# This function takes an input list and an item, and removes all copies of the item from the list.
def remove_from_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    for i in input_list:

        if i == item:
            input_list.remove(item)

    print("Removing item from list.")

    print (input_list)

    ### YOUR CODE ABOVE HERE ###

    return input_list


# This function takes a numerical grade (e.g. 75.4), and returns True or False depending on whether that grade will earn a B (between 80 and 90)
def check_if_b_grade(grade):

    ### YOUR CODE BELOW HERE ###

    print("Determining if your grade is a B or not ....")

    if grade < 90 and grade > 80:
        print ("True, your grade is a B")

    else:
        print("False, your grade may be above or below a B")


    ### YOUR CODE ABOVE HERE ###

    return check_if_b_grade 


# This function takes a list of RNA codons, and uses a dictionary to return a list of the amino acid translations. If any codon is invalid (aka, not in the dictionary), return an empty list.


    ### YOUR CODE BELOW HERE ###

my_codons = ["UUC","GCC","AAA","GAG"]

fake_codons = ["UUC","GCC","AAA","GOO"]

def get_protein_seq(list_of_codons):

    amino_acid_list = []

    codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    
    for codon in list_of_codons:

        if codon not in codon_dict:  # checks if all codons in the list are valid

            print("There is an invalid codon in your list")
            return []

        amino_acid_list.append(codon_dict[codon])

    print (amino_acid_list)
 
    ### YOUR CODE ABOVE HERE ###

    return amino_acid_list

    

# This function reads in a text file, and counts how many times the word of interest appears.
def count_word_in_file(input_file, word_of_interest):

    ### YOUR CODE BELOW HERE ###

    word_count = 0

    with open (input_file, "r") as file:

        for line in file:                  # iterates over every line in the file but not individual words

            for word in line.split():         # iterates over every word in every line using the split function to split the line into individual words

                if word == word_of_interest:   # this line tells python to check if the word of interest is in the line going word by word
                
                    word_count += 1

    print (f"This word appears {word_count} times in the textfile")


    ### YOUR CODE ABOVE HERE ###

    return


# This function takes a list of 3 column names, and a list of data for each column (each data list is the same length), then outputs a correctly-formatted CSV file "data.csv".

Column_names = ["Name", "Age", "Country"]
Names = ["Juelle", "Bruno", "Nina"]
Ages = [22, 26, 22]
Country = ["St. Lucia" , "Cameroon", "Equatorial Guinea"]

def create_data_file(column_names_list, column1_data, column2_data, column3_data):

    ### YOUR CODE BELOW HERE ###

    if len(column_names_list) != 3:
        print("Error: Must provide exactly 3 column names.")

    with open("data.csv", "w") as file:

        file.write(column_names_list[0] + "," +
                   column_names_list[1] + "," +
                   column_names_list[2] + "\n")
        
        for i in range(len(column1_data)):

            row = str(column1_data[i]) + "," + \
                  str(column2_data[i]) + "," + \
                  str(column3_data[i]) + "\n"
            
            file.write(row)


    print("File 'data.csv' created successfully.")

    ### YOUR CODE ABOVE HERE ###


# This function reads in a CSV file, "file2.csv", and outputs two new files: tav.csv contains ONLY entries with "Tav" as the technician, 
# and andre.csv contains ONLY entries with "Andre" as the technician. Look at file2.csv before writing code!

def filter_data(input_file_csv):


    ### YOUR CODE BELOW HERE ###

    with open(input_file_csv,"r") as fin:
        with open("Andre_file", "w") as outfile_1:
            with open("Tav_file", "w") as outfile_2:

                header = fin.readline()
                outfile_1.write(header)
                outfile_2.write(header)

                for line in fin:

                    columns = line.strip().split(",")
                
                    if columns[3] == "Andre":
                        outfile_1.write(line)

                    elif columns[3] == "Tav":
                        outfile_2.write(line)



    print("Input file information transferred")

    ### YOUR CODE ABOVE HERE ###


### AI Statement: I use AI to figure out how to fix my code for the last 3 functions. I mainly used it to figure out how to fix myloops and how to separate files into lines so that I can iterate over the files by lines. 


### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###


# Calling the add_to_list function and adding Belgian Malinois to the list

# add_to_list(Dog_breeds, "Belgian Malinois")

# Calling the merge_lists function 

# merge_lists(Dog_breeds,Disney_movies)

# Calling remove_from_list function

# remove_from_list(Disney_movies, "HSM")

# Calling check_if_b_grade function

# check_if_b_grade(85.5)
# check_if_b_grade(70.5)
# check_if_b_grade(90.5)

# Calling get_protein_seq function

#get_protein_seq (my_codons)
#get_protein_seq (fake_codons)

# Calling count_word_in_file function

#count_word_in_file ("file1.txt", "And")
#count_word_in_file ("file1.txt", "diverged")
#count_word_in_file ("file2.txt", "cat")

# Calling create_data_file funtion

#create_data_file(Column_names, Names, Ages, Country)

# Calling filter_data function

#filter_data("file2.csv")
