require([
    "jquery",
    "splunkjs/mvc/searchmanager",
    "splunkjs/mvc/simplexml/ready!"
], function(
    $,
    SearchManager
) {
    var mysearch = new SearchManager({
        id: "mysearch",
        autostart: "false",
        search: "| update" 
    });
    $(".button1").on("click", function (){
        var ok = confirm("Are you sure?");
        if (ok){
            mysearch.startSearch();
            alert('Please restart Splunk or run debug/refresh to make changes effective! But wait 10min before doing it to ensure the script was finished.');
        } 
    });
});
