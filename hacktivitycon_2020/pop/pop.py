import os

while True:    
    file = os.popen('ls pop/').read()
    file = file.strip()
    cmd = 'file pop/' + file
    res = os.popen(cmd).read().strip()    
    print(res)
    if res.find(" XZ ") != -1:        
        cmd = " mv pop/" + file + " pop/out.xz"    
        os.system(cmd)
        cmd = "unxz pop/out.xz"
        os.system(cmd)
    elif res.find(" bzip2 ") != -1:
        cmd = " mv pop/" + file + " pop/out.bz2"   
        print(cmd) 
        os.system(cmd)
        cmd = "bunzip2 pop/out.bz2"
        os.system(cmd)
    elif res.find(" gzip ") != -1:        
        cmd = "mv pop/" + file + " pop/tmp.gz"
        os.system(cmd)
        cmd = "gunzip pop/tmp.gz"
        os.system(cmd)
    elif res.find(" Zip ") != -1:
        print("Zip")
        cmd = "unzip -o -d pop/ pop/" + file
        print(cmd)
        os.system(cmd)
        if len(os.listdir("/home/kali/Downloads/pop/")) > 1:
            print(file)
            cmd = "rm pop/" + file
            os.popen(cmd)
    else:
        print("Unrecognized file format:")
        print(res)
        break