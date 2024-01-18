with open('/Users/ayman/Desktop/Udemy_python/Day 24(Part2): Mail Merge/Input/Letter/starting_letter.txt', mode='r') as file:
    content = file.read()

with open('/Users/ayman/Desktop/Udemy_python/Day 24(Part2): Mail Merge/Input/Names/name.txt', mode='r') as name_file:
    names = name_file.readlines()
    for name in names:
        name = name.strip()
        modified_content = content.replace('[name]', name)
        new_file_name = f"letter_for_{name}.txt"

        with open(f"/Users/ayman/Desktop/Udemy_python/Day 24(Part2): Mail Merge/Output/ReadyToSend/{new_file_name}", mode='w') as new_file:
            new_file.write(modified_content)