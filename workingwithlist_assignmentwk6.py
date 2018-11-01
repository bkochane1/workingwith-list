course_list =  ["it 402", "it 406" , "it 417","it 460","it 461","it 462"] # 1 list of courses i have taken at walsh
course_list.sort() # 1 sort the list
for course in course_list: # number 2 sort and print each course in uppercase
    print("I have taken " + course.upper() + " at Walsh college")

course_list.append("it 412") # number 3 add classes planned  taken next term
course_list.append("it 419") # number 3 add classes I plan to take next term 

course_list.sort() # number 3 resort the list
print("This is my course of study with upcoming courses added:") #number 3 print a message 
print(course_list)

removed_courses = []
removed_courses.append(course_list.pop(0)) #number 4 remove courses i have already taken and add to the list
removed_courses.append(course_list.pop(0))
removed_courses.append(course_list.pop(1))
removed_courses.append(course_list.pop(2))
removed_courses.append(course_list.pop(2))
removed_courses.append(course_list.pop(2))

print("I do not have to take these courses:") # numer 4 print the courses i dont need to take
for finished in removed_courses:
    print(finished)

print("I plan on taking the next term") # number 5 print courses left plan on taking 
for future_course in course_list: 
    print(future_course) # 5 prints courses remaining in the course list

one_to_thousand_divisible_by_six = list(range(6, 1001, 6)) #number 6 creates a list of numbers divisible by 6
print(one_to_thousand_divisible_by_six)

print("Here are twenty numbers divisible by 6") #  number 7 prints a message twentynumbers numbers divisible by 6
twenty_numbers = one_to_thousand_divisible_by_six[:20] # number 7 takes numbers from a list and prints 20 numbers divisible by 6
for num in twenty_numbers:
    print(num)

max_num = max(one_to_thousand_divisible_by_six) # number 8 finds the maximum number and stores in variable
print("The maximum value in the list is: ") # number 9 finds the maximum number and stores in variable
print(max_num)

sum_num = sum(one_to_thousand_divisible_by_six[9:50]) # number 10 finds sum of values between 10 th and 50th number on the list
print("Here is the sum of several values in the list")
print(sum_num)

course_list = one_to_thousand_divisible_by_six[:] # number 11 copying number list into course list 
print(course_list)




