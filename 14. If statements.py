is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male!")
elif not(is_male) and is_tall:
    print("You are a not a male but you are tall")
else:  # jeśl nie, wykona się to
    print("You are neither a male or tall")

# if is_male:  # jeśli warunek jest true, kod sie wykona
# if\or\and
# else
# elif - else if - taki pythonowy skrót
# not(zmienna) - if false
