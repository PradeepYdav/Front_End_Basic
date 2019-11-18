var fname=prompt("Enter First Name")
var lname=prompt("Enter last name")
var age =prompt("Enter age")
var height =prompt("Height in cm")
var petname=prompt("Enter Pet name")

var l=petname[petname.length-1]

if (fname[0] ==lname[0] && age>20 && age<30 && height>=170 && l=="y"){
    console.log(" hey Comrode you are a spy");
}
else{
  console.log("Nothing ");
}
