import sys, time, argparse
from termcolor import colored, cprint
from tqdm import tqdm           
from datetime import datetime
from time import sleep

def drammExploit():
    print(datetime.now().strftime('[%m-%d-%y %H:%M:%S] ') + 'Initializing commands...')
    time.sleep(.9)
    print(datetime.now().strftime('[%m-%d-%y %H:%M:%S] ') + 'Initializing su files...')
    time.sleep(.9)
    modules = [
        'Rooted the device successfully.',
        'Busybox installed in /system/xbin.',
        'Spoofer 1.2a installed.',
        'DecryptMyCache BETA installed.'
    ]
    for i in range(4):
        for j in tqdm(range(50), 'Installing module'):
            sleep(0.2)
        print(modules[i])
    
    cprint(datetime.now().strftime('[%m-%d-%y %H:%M:%S] ') + 'Modules installed successfully.\n', 'green')

    sleep(2)
    print('Rebooting device to take effect...')
    sleep(12)
    print('\nRebooted successfully')
    sleep(1)

def start(ip = '192.168.1.53', port=443):

    loader = '-\\|/'

    for i in range(1, 6):
        sys.stdout.write('\rSpoofing device credentials... {0} of 5'.format(i))
        sys.stdout.flush()
        time.sleep(0.5)
    print('''\nDevice: {0}
IMEI : 334199983826931
MAC Address: 18:cc:72:df:8a:e5
IPv4: 192.168.1.53'''.format('Samsung'))
    time.sleep(1)
    input('Perform exploit check [Y/n] : ')
    sleep(1)
    cprint('\nGenerating configurations...\n', 'yellow')
    time.sleep(1)

    counter = 0
    for i in range(104):
        if counter > len(loader)-1:
            counter = 0
        sys.stdout.write('\r' + colored('Poisoning Network...'+loader[counter], 'red'))
        sys.stdout.flush()
        time.sleep(.1)
        counter += 1

    print()

    for i in range(1, 126):
        sys.stdout.write('\rFinding an exploit... {0} of 45'.format(i))
        sys.stdout.flush()
        if i == 38:
            break
        time.sleep(0.1)
    
    cprint('\nFound 1 exploit.','red')
    
    time.sleep(1)
    count = 4
    for i in tqdm(range(20), 'Preparing a DRAMM Attack'):
        time.sleep(0.3)
    
    input('\nDo you want to continue[y/n]: ')

    drammExploit()

    cprint('\nGained root access to the device!\n', 'red', attrs=['bold', 'dark'])
    time.sleep(.89)
    cprint('Setting up init files...')
    time.sleep(.89)
    cprint('Initiating shell', 'yellow')
    time.sleep(2)

    while True:
        sys.stdout.write('\r' + colored('Shell>> ','red',attrs=['bold', 'dark']))
        sys.stdout.flush()
        cmd = input()
        print('Connecting to the irc servers...')
        sleep(2)

        irc_servers()

        for i in range(32):
            cprint(datetime.now().strftime('[%m-%d-%y %H:%M:%S] ') + 'Messaged channels id:E0K92K3E019S' + str(i*9^2), 'yellow')
            time.sleep(0.1)
        cprint('\nMessaged 32 channels. [SUCCESS]', 'green', attrs=['bold'])
        sleep(3)
        break


def irc_servers():
    for i in range(32):
        cprint(datetime.now().strftime(
            '[%m/%d/%y %H:%M:%S]') + 'Connected to E0K92K3E019S'+ str(i*9^2), 'blue')
        sleep(1)
    print('Succesfully connected to the channels.')
    sleep(2)
    print('Serializing device object...')
    sleep(1.5)

def catch_a_device():

    loader = '-\\|/'
    counter = 0

    for i in range(1500):
        if count == len(loader)
        print('Catching connected device...' + loader[i])
        sleep(.02)
        counter += 1

    print('Device found in 192.168.43.28')
    sleep(3)
    print('Instantiating objects...')
    sleep(.8)
    print('Initiating attack...')
    sleep(5)

if __name__ == "__main__":
    start_time = time.time()
    start()
    print('Script finished in ' + str(time.time() - start_time) + ' seconds.')
