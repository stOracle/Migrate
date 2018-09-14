<?php
// Include the PEAR DB library.
require_once "DB.php";

// Use PEAR DB's ODBC driver as the backend.
$dbbackend = "odbc";

// For SQL Server, you must specify the database username and
// password here. Otherwise, leave $dbuser and $dbpassword
// blank if not required by your database or already specified
// in the ODBC data source.
$dbuser = "";
$dbpassword = "";

// Replace my_easysoft_dsn with the name of your Easysoft ODBC data
// source.
$dbname = "my_easysoft_dsn";

// Replace my_table with the name of a table in your database.
$stmt = "SELECT * FROM my_table";

// This DSN connects to an Easysoft ODBC data source.
if ($dbuser == "") {
    $dsn = "$dbbackend:///$dbname";
} else {
    $dsn = "$dbbackend://$dbuser:$dbpassword@/$dbname";
}

// Create a new DB connection object and connect to the ODBC database.
$dbh =& DB::connect($dsn);
if (DB::isError($dbh)) {
    die("Unable to connect to database: " . $dbh->getMessage() . "\n"
                                          . $dbh->getDebugInfo() . "\n");
}

// Use the database connection object to execute a SQL query.
$sth =& $dbh->query($stmt);
if (DB::isError($sth)) {
    die("Unable execute query: " . $sth->getMessage() . "\n"
                                 . $sth->getDebugInfo() . "\n");
}

// Retrieve each row from the DB result object.
while ($row =& $sth->fetchRow()) {
    print_r($row);
}

// Release the result set.
$sth->free();

// Close the connection object.
$dbh->disconnect();
?>