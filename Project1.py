f = open("Github projects\pi.txt", "r")
data = f.read().replace("\n", "")

counter = 0

for i in range(len(data) - 1):
    fragment = int(data[i] + data[i+1])

    if fragment > 90:
        counter+=1


print("liczba fragmentów większych od 90:", counter)
