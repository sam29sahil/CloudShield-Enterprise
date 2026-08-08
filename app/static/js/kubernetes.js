/*
==========================================
CloudShield Enterprise
Kubernetes JavaScript
==========================================
*/

document.addEventListener(

    "DOMContentLoaded",
    
    function(){
    
    console.log(
    
    "CloudShield Kubernetes Loaded"
    
    );
    
    initializeCards();
    
    initializeTables();
    
    initializeHealth();
    
    initializeTooltips();
    
    }
    
    );
    
    function initializeCards(){
    
    document
    
    .querySelectorAll(".resource-card")
    
    .forEach(function(card){
    
    card.addEventListener(
    
    "mouseenter",
    
    function(){
    
    card.style.boxShadow=
    
    "0 10px 25px rgba(0,0,0,.15)";
    
    }
    
    );
    
    card.addEventListener(
    
    "mouseleave",
    
    function(){
    
    card.style.boxShadow="";
    
    }
    
    );
    
    });
    
    }
    
    function initializeTables(){
    
    document
    
    .querySelectorAll("table")
    
    .forEach(function(table){
    
    table.classList.add(
    
    "table-striped"
    
    );
    
    });
    
    }
    
    function initializeHealth(){
    
    const badges=document.querySelectorAll(
    
    ".badge"
    
    );
    
    badges.forEach(function(badge){
    
    const text=badge.innerText.toLowerCase();
    
    if(text.includes("healthy")){
    
    badge.classList.add("bg-success");
    
    }
    
    if(text.includes("critical")){
    
    badge.classList.add("bg-danger");
    
    }
    
    if(text.includes("warning")){
    
    badge.classList.add("bg-warning");
    
    }
    
    });
    
    }
    
    function initializeTooltips(){
    
    const triggers=[].slice.call(
    
    document.querySelectorAll(
    
    '[data-bs-toggle="tooltip"]'
    
    )
    
    );
    
    triggers.forEach(function(el){
    
    new bootstrap.Tooltip(el);
    
    });
    
    }
    
    function refreshDashboard(){
    
    location.reload();
    
    }
    
    function searchTable(inputId,tableId){
    
    const input=document.getElementById(inputId);
    
    const filter=input.value.toLowerCase();
    
    const rows=document
    
    .getElementById(tableId)
    
    .getElementsByTagName("tr");
    
    for(let i=1;i<rows.length;i++){
    
    const row=rows[i];
    
    const text=row.innerText.toLowerCase();
    
    row.style.display=
    
    text.includes(filter)
    
    ? ""
    
    : "none";
    
    }
    
    }
    
    function exportTableCSV(filename){
    
    let csv=[];
    
    document
    
    .querySelectorAll("table tr")
    
    .forEach(function(row){
    
    let cols=row.querySelectorAll(
    
    "td,th"
    
    );
    
    let data=[];
    
    cols.forEach(function(col){
    
    data.push(col.innerText);
    
    });
    
    csv.push(data.join(","));
    
    });
    
    let blob=new Blob(
    
    [csv.join("\n")],
    
    {type:"text/csv"}
    
    );
    
    let link=document.createElement("a");
    
    link.download=filename;
    
    link.href=
    
    window.URL.createObjectURL(blob);
    
    link.click();
    
    }