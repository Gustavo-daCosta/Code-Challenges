const faseAtual = 3;
if (faseAtual === 3) {
    let buffetsVisitados = {buffet1: true, buffet2: true, buffet3: true, buffet4: true};
    let todosBuffetsVisitados = true;
//    for (var i = 0; i < 4; i++) {
//        console.log(buffetsVisitados[i]);
//        if (!buffetsVisitados[i]) {
//            todosBuffetsVisitados = false;
//            break;
//        }
//    }
    Object.entries(buffetsVisitados).forEach(([key, val]) => {
        if (!val) {
            todosBuffetsVisitados = false;
        }
    });
    if (todosBuffetsVisitados) {
        console.log("Fase 3 !!");
    } else {
        console.log("Não!!")
    }
}