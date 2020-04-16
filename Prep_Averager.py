#count how many numbers are input by user
m_count = 0
m_total = 0
m_number = 0

#user inputs the floats
while True :
    m_number = float(input('Enter moisture with decimal, enter -1 to calculate: '))
    if m_number < 0:
        if m_count == 0:
            print('No numbers entered yet')
            continue
        break

    m_count += 1
    m_total += m_number
#add up numbers and divide by the counter
m_average = m_total / m_count

print()
print('The average moisture was:', round(m_average, 1))
print()
print('Number of values entered:', m_count)
print('Sum of entered values', m_total)
print()
print('**************************************************************')
print()
#start temp average
#count how many numbers are input by user
t_count = 0
t_total = 0
t_number = 0

#user inputs the floats
while True :
    t_number = int(input('Enter temp with decimal, enter -1 to calculate: '))
    if t_number < 0:
        if t_count == 0:
            print('No numbers entered yet')
            continue
        break

    t_count += 1
    t_total += t_number
#add up numbers and divide by the counter
t_average = t_total / t_count

print()
print('the average temp was:', round(t_average, 1))
print()
print('number of values entered:', t_count)
print('Sum of entered values', t_total)
