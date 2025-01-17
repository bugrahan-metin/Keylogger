# Keylogger

# Nasıl Kullanılır
- Kullanmadan önce komutların içerisindeki email ve password bilgilerini değiştirmeyi unutmayınız.
- İsteğe bağlı olarak 30 saniye olarak ayarlanan gönderim sıklığını da değiştirebilirsiniz.
- Kullanmak istediğiniz bilgisayarda çalıştırdıktan sonra belirlediğiniz süre sonrasında devamlı olarak hangi tuşlara basıldığı sırasıyla birlikte yazdığınız email adresine gönderilecektir.
- uygulamayı çalıştırmadan önce email adresinizden uygulama şifreleri bölümünden şifrenizi almanız gerekmektedir onun dışındaki şifrelerle uygulmanız çalışmayacaktır.
- Gmail adresinizde uygulama şifreleri bölümünü açmak için öncelikle 2 aşamalı doğrulamayı etkinleştirip daha sonra denemelisiniz.
- Eğer gmail dışında bir mail gönderme işlemi yapacaksanız kod içinde varsayılan olarak ayarlanan 587 portunu hangi aracı kullanacaksanız o aracın portunu girmeniz gerekmektedir.
- Doğru portu bulmak için smtplib kütüphanesinin dökümanlarına göz atabilirsiniz.

# Notlar
- Kullanmadan önce gerekli olan pynput ve smtplib kütüphanelerini bilgisayarınıza indirmeyi unutmayınız.
   ```bash
   pip install smtplib
   pip install pynput


Bu uygulama yalnızca eğitim amaçlıdır. İzinsiz her türlü kullanım kesinlikle yasaktır.
