function download(filename, character_class) {
    var headlines_data=document.getElementsByClassName('0');
    var info = document.getElementsByClassName(character_class);
    var data = '';


    for(var i=0; i<headlines_data.length; i++){
        if(headlines_data[i+1]==null){
            data += headlines_data[i].innerHTML + ':' + info[i].innerHTML;
        }else{
            data += headlines_data[i].innerHTML + ':' + info[i].innerHTML+ '\n';
        }

    }

    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}