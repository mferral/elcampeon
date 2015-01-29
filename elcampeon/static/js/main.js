 $(document).ready(function() {

     $(document).foundation({
         orbit: {
             slide_number: false,
             bullets: false,
         }
     });

     $(".inicioBtn").click(function() {
         $("#superCont").load("pages/home.html");
     });

     $(".entryMasBtn").click(function() {
         $("#superCont").load("pages/entry.html");
     });

     $(".deporteLocalBtn").click(function() {
         $("#superCont").load("pages/deporteLocal.html");
     });

     $(".correcaminosBtn").click(function() {
         $("#superCont").load("pages/correcaminos.html");
     });


 });
