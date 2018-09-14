'''
Created on May 17, 2018

@author: srauner
'''

header="Content-Type: text/html\n\n"

page = """
<!DOCTYPE html>
<html>
<head>
<title>Welcome to My House</title>
</head>
<body>
<form name="weatherForm">
    <p>Zip Code: <input type="text" name ="zipcode"></input>
    <br/>
    <input type="submit"></input>
</form>
<hr/>

<h1>Address: 2300 Cloud Way, Austin TX 78741</h1>

</body>
</html>
"""

print(header)
print(page)