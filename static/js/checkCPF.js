onload = function() {
    document.getElementById('id_cpf').addEventListener('keyUp', checkCPF);
}

function checkCPF(e) {
    var cpf_field = document.getElementById('id_cpf');
    var cpf_value = cpf_field.value;
    xmlhttp = new XMLHttpRequest();
    console.log(cpf_value);
    xmlhttp.open('GET', '/accounts/checkCPF' + '?cpf=' + encondeURIComponent(cpf_value),true);
    xmlhttp.onreadystatechange = checkCPFCallBack;
    xmlhttp.send(null);
}

function verificaUsernameCallBack() {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var response = JSON.parse(xmlhttp.responseText);
        document.getElementById('idErro').replaceChild(
            document.createTextNode(response.message),
            document.getElementById('idErro').firstChild
        );
    }

}
