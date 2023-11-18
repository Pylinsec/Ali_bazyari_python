#  string --> harch  ke bin ''--> single quotation  "" double quotation
name = 'Ali Bazyari'
print(type(name)) # tashkhis no dadeh
#--------------- len() --> length --> tool sakhteman dadeh bermigardand
length_name = len(name)
print(f"tool name is {length_name} character")
#
#  membership operator in , not in , identity operator  is , is not
sentence = "If you want to live a happy life, tie it to a goal, not to people or things."
print(len(sentence)) # tool jomleh
print('tie' in sentence) # > agar bood true barmigardanad
print('live' not in sentence) # --> agar nebood True barmigardand
print(sentence is sentence) # agar eine ham boodan true 
print(name is not sentence) # agar moshabeh nebood True 