!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()
s1 = data.getvalue('slider1')

with open('led_pwm.txt', 'w') as f:  
  #f.write(str(s1))
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="option" value="a" checked> LED 1 (blue) <br>)
print('<input type="radio" name="option" value="b"> LED 2 (red) <br>')
print('<input type="radio" name="option" value="c"> LED 3 (yellow) <br> <br>')
print('<input type="submit" value="Submit"> <br> <br> <br>')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change Brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')


