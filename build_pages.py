import os
from partials import page, phero, search_widget

def write(path, title, body, active=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(page(title, body, active))
    print(path, len(body))

# ============ FLIGHTS ============
FL_HEAD = phero("Flights", "Search, compare and book flights. If the perfect option isn’t available yet, BTicket monitors availability for you.", "Flights")
FL_WIDGET = search_widget("fl", ["Tashkent","Samarkand","Bukhara","Khiva"], ["Dubai","Istanbul","Seoul","London"], "fl-go")
FL_BODY = (FL_HEAD + '''
<div class="container" style="padding-bottom:56px">
''' + FL_WIDGET + '''
<div style="margin-top:18px" id="fl-book"><div class="bill" style="max-width:520px;margin:0 auto">
<h3>Booking summary</h3>
<div class="brow"><span>Ticket price</span><b id="fb-ticket">—</b></div>
<div class="brow"><span>BTicket service fee <span class="mut">(10%)</span></span><b id="fb-fee">—</b></div>
<div class="brow total"><span>Total</span><b id="fb-total">—</b></div>
<div class="fee-note">Service fees are always shown before you pay.</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button" id="fb-confirm">Continue to booking →</button>
</div></div>
</div>
<script>
const FLIGHTS = [
 {air:"Uzbekistan Airways", code:"HY-201", dep:"07:15", arr:"11:40", dur:"4h 25m", stops:0, bag:1, price:180},
 {air:"Flydubai", code:"FZ-1940", dep:"09:40", arr:"13:25", dur:"3h 45m", stops:0, bag:0, price:240},
 {air:"Uzbekistan Airways", code:"HY-305", dep:"14:05", arr:"18:50", dur:"4h 45m", stops:1, bag:1, price:215},
 {air:"Emirates", code:"EK-2129", dep:"21:30", arr:"01:55+1", dur:"4h 25m", stops:1, bag:1, price:165}
];
const q = new URLSearchParams(location.search);
document.querySelectorAll("[data-swap]").forEach(b => b.addEventListener("click", () => {
  const a = document.getElementById(b.dataset.swap+"-from"), t = document.getElementById(b.dataset.swap+"-to");
  const v = a.value; a.value = t.value; t.value = v;
}));
function filterList(){
  let l = FLIGHTS.slice();
  const sort = document.querySelector(".flt-sort[data-set=fl]").value;
  l.sort((a,b) => sort === "asc" ? a.price-b.price : b.price-a.price);
  if (document.querySelector(".flt-direct[data-set=fl]").checked) l = l.filter(f => f.stops===0);
  if (document.querySelector(".flt-bag[data-set=fl]").checked) l = l.filter(f => f.bag>0);
  const dep = document.querySelector(".flt-dep[data-set=fl]").value;
  if (dep==="am") l = l.filter(f => f.dep < "12:00");
  if (dep==="pm") l = l.filter(f => f.dep >= "12:00");
  return l;
}
function render(){
  const from = document.getElementById("fl-from").value, to = document.getElementById("fl-to").value;
  const list = filterList();
  document.getElementById("fl-tickets").innerHTML = list.length===0
    ? '<div class="res-detail" style="grid-template-columns:1fr;text-align:center;color:var(--mut)">No flights match these filters.</div>'
    : list.map(f => {
      const fee = Math.round(f.price*0.1);
      return '<div class="res-detail" style="grid-template-columns:1.4fr auto auto 1fr auto auto">' +
        '<div class="airline">'+f.air+'<span style="color:var(--mut);font-size:.8rem;font-weight:600"> '+f.code+'</span></div>' +
        '<div class="seg"><b>'+f.dep+'</b><span>'+from+'</span></div>' +
        '<div class="dur"><span class="ln"></span>'+f.dur+(f.stops===0?' • direct':' • '+f.stops+' stop')+'</div>' +
        '<div class="seg"><b>'+f.arr+'</b><span>'+to+'</span></div>' +
        '<div class="price"><b>$'+f.price+'</b><span>ticket $'+f.price+' + fee $'+fee+'</span></div>' +
        '<button class="selectBtn" data-price="'+f.price+'" type="button">Select</button></div>';
    }).join("");
  document.querySelectorAll("#fl-tickets .selectBtn").forEach(btn => btn.addEventListener("click", () => {
    const pr = +btn.dataset.price, fee = Math.round(pr*0.1);
    document.getElementById("fb-ticket").textContent = "$"+pr;
    document.getElementById("fb-fee").textContent = "$"+fee;
    document.getElementById("fb-total").textContent = "$"+(pr+fee);
    btn.textContent = "Selected ✓"; btn.disabled = true;
    document.getElementById("fl-book").scrollIntoView({behavior:"smooth", block:"center"});
  }));
}
document.querySelectorAll("#fl-filters select, #fl-filters input").forEach(el => el.addEventListener("change", render));
function go(){
  const from = document.getElementById("fl-from").value, to = document.getElementById("fl-to").value;
  const err = document.getElementById("fl-err"); err.textContent = "";
  if (from===to) { err.textContent = "Please choose a different destination."; return; }
  document.querySelector(".widget-in").style.display = "none";
  document.getElementById("fl-loading").style.display = "block";
  document.getElementById("fl-loading").scrollIntoView({behavior:"smooth"});
  setTimeout(() => { document.getElementById("fl-loading").style.display = "none"; document.getElementById("fl-results").style.display = "grid"; render(); }, 1800);
}
document.getElementById("fl-go").addEventListener("click", go);
document.getElementById("fb-confirm").addEventListener("click", e => { e.currentTarget.textContent = "Booking requested ✓"; e.currentTarget.disabled = true; });
if(q.has("from")) document.getElementById("fl-from").value = q.get("from");
if(q.has("to")) document.getElementById("fl-to").value = q.get("to");
if(q.has("date")) document.getElementById("fl-date").value = q.get("date");
if(q.has("pax")) document.getElementById("fl-pax").value = q.get("pax");
if(q.has("from") || q.has("to")) go();
</script>''')
write("flights/index.html", "Flights — BTicket", FL_BODY, "Flights")

# ============ TRAINS ============
TR_HEAD = phero("Trains", "High-speed rail across Uzbekistan. Search, compare classes and select your train.", "Trains")
TR_WIDGET = search_widget("tr", ["Tashkent","Samarkand","Bukhara","Khiva"], ["Tashkent","Samarkand","Bukhara","Khiva"], "tr-go")
TR_BODY = (TR_HEAD + '''
<div class="container" style="padding-bottom:56px">
''' + TR_WIDGET + '''
<div style="margin-top:18px" id="tr-book"><div class="bill" style="max-width:520px;margin:0 auto">
<h3>Booking summary</h3>
<div class="brow"><span>Ticket price</span><b id="tb-ticket">—</b></div>
<div class="brow"><span>BTicket service fee <span class="mut">(10%)</span></span><b id="tb-fee">—</b></div>
<div class="brow total"><span>Total</span><b id="tb-total">—</b></div>
<div class="fee-note">Service fees are always shown before you pay.</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button" id="tb-confirm">Select train ✅</button>
</div></div>
</div>
<script>
const TRAINS = [
 {name:"Afrosiyob", code:"760F", dep:"07:28", arr:"11:05", dur:"3h 37m", cls:"Economy / Business", seats:14, price:124000},
 {name:"Afrosiyob", code:"762F", dep:"13:15", arr:"16:55", dur:"3h 40m", cls:"Economy / Business", seats:6, price:136000},
 {name:"Sharq", code:"704F", dep:"19:40", arr:"23:28", dur:"3h 48m", cls:"Economy / Coupe", seats:22, price:116000}
];
function fmtUZS(n){ return n.toLocaleString("en-US").replace(/,/g," ")+" UZS"; }
const q = new URLSearchParams(location.search);
document.querySelectorAll("[data-swap]").forEach(b => b.addEventListener("click", () => {
  const a = document.getElementById(b.dataset.swap+"-from"), t = document.getElementById(b.dataset.swap+"-to");
  const v = a.value; a.value = t.value; t.value = v;
}));
function render(){
  const from = document.getElementById("tr-from").value, to = document.getElementById("tr-to").value;
  document.getElementById("tr-tickets").innerHTML = TRAINS.map(t => {
    const fee = Math.round(t.price*0.1);
    return '<div class="res-detail" style="grid-template-columns:1.4fr auto auto 1fr auto auto">' +
      '<div class="airline">🚆<div><b>'+t.name+'</b><span style="color:var(--mut);font-size:.8rem;font-weight:600"> '+t.code+'</span></div></div>' +
      '<div class="seg"><b>'+t.dep+'</b><span>'+from+'</span></div>' +
      '<div class="seg"><b>'+t.arr+'</b><span>'+to+'</span></div>' +
      '<div class="dur"><span class="ln"></span>'+t.dur+' • '+t.cls+' • '+t.seats+' seats left</div>' +
      '<div class="price"><b>'+fmtUZS(t.price)+'</b><span>fee '+fmtUZS(fee)+'</span></div>' +
      '<button class="selectBtn" data-price="'+t.price+'" type="button">Select</button></div>';
  }).join("");
  document.querySelectorAll("#tr-tickets .selectBtn").forEach(btn => btn.addEventListener("click", () => {
    const pr = +btn.dataset.price, fee = Math.round(pr*0.1);
    document.getElementById("tb-ticket").textContent = fmtUZS(pr);
    document.getElementById("tb-fee").textContent = fmtUZS(fee);
    document.getElementById("tb-total").textContent = fmtUZS(pr+fee);
    btn.textContent = "Selected ✓"; btn.disabled = true;
    document.getElementById("tr-book").scrollIntoView({behavior:"smooth", block:"center"});
  }));
}
function go(){
  const from = document.getElementById("tr-from").value, to = document.getElementById("tr-to").value;
  const err = document.getElementById("tr-err"); err.textContent = "";
  if (from===to) { err.textContent = "Please choose a different destination."; return; }
  document.querySelector(".widget-in").style.display = "none";
  document.getElementById("tr-loading").style.display = "block";
  document.getElementById("tr-loading").scrollIntoView({behavior:"smooth"});
  setTimeout(() => { document.getElementById("tr-loading").style.display = "none"; document.getElementById("tr-results").style.display = "grid"; render(); }, 1800);
}
document.getElementById("tr-go").addEventListener("click", go);
document.getElementById("tb-confirm").addEventListener("click", e => { e.currentTarget.textContent = "Ticket selected ✓"; e.currentTarget.disabled = true; });
if(q.has("from")) document.getElementById("tr-from").value = q.get("from");
if(q.has("to")) document.getElementById("tr-to").value = q.get("to");
if(q.has("date")) document.getElementById("tr-date").value = q.get("date");
if(q.has("pax")) document.getElementById("tr-pax").value = q.get("pax");
if(q.has("from") || q.has("to")) go();
</script>''')
write("trains/index.html", "Trains — BTicket", TR_BODY, "Trains")
