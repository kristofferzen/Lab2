def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {round(bmi, 2)}")

    # Return categories based on BMI
    if bmi < 18.5:
        return -1  # underweight
    elif 18.5 <= bmi < 24.9:
        return 0   # normal weight
    else:
        return 1   # overweight
    

calculate_bmi(weight=57,height=1.73)
print("BMI Category Code:", result)



#5.5 git commit -m "Initial version to display text message on console"
#5.6 git remote add origin https://github.com/kristofferzen/Lab2.git
# git remote -v
#git push --set-upstream origin master

#1b) TypeError: can only concatenate str (not "float") to str because the str converts the height and weight into strings