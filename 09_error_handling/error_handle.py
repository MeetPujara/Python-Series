file = open('youtube.txt','w')

# Two ways to write things in file

# 1st Way: Here You Have to Close The File Compulsory
# try:
#     file.write("Chai  Aur Code")
# finally:
#     file.close()
    
# 2nd Way: "With Statement" and No Need To Close The File

with open('youtube.txt','w') as file:
    file.write("Chai Aur Python")