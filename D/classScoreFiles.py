file1 = open("C:/Users/ccsad/OneDrive/Desktop/Documents/D/class_score.txt", "r")
read_content = file1.readlines()
file1.close()

new_content = []

for line in read_content:
    username, score = line.split()
    new_score = int(score) + 5
    new_content.append(f"{username} {new_score}\n")

file2 = open("C:/Users/ccsad/OneDrive/Desktop/Documents/D/class_score_2.txt", "w")
file2.writelines(new_content)
file2.close()
