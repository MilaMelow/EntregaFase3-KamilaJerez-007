function validar(){
    var correo, contraseña;
    correo = document.getElementById("correo").value;
    contraseña = document.getElementById("contraseña").value;

    if(correo == "" ||contraseña == ""){
        alert("Todos los campos son obligatorios")
        return false;
    }
}