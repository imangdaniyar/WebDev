document.getElementById("addTask").addEventListener("click", addTask);
  	let n = 0;
function addTask() {
	let taskName = document.querySelector('input#taskName').value;
  	console.log(taskName);
  	let tasks = document.querySelector('#tasks');
  	let task = document.createElement('div');
  	n = n + 1;
  	task.setAttribute("class","task");
  	task.setAttribute("id","task" + n);
  	let checkbox = document.createElement('input');
  	let name = document.createElement('span');
  	let button = document.createElement('button');
  	button.setAttribute("class","delete");
  	button.setAttribute("onclick","deleteElement(task"+n+")");
  	var t = document.createTextNode(taskName);
  	button.appendChild(document.createTextNode("Delete"));
  	name.appendChild(t);
  	checkbox.setAttribute("type","checkbox")
  	tasks.appendChild(task);
  	task.appendChild(checkbox);
  	task.appendChild(name);
  	task.appendChild(button)
}
function deleteElement(number) {
	let tasks = document.querySelector('#tasks');
	let taskId = document.querySelector('#' + number.getAttribute("id"));
	tasks.removeChild(taskId)
}