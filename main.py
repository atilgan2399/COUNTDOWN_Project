import time
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}: {:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t=t-1
    print("Sayaç ended..")
t =input('LÜTFEN KAÇ SANİYE OLACAĞINI GİRİNİZ ZAHMET OLMAZSA :')
countdown(int(t))