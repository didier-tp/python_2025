import sys
import os
print("sys.argv=",sys.argv)
print("app name=",sys.argv[0])
if len(sys.argv)>1 :
    print("premier arg=",sys.argv[1])
if len(sys.argv)>2 :
    print("second arg=",sys.argv[2])
    try :
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c=a+b
        resMessage=f"a={a} b={b} c=a+b={c}"
        CASE_ENV=os.environ.get("CASE","?")
        print(f"CASE_ENV={CASE_ENV}")
        if CASE_ENV=='MAJ':
            resMessage=resMessage.upper()
        print(resMessage)
    except:
        # print("erreur: arguments numeriques attendus") # print to stdout 
        print("erreur: arguments numeriques attendus" , file = sys.stderr)
        sys.stderr.write("direct write in stderr ...\n")