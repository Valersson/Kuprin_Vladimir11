<<<<<<< HEAD
#duration
duration = int(input())
minutes = 0
hours = 0
days = 0
for i in range (1; duration):
    if i / 60 >= 1:
        minutes += 1
    if i / 360 >= 1:
        hours += 1
    if i / 8640 >= 1:
        days += 1
print(minutes, hours, days)

#=======
#def convert_time(duration: int) -> str:
#    return


#duration = 400153
#result = convert_time(duration)
#print(result)
#>>>>>>> origin/Vladimir_Kuprin_lesson_1
