list1=[2452817, 1480429, 3230001, 3138371, 843447]
outFile = open('outfile.txt', 'w')
user_likes={123423:[456,45645,4564],345335:[345,34435,223423]}
for n_user in list1:
    temp_list=user_likes.keys()
    temp = list(temp_list)
    user_id=temp[n_user]
    for item_id in user_likes[user_id]:
        outFile.write(str(item_id) + ' ' + str(user_id) + '\n')

outFile.close()