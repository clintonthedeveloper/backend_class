countries = ['United kingdom', 'Ghana', 'Nigeria', 'Kenya', 'Western']
print(countries[0])
# Getting countries to the end also you can get range
print(countries[1:])

# type list
print(type(countries))

# Changing one value to another
countries = ['Kenya', 'Ethopia', 'Tanzania', 'Uganda' ]
countries[0] = 'Djibout'
countries[3] = 'Canada'
print(countries)

# Lenth list
countries = ['Kenya', 'Ethopia', 'Tanzania', 'Uganda' ]
print(len(countries))

# Type of value in a list
countries = ['Kenya', 'Ethopia', 2, True, 'Tanzania', 'Uganda']
print(type(countries[0]))

# list constractor
countries = list(('Kenya', 34, False))
print(countries)