from termcolor import colored, cprint
import sys
import math
import os
import time
from tqdm import tqdm


def menu(status='Hack responsibly.', repeated=False):
    logo = """
                    .                                                      .
                .n                   .                 .                  n.
        .   .dP                  dP                   9b                 9b.    .
        4    qXb         .       dX                     Xb       .        dXp     t
        dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
        9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
        9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
        `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
            `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
                ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                )b.  .dbo.dP'`v'`9b.odb.  .dX(
                            ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                            dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                            dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                            9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                            `'      9XXXXXX(   )XXXXXXP      `'
                                    XXXX X.`v'.X XXXX
                                    XP^X'`b   d'`X^XX
                                    X. 9  `   '  P )X
                                    `b  `       '  d'
                                    `             '
            """
    content = ''

    items = (
        'Catch a Victim',
        'Exploit Credentials',
        'Bruteforce Site',
        ''
        
    )

    for num in range(len(items)):
        content += '[{0}] {1} \n\r'.format(num + 1, items[num])

    output = "{0}\n{1}\n\n{2}\n".format(
        colored(logo, 'red'), colored(status.center(90), 'green'), content)

    if not repeated:
        sys.stdout.write('\r' + output)
        sys.stdout.flush()

    response = input(">> ")

    if response not in [str(items.index(x) + 1) for x in items]:
        os.system('clear' if os.name == 'nt' else 'cls')
        return menu('Repeated shit')
    else:
        return response


def find_user():

    user = input('Username/Email: ')
    for i in tqdm(range(120), ncols=120, ascii=True, desc='Finding [{0}]'.format(user)):
        time.sleep(0.1)

    print(colored('\r"{0}" user not found, please try again'.format(user), 'red'))



if __name__ == "__main__":
    if menu() == '1':
        find_user()
