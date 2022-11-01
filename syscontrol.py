import subprocess as sp


def return_command(cmd:str):
    # The command you want to execute   
    cmdlist = cmd.strip().split(" ")

    # send one packet of data to the host 
    # this is specified by '-c 1' in the argument list 
    #cmd.append("/dev/null")
    # Iterate over all the servers in the list and ping each server
    
    process = sp.Popen(cmdlist, stdout=sp.PIPE, stderr=sp.PIPE)
    
    stdout, stderr = process.communicate()
    #print(stderr.decode("utf-8"))
    return stdout.decode("utf-8").strip()