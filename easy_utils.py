from time import sleep
from os import system, listdir, path, sys
from datetime import datetime


def mkdir_name(url,*flag):
    dir_name = url.rsplit('/', 2)[1]
    if flag in dir_name:
        dir_name = dir_name.rsplit("-", 1)[0]

        if dir_name[-1] == '/':
            return dir_name
        else:
            dir_name = dir_name + '/'
            return dir_name
    else:
        return dir_name

def mk_fname(url, ftype, *flag):
    fname = url.rsplit(flag)[0].rsplit('/', 1)[1]
    if ftype not in fname:
        return fname + ftype
    else:
        return fname
def kill_drivers(*silent):
    if silent != 'silent':
        system('pkill chromium && pkill chromedriver')
        print(Fore.GREEN + 'killed chromium and chromedriver sessions'+Style.RESET_ALL)
        return

    else:
        system('pkill chromium && pkill chromedriver')
        return

def alert(alarm, x):
    for i in range(x):
        print(Fore.YELLOW + alarm+Style.RESET_ALL)
        sleep(1)
    return

def check_dir(child, parent):
    file_dest  =  parent + child
    if child[:-1] not in listdir(parent):
        command  = 'm kdir ' + file_dest
        system(command)
        print(command)
        log_it(command)
        return file_dest
    else:
        return file_dest

def check_file(fname, file_dest):
    if fname not in listdir(file_dest):
        return file_dest +fname
    else:
        return False

def log_it(text):
    fname = './log/'+str(datetime.today()).rsplit(' ',1)[0]+'.log'
    #exc_type, exc_obj, exc_tb = sys.exc_info()
    #fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #text = str(text) +'\n'+ str(exc_obj) + str(exc_type) + ' ' + str(exc_tb.tb_lineno)
    text = str(text)
    with open(fname, 'a+') as f:
        f.write(str(datetime.now())[:-7]+'\t'+text+'\n')
        f.close()

def check_url(name, url, flag):
    #if 'id=' not in video_name:
    if flag not in name:
        error = 'skipping : ' + flag+' in '+url
        print(Fore.RED + error + Style.RESET_ALL)
        log_it(error)
        return False
    else:
        return True

def remove_it(src_dir):
    command = "rm -rf " + src_dir
    system(command)
    print(command)


def ship_it(dest_login,src_dir,dest_dir):
    command = "scp -r " + src_dir + ' ' + dest_login + ":" + dest_dir 
    try:
        print(command)
    #system(command)
        remove_it(src_dir)
    except:
        print('problem shipping files to',dest_login )

def live_download(server, destination):
    if path:
        command = 'curl ' + server + ' --max-time 2400 -o ' + destination
        #test_command = 'touch '+ destination
    else:
        return
    print(Fore.MAGENTA + command+Style.RESET_ALL)
    log_it(command)
    system(command)
    check_download(destination)
    msg = 'success senpai... '+destination+" downloaded"
    print(Fore.BLUE +msg+Style.RESET_ALL)
    log_it(msg)
        
def check_download(d_file):
    d_size = path.getsize(d_file)/(2**20)
    status = ''
    if d_size > 200:
        status = status +  "download met size requirement"
        print(status)
        log_it(status)
        return True
    else:
        status = status +  "download possibly incomplete"
        print(status)
        log_it(status)

