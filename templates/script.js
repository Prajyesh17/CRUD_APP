let body = document.body //this is the body of the document, we are gonna be adding elements to this page.We can add elements to this body (append)
const div = document.createElement("div") //this is how you add reference to an element, you are only refenrencing it here, you stil have to add it next. Const basically means you cant change it later on in html.
//div.innerText = "Hello, world!" //this is how you add text inside a div.
//in append you can append strings as well and multiple things at once
div.textContent = "Hello, world 2!" //this is how you add text inside a div
body.append(div) 


