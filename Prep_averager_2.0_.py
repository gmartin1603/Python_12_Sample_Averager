trace = True
while True:
    #counter that flags claculation at 12
    number = 0
    #the average moisture
    m_average = 0
    #the average temperature
    t_average = 0

    #list of inputs to get averaged
    m_values = []
    t_values = []
    #allows input of moistuer and temp for each sample
    while number < 12:
        moist = input('Enter the moisture: ')
        #hitting enter bypasses the sample time w/o effecting average
        if moist == '':
            number += 1
            continue

        else:
            moist = float(moist)
            moist = m_values.append(moist) #adds each value to the list to be averaged


        temp = input('Enter the temperature: ')
        if temp == '':
            continue
        else:
            temp = int(temp)
            temp = t_values.append(temp)
            number += 1


    #equations for average after number = 12
    divisor = len(m_values)
    m_total = sum(m_values)
    m_average = m_total / divisor

    divisor = len(t_values)
    t_total = sum(t_values)
    t_average = t_total / divisor

    print('****************************************************')
    print('The average moisture is ', round(m_average,1))
    print()
    print('The average temperature is ', round(t_average,1))
    print('****************************************************')
    break
restart = input('Hit "Enter" to close')
