$(document).ready(function(){
     $("#amount").inputmask("decimal",{
         radixPoint:".", 
         groupSeparator: ",", 
         digits: 2,
         autoGroup: true,
         prefix: '$'
     });
});