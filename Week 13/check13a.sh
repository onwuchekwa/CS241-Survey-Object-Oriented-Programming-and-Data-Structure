//Create a new file and write to it
echo "Hello CS 241 World" >hello.txt

//Display the content of a file
cat < hello.txt

//Directory listing to a file
ls /home > homeDirs.txt

// Get the first 20 lines
head -n 20 homeDirs.txt >homeDirs_20.txt

Search files
grep -l "format" *.py

//Less
grep -l "format" *.py | less

// Grep, Tail, and Redirect.
grep -l "format" *.py | tail -n 5 >homeDirs_5.txt
