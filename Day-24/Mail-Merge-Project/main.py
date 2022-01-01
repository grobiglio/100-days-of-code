#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

starting_letter = './Input/Letters/starting_letter.txt'
with open(starting_letter) as f:
    example_letter = f.read()

invited_names = './Input/Names/invited_names.txt'
with open(invited_names) as inv:
    for line in inv:
        name = line.strip()
        personal_letter = example_letter.replace('[name]',name)
        personal_file_name = './Output/ReadyToSend/'+name+'.txt'
        with open(personal_file_name, mode='w') as pf:
            pf.write(personal_letter)
