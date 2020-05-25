# فرهنگ

لغت نامه فارسی به فارسی، شامل فرهنگ معین و دهخدا.

نمونه:

    http://dictionary.newbtin.ir/v1/dictionary/

    http://dictionary.newbtin.ir/v1/dictionary/word/ماش
    
    http://dictionary.newbtin.ir/v1/dictionary/1/word/ماش


### روش نصب

کلون کردن برنامه

    git clone https://github.com/abtinmo/farhang-backend && cd farhang-backend 
    

نصب محیط مجازی و پیش‌نیاز‌ها

    sudo apt install redis postgresql python3-pip

    python3 -m pip install virtualenv
    
    python3 -m virtualenv .venv && source .venv/bin/activate
    
    pip install -r requirements/prod.txt
        
تغییر تنظیمات برنامه


    cp .env.sample .env


در محیط عملیاتی مقادیر زیر را فالس قرار دهید

    DEBUG = True

    ACCESS_LOG = True

پورت و هاستی که برنامه بر روی آن قابل دیدن است

    PORT = 8888
    HOST = "localhost"

آدرس و اطلاعات دیتابیس

    DB_DSN = "postgresql://localhost/farhang"


آدرس ردیس و مقدار زمانی که داده‌های کش شده را نگهداری میکند به ثانیه

    CACHE_DSN = "redis://localhost"

    CACHE_EXPIRE_TIME = 3600
 

### مقدار دهی اولیه دیتابیس

    psql -U postgres farhang < farhang.psql
    
حجم داده ‌های فرهنگ دهخدا حدود ۲۴۰ مگابایت می‌شود و امکان بارگزاری در بستر گیتهاب میسر نبود، در صورت نیاز می‌توانید از این مخزن استفاده کنید. 
https://github.com/nimah79/Dehkhoda-SQL


### اجرای برنامه

    python3 main.py
