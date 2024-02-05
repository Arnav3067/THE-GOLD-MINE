#Africa Game

countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]

print('welcome freinds tp the countries of Africa')
lives = 3
score = 0
while len(countries) >0:
    print('the number of countries to guess')
    print(len(countries))
    print('your score is :',score,'\tyou have',lives,'lives')
    country = input('enter the name of a country')
    country1 = country[0].upper()+country[1:]
    if country1 in countries :
        print('YOU SCORED!!')
        score = score +1
        countries.remove(country1)
    else :
        print('invalid guess')
        lives = lives -1
        
    if lives == 0 :
        print('game over')
        break
        
print('you win')
