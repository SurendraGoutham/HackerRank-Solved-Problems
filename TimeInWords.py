'''
Created on 07-Apr-2015

@author: 00003179
'''
 
class TimeInWords():
    def __init__(self):
        self.words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one",
       "twenty two", "twenty three", "twenty four", "twenty five",
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
 
    def caltime(self,hrs,mins):
        msg = ""
        if (hrs > 12):
            hrs = hrs - 12
        if (mins == 0):
            hr = self.words[hrs - 1]
            msg = hr + " o' clock"
        elif (mins < 31):
            hr = self.words[hrs - 1]
            mn = self.words[mins - 1]
            if (mn is "quarter") or (mn is "half"):
                msg = mn + " past " + hr
            else: msg = mn + " minutes past " + hr
            if(mins == 1) : msg = mn + " minute past " + hr
        else:
            hr = self.words[hrs]
            mn = self.words[(60 - mins - 1)]
            if (mn is "quarter") or (mn is "half"):
                msg = mn + " to " + hr
            else:
                msg = mn + " minutes to " + hr
        return msg
 
 
if __name__ == '__main__':
    hrs = int(input())
    mins = int(input())
    t = TimeInWords()    
    print t.caltime(hrs,mins)
