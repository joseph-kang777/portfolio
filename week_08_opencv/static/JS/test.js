const dropbox = document.querySelector('.file_box');
const input_filename = document.querySelector('.file_name');
const image_= document.getElementById("file_name")


//박스 안에 drag 하고 있을 때
dropbox.addEventListener('dragover', function (e) {
  e.preventDefault();
  this.style.backgroundColor = 'rgb(13 110 253 / 25%)';
});

//박스 밖으로 drag가 나갈 때
dropbox.addEventListener('dragleave', function (e) {
  this.style.backgroundColor = 'white';
});

//박스 안에 drop 했을 때
dropbox.addEventListener('drop', function (e) {
  e.preventDefault();
  this.style.backgroundColor = 'white';

  //파일 이름을 text로 표시
  let filename = e.dataTransfer.files[0].name;
  input_filename.innerHTML = filename;
});


// 체크박스 단일 선택
function checkOnlyOne(element) {
  
  const checkboxes 
      = document.getElementsByName("gender");
  
  checkboxes.forEach((cb) => {
    cb.checked = false;
  })
  element.checked = true;
}

