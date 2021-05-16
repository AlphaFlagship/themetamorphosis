
old_users = ['admin', 'mohi','ishu', 'cherry','abhi', 'archi']
new_users = ['admin', 'ishu','anu','bg','aki']
username = "ADMIN"
name = username.lower()
if username in old_users:
    print ("hi")
elif username != old_users:
    print ("enter username")
    if name in old_users:
        print("unavailable")
    else:
        print("ok")
    
print (name)

