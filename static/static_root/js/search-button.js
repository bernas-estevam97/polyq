var input = document.getElementById('myInput');

document.getElementById('myButton').onclick = function() {
   if (input.value == "Huntington's disease"){
      location.assign("../diseases/hd");
   } else if (input.value.toLowerCase() == "hd"){
      location.assign("../diseases/hd");
   } else if (input.value == "Dentatorubral-pallidoluysian atrophy"){
      location.assign("../diseases/drpla");
   } else if (input.value.toLowerCase() == "drpla"){
      location.assign("../diseases/drpla");
   } else if (input.value == "Spinal-bulbar muscular atrophy"){
      location.assign("../diseases/sbma");
   } else if (input.value.toLowerCase() =="sbma"){
      location.assign("../diseases/sbma");
   } else if (input.value == "Spinocerebellar ataxia type 1"){
      location.assign("../diseases/sca1");
   } else if (input.value.toLowerCase() == "sca1"){
      location.assign("../diseases/sca1");
   } else if (input.value == "Spinocerebellar ataxia type 2"){
         location.assign("../diseases/sca2");
   } else if (input.value.toLowerCase() == "sca2"){
      location.assign("../diseases/sca2");
   } else if (input.value == "Spinocerebellar ataxia type 3"){
         location.assign("../diseases/sca3");
   } else if (input.value.toLowerCase() == "sca3"){
         location.assign("../diseases/sca3");
      } else if (input.value == "Spinocerebellar ataxia type 6"){
            location.assign("../diseases/sca6");
   } else if (input.value.toLowerCase() == "sca6"){
         location.assign("../diseases/sca6");
      } else if (input.value == "Spinocerebellar ataxia type 7"){
            location.assign("../diseases/sca7");
   } else if (input.value.toLowerCase() == "sca7"){
         location.assign("../diseases/sca7");
      } else if (input.value == "Spinocerebellar ataxia type 17"){
               location.assign("../diseases/sca17");
   } else if (input.value.toLowerCase() == "sca17"){
            location.assign("../diseases/sca17");
   } else if (input.value.toLowerCase() == ""){
      return alert('Fill the text box.');
   } else {
      return alert('Error. No such disease');
   }
   return 1;
};

// On enter key pressed same thing as clicking button
input.onkeydown = function(e){
   if(e.keyCode == 13){
      if (input.value == "Huntington's disease"){
         location.assign("../diseases/hd");
      } else if (input.value.toLowerCase() == "hd"){
         location.assign("../diseases/hd");
      } else if (input.value == "Dentatorubral-pallidoluysian atrophy"){
         location.assign("../diseases/drpla");
      } else if (input.value.toLowerCase() == "drpla"){
         location.assign("../diseases/drpla");
      } else if (input.value == "Spinal-bulbar muscular atrophy"){
         location.assign("../diseases/sbma");
      } else if (input.value.toLowerCase() =="sbma"){
         location.assign("../diseases/sbma");
      } else if (input.value == "Spinocerebellar ataxia type 1"){
         location.assign("../diseases/sca1");
      } else if (input.value.toLowerCase() == "sca1"){
         location.assign("../diseases/sca1");
      } else if (input.value == "Spinocerebellar ataxia type 2"){
            location.assign("../diseases/sca2");
      } else if (input.value.toLowerCase() == "sca2"){
         location.assign("../diseases/sca2");
      } else if (input.value == "Spinocerebellar ataxia type 3"){
            location.assign("../diseases/sca3");
      } else if (input.value.toLowerCase() == "sca3"){
            location.assign("../diseases/sca3");
         } else if (input.value == "Spinocerebellar ataxia type 6"){
               location.assign("../diseases/sca6");
      } else if (input.value.toLowerCase() == "sca6"){
            location.assign("../diseases/sca6");
         } else if (input.value == "Spinocerebellar ataxia type 7"){
               location.assign("../diseases/sca7");
      } else if (input.value.toLowerCase() == "sca7"){
            location.assign("../diseases/sca7");
         } else if (input.value == "Spinocerebellar ataxia type 17"){
                  location.assign("../diseases/sca17");
      } else if (input.value.toLowerCase() == "sca17"){
               location.assign("../diseases/sca17");
      } else if (input.value.toLowerCase() == ""){
         return alert('Fill the text box.');
      }
       else {
         return alert('Error. No such disease');
      }
      return 1;
   }
};
