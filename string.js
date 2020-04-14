//charAt = vai ate a string escolhida
const name = "Gustavo";

console.log(name.charAt(5));
//comecando em 0, vai mostrar a letra v

// -----------------------------------

//codigo asssociado ao numero ou letra escolhido (hexadecimal?)
console.log(name.charCodeAt(2));

//indexOf (tenho o digito quero saber em que indicie aquele digito esta na palavra ou frase)
console.log(name.indexOf('u'));
//vai mostrar o numero 1 pois se inicia em 0

//------------------------------------

//substring vai a partir do indice escolhido até o final da palavra ou frase
console.log(name.substring(3)); //tavo

//tambem com o substring pode se ir ao indice escolhido por intervalos
console.log(name.substring(0, 3)); //Gus

// ------------------------------

//concatenacao
console.log('Luis '.concat(name).concat('.')); //Luis Gustavo.

//replace faz a substituicao do indice escolhido uma vez ou por um todo
console.log(name.replace('o', 'a')); //Gustava

// ------------------

//split cria array com a espaçamento de escolha
console.log('Pão,Leite,Coca'.split(',')); //[Pao, Leite, Coca]



