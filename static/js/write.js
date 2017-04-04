/*eslint-env browser */
var txtFile = "static/js/test.txt";
var file = new File(txtFile);
var str = "My string of text";

file.open("w"); // open file with write access
file.writeln("First line of text");
file.writeln("Second line of text " + str);
file.write(str);
file.close();



