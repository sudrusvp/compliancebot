/*eslint-env browser */
var txtFile = "static/js/test.txt";
var file = new File(txtFile);

file.open("r"); // open file with read access
var str = "";
while (!file.eof) {
	// read each line of text
	str += file.readln() + "\n";
}
file.close();