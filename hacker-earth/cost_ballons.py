
test_cases = input()
for i in range(int(test_cases)):
    price_ballons = input()
    price_ballons = price_ballons.split(' ')
    ballon_green = int(price_ballons[0])
    ballon_purple = int(price_ballons[1])
    particpants = input()
    total_greeen = 0
    total_purple = 0
    minimum = 0
    aux_min = 0
    for j in range(int(particpants)):
        questions_answered = input()
        questions_answered = questions_answered.split(' ')
        total_greeen += int(questions_answered[0])
        total_purple += int(questions_answered[1])
    tot_a = ballon_green * total_greeen
    tot_b = ballon_purple * total_purple
    minimum = tot_a + tot_b
    tot_a = ballon_green * total_purple
    tot_b = ballon_purple * total_greeen
    aux_min = tot_a + tot_b
    if aux_min < minimum:
        minimum = aux_min
    print(minimum)

