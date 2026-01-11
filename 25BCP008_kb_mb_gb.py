def kb_mb_gb():
    a=int(input("Enter the number of bytes:"))
    KB=a/1024
    MB=a/(1024*1024)
    GB=a/(1024*1024*1024)
    print("The number of bytes in KB, MB, GB are:", KB, MB, GB)
kb_mb_gb()
