
print("welcome to exception handling party")


def firstExceptionSample():
    try:
        #print(x)
        secondExceptionSample()
    except TypeError as e: #just notice how I define it .. with no () and also I use "as" keyword
        print("what the ...! " + str(e) )
        template = " the exception type is {0}".format(type(e).__name__)
        print(template);
    except(ValueError):
        print("haha no value is set")
    except Exception as e:
        #print("finally ye exception hast")
        print(str(e))                           # learn how to print the e message

    else:
        print("khodaro shokr moshkeli nist")
    finally:
        print("va in dastan be etmam resid")


def secondExceptionSample(): #learn how to raise an error
    x = -1
    if(x<0):
        #raise Exception("sorry, no numbers below zero")
        raise TypeError("sorry, no numbers below zero")


firstExceptionSample()