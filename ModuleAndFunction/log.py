import datetime
def register_log(*messages, **settings):
    """ Bu fonksiyon sınırsız string türünde mesaj ve **kwargs ile çalışır. Beklenen key'ler şöyledir: 'level','time','file','color' """
    level = settings.get("level","INFO")
    is_time_stamp = settings.get('time',True)
    file = settings.get('file',None)
    color = settings.get('color',None)

    if is_time_stamp:
        time = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
        prefix = f"[{time}] [{level}]"
    else:
        prefix = f"[{level}]"

    full_message = f"{prefix} {' '.join(messages)}"

    if color:
        full_message += f" {color}"
    
    if file:
        print(f"{file} isimli dosyaya kaydedildi")

    print(full_message)
    print()
