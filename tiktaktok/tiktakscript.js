
//  get restar button

var restart=document.querySelector("#b")

//grabs all the squares

var squares=document.querySelectorAll("td")


//clear all the Squares funxtion

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent='';
  }

}

restart.addEventListener("click",clearBoard);


//get the marker
//
// var cellone=document.querySelector("#one")
//
// cellone.addEventListener("click",function() {
//   if (cellone.textContent===''){
//     cellone.textContent="X";
//   }else if (cellone.textContent==="X") {
//     cellone.textContent="O";
//   }else {
//     cellone.textContent='';
//   }
// })

//check querySelector

function changeMarker() {
  if(this.textContent===''){
    this.textContent="X";
  }else if (this.textContent==="X") {
      this.textContent="O";
  }else {
    this.textContent='';
  }

}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker)
}
