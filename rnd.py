word_count={}
with open("textfile.txt", "r") as file:
    all_lines = file.readlines()
    
    for lines in all_lines:
        words = lines.strip().split('e')
        for word in words:

            if word in word_count:
                word_count[word] += 1
                
            else: 
                word_count[word] = 1
            
            

for word, numbers in word_count.items():
    print(f"{word} = {numbers}")


