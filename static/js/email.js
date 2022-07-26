function sendEmail() {
	Email.send({
	Host: "smtp.gmail.com",
	Username : "shubhamlagad800@gmail.com",
	Password : "gmailaccount4",
	To : 'shubhamlagad2000@gmail.com',
	From : "shubhamlagad800@gmail.com",
	Subject : "hello onkar",
	Body : "welcome to smptp",
	}).then(
		message => alert("mail sent successfully")
	);
}




// function sendEmail() {
// 	Email.send({
// 	Host: "smtp.gmail.com",
// 	Username : "<sender’s email address>",
// 	Password : "<email password>",
// 	To : '<recipient’s email address>',
// 	From : "<sender’s email address>",
// 	Subject : "<email subject>",
// 	Body : "<email body>",
// 	}).then(
// 		message => alert("mail sent successfully")
// 	);
// }