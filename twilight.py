class sparkle(object):
    reset = '\033[0m'
    charcoal = '\033[30m'
    grey = '\033[90m'
    wine = '\033[31m\033[2m'
    red = '\033[m'
    cherry = '\033[91m'
    bronze = '\033[33m\033[2m'
    gold = '\033[33m'
    yellow = '\033[93m'
    grass = '\033[92m'
    green = '\033[32m'
    forest = '\033[32m\033[2m'
    teal = '\033[36m\033[2m'
    cyan = '\033[36m'
    sky = '\033[96m'
    baby = '\033[94m'
    blue = '\033[34m'
    royal = '\033[34m\033[2m'
    magenta = '\033[35m\033[2m'
    purple = '\033[35m'
    violet = '\033[95m'
    light = '\033[37m'
    white = '\033[97m'

if __name__ == '__main__':
    print sparkle.red + 'Red ' + sparkle.reset + 'reset'
    print sparkle.yellow + 'Yellow ' + sparkle.reset + 'reset'
    print sparkle.green + 'Green ' + sparkle.reset + 'reset'
    print sparkle.blue + 'Blue ' + sparkle.reset + 'reset'
