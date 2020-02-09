from time import sleep
import sys

def mark(email):
    password = 'ethanlovesnicole020720'
    print()
    print('Facebook Account Credentials\n')
    print('Email: ' + email)
    sleep(3)
    print('Passkey: ', end='')
    for i in range(len(password)):
        sys.stdout.write(password[i])
        sys.stdout.flush()
        sleep(.3)
    print('\n\nDecrypted Successfully.')

def jude(email):
    password = 'judewiththelord2000'
    print()
    print('Facebook Account Credentials\n')
    print('Email: ' + email)
    sleep(3)
    print('Passkey: ', end='')
    for i in range(len(password)):
        sys.stdout.write(password[i])
        sys.stdout.flush()
        sleep(.3)
    print('\n\nDecrypted Successfully.')

def nacua(email):
    password = 'beatles4everdepressed'
    print()
    print('Facebook Account Credentials\n')
    print('Email: ' + email)
    sleep(3)
    print('Passkey: ', end='')
    for i in range(len(password)):
        sys.stdout.write(password[i])
        sys.stdout.flush()
        sleep(.3)
    print('\n\nDecrypted Successfully.')

def print_loader(text, msg_done='Done.'):
    loader = '-\\|/'
    counter = 0
    for i in range(78):
        if counter == len(loader):
            counter = 0
        sys.stdout.write('\r' + text + loader[counter])
        sys.stdout.flush()
        counter += 1
        sleep(.06)
    print('\n' + msg_done)

print('Recent site: 102.124.234.23')
input("Set index server: ")

print_loader('Connecting to the server...', '\nConnected to port : 23679')
print_loader('Initializing setup...', '\nConfiguration done.')

email = input('\nEmail: ')

password = input('\nEnter the password pattern: ')

for i in range(1, 534):
    sys.stdout.write(f'\rBruteforcing password ({i}) of 533')
    sys.stdout.flush()
    sleep(.1)
    if email == 'jake_cobain04@gmail.com' and i == 267:
        print('\nPassword found.\n')
        sleep(1)
        nacua(email)
        break
    elif email == 'judeuaskiss@gmail.com' and i == 478:
        print('\nPassword found.\n')
        sleep(1)
        jude(email)
        break
    elif i == 530:
        print('\nPassword found.\n')
        sleep(1)
        mark(email)
        break


