//Создаём функцию, которая фильтрует исходный массив, проверяя есть ли в элементе не менее 2 русских букв  
function checkArray(arr){
  let ar = arr.filter(el =>                                          
     el.match(/[А-Яа-яЁё]/gi)!==null && el.match(/[А-Яа-яЁё]/gi).length>1    
  )
  return ar
}
// Исходный массив со строками, который необходимо отфильтровать
const array = ["ghvbjnk","vgbhnj", "пр ито", "cfvgbhjn", "пмриото", "GHBРПHGJH", "GHBПоGJH", "56bhирbhbn"]

//Выводим результат 
console.log (checkArray(array))

