
print('Welcome to the DataBase Admin Program')

#Create dicctionary to hold all username:password key-value pairs
log_on_info = {
    'pepe':'1234',
    'Enrique':'5678',
    'Jose':'0000',
    'admin':'admin',
}

#User input
username = input('Enter yor username: ')

#Simulete login on...
print('Loading...')

#Get User password
if username in log_on_info.keys():
    password = input('Enter your password: ')
    if password == log_on_info[username]:
        print(' Hello ' + username + '!')
        if username == 'admin':
            #Show the whole database
            print(' Here is the current database: ')
            for key, value in log_on_info.items():
                print('Username: ' + key + ' Password: ' + value)
        else:
            #Allow standar user to change their password
            password_change = input('Would you like to change your password?=(yes/no): ').lower().strip()
            if password_change =='yes':
                new_password = input('Introduce the new password: ')
                print(username + ' your new password is ' + log_on_info[username] + '.')
            else:
                print('Thanks, goodbye')
    #wrong password
    else:
        print('password incorrect!')

#User not in database
else:  
    print('Error, username not in database')