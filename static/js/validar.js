function validar(){
    var nombres, apellido, correo, contraseña;
    nombres = document.getElementById("nombres").value;
    apellido = document.getElementById("apellido").value;
    correo = document.getElementById("correo").value;
    contraseña = document.getElementById("contraseña").value;

    if(nombre == "" || apellido == "" || correo == "" ||contraseña == ""){
        alert("Todos los campos son obligatorios")
        return false;
    }
}
