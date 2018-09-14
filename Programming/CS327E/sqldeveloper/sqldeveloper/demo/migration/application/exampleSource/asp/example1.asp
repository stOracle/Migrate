<html>
<head>
<title>My First ASP Page</title>
</head>
<body bgcolor="white" text="black">
		
<% 
'Dimension variables
Dim adoCon         'Holds the Database Connection Object
Dim rsGuestbook    'Holds the recordset for the records in the database
Dim strSQL         'Holds the SQL query to query the database
'Create an ADO connection object
Set adoCon = Server.CreateObject("ADODB.Connection")

'Set an active connection to the Connection object using a DSN-less connection
adoCon.Open "Provider=Microsoft.Jet.OLEDB.4.0; Data Source=" & Server.MapPath("guestbook.mdb")

'Set an active connection to the Connection object using DSN connection
adoCon.Open "DSN=guestbook"
	
'Create an ADO recordset object
Set rsGuestbook = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT tblComments.Name, tblComments.Comments FROM tblComments;"

		
'Open the recordset with the SQL query 
rsGuestbook.Open strSQL, adoCon

		
'Loop through the recordset 
Do While not rsGuestbook.EOF 

    'Write the HTML to display the current record in the recordset 
    Response.Write ("<br>") 
    Response.Write (rsGuestbook("Name")) 
    Response.Write ("<br>") 
    Response.Write (rsGuestbook("Comments")) 
    Response.Write ("<br>") 

    'Move to the next record in the recordset 
    rsGuestbook.MoveNext 
Loop

		
'Reset server objects
rsGuestbook.Close
Set rsGuestbook = Nothing
Set adoCon = Nothing
%>

</body>
</html>
