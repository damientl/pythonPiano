
from intervals import play_intervals

if __name__ == '__main__':
    #somdifpausa-0, som normal-1,in-2,out-3,hold-4

    p_options = ['allSounds', '30s', 'default', '10s', 'wimhof', 'quadrada_wimhof', '20', 'pomodoro']
    i=0
    for o in p_options:
        print(f"{i} - {p_options[i]}")
        i+=1
    option = int(input())

    play_intervals(f"program/{p_options[option]}.csv")
