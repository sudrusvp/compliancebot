<html>
<p>Hi</p>
<?php
function writeToFile() {
	$myfile = fopen("static/php/test.txt", "w") or die("Unable to open file!");
	$txt = "John Doe\n";
	fwrite($myfile, $txt);
	$txt = "Jane Doe\n";
	fwrite($myfile, $txt);
	fclose($myfile);
}
writeToFile();
?>
</html>