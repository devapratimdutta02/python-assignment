file1 = open("class_score.txt", "r")
read_content = file1.readlines()
file1.close()

new_content = []

for line in read_content:
    if line.strip():
        parts=line.split()
        if len(parts)==2:
            username, score = parts
            new_score = int(score) + 5
            new_content.append(f"{username} {new_score}\n")

file2 = open("class_score_2.txt", "w")
file2.writelines(new_content)
file2.close()
