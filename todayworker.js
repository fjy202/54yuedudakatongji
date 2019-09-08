var renshu=46
function getWorker(date){
    firstDate=new Date("2019-09-03")
    secondDate=new Date(date)
    var diff = Math.abs(firstDate.getTime() - secondDate.getTime())
    var result = parseInt(diff / (1000 * 60 * 60 * 24));
    return result%renshu+1
}