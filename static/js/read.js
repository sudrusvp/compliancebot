///*eslint-env browser */
//var txtFile = "static/js/test.txt";
//var file = new File(txtFile);
//
//file.open("r"); // open file with read access
//var str = "";
//while (!file.eof) {
//	// read each line of text
//	str += file.readln() + "\n";
//}
//file.close();
function readTextFile(filepath) {
	var str = "";
	var txtFile = new File(filepath);
	txtFile.open("r");
	while (!txtFile.eof) {
		// read each line of text
		str += txtFile.readln() + "\n";
	}
	return str;
}