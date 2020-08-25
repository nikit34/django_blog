let previews = document.getElementsByClassName('preview');
Array.from(previews).forEach((el)=>{
  el.innerHTML = el.innerText;
});