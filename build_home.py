from partials import page

ICONS = {
 1: '<svg viewBox="0 0 24 24"><path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 2: '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/><path d="M8 11l6 0"/></svg>',
 3: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/><path d="M12 12l4-4"/></svg>',
 4: '<svg viewBox="0 0 24 24"><path d="M4 9l16-5-5 16-3-6-3 2v-4z"/></svg>',
 5: '<svg viewBox="0 0 24 24"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M10.3 21a2 2 0 0 0 3.4 0"/></svg>',
 6: '<svg viewBox="0 0 24 24"><path d="M3 8l18-4-3 12-5-2-3 4-2-6z"/></svg>',
}
STEPS = [
 ("TELL US","Choose your destination, date and preferences."),
 ("SEARCH","BTicket searches available flights and trains."),
 ("MONITOR","If your ticket isn’t available, we keep looking."),
 ("FOUND","A matching ticket becomes available."),
 ("NOTIFY","You receive an instant notification."),
 ("TRAVEL","Book your journey and go."),
]

PRE = '''<header class="mast">
<div class="mast-photo" style="background-image:url(assets/img/airplane.jpg)"></div>
<div class="mast-fade"></div>
<div class="container">
<div class="mast-in">
<span class="hero-badge">✦ Automated travel booking</span>
<h1>Your journey.<br><span class="grad">We find the way.</span></h1>
<p class="sub">Tell us where you want to go. BTicket searches for the right flight or train and helps you secure your journey.</p>
<div class="mast-stats">
<div><b>2M+</b><span>happy passengers</span></div>
<div><b>40+</b><span>routes nationwide</span></div>
<div><b>4.9★</b><span>app rating</span></div>
</div>
</div>
<div class="booking" id="booking">
<div class="book-card" id="homeBookCard">
<div class="tabs">
<button class="tab active" type="button" data-mode="flights">✈ Flights</button>
<button class="tab" type="button" data-mode="trains">🚆 Trains</button>
</div>
<div class="panel active" id="hp-flights">
<div class="fields">
<div class="field"><small>FROM</small><select id="hf-from"><option>Tashkent</option><option>Samarkand</option><option>Bukhara</option><option>Khiva</option></select></div>
<button class="swap" data-swap="f" type="button">⇄</button>
<div class="field"><small>TO</small><select id="hf-to"><option value="Dubai" selected>Dubai</option><option>Istanbul</option><option>Seoul</option><option>London</option></select></div>
<div class="field"><small>DATE</small><input id="hf-date" type="date" value="2026-09-27" /></div>
<div class="field"><small>PASSENGERS</small><select id="hf-pax"><option>1 Adult</option><option>2 Adults</option><option>3 Adults</option></select></div>
</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button" data-go="flights">Search tickets →</button>
</div>
<div class="panel" id="hp-trains">
<div class="fields">
<div class="field"><small>FROM</small><select id="ht-from"><option selected>Tashkent</option><option>Samarkand</option><option>Bukhara</option><option>Khiva</option></select></div>
<button class="swap" data-swap="t" type="button">⇄</button>
<div class="field"><small>TO</small><select id="ht-to"><option>Tashkent</option><option selected>Samarkand</option><option>Bukhara</option><option>Khiva</option></select></div>
<div class="field"><small>DATE</small><input id="ht-date" type="date" value="2026-09-27" /></div>
<div class="field"><small>PASSENGERS</small><select id="ht-pax"><option>1 Adult</option><option>2 Adults</option><option>3 Adults</option></select></div>
</div>
<button class="btn-cta lg" style="width:100%;margin-top:16px" type="button" data-go="trains">Search tickets →</button>
</div>
</div>
</div>
</div>
</header>

<main class="container">
<section class="section" id="active-search">
<div class="sec-head"><h2>Active ticket search</h2><p>You don’t need to keep checking. BTicket does it for you.</p></div>
<div class="st3" id="statusBar">
<div class="st3c on" data-st="hard"><div class="dot red">🔴</div><b>Hard to find</b><p>Few matching tickets currently available.</p></div>
<div class="st3c" data-st="search"><div class="dot amber">🟡</div><b>Searching</b><p>BTicket is actively checking availability.</p></div>
<div class="st3c" data-st="found"><div class="dot green">🟢</div><b>Found in 5 sec</b><p>A matching ticket was found.</p></div>
</div>
<div class="anim-bar"><i></i></div>
<div class="search-card" style="max-width:520px;margin:30px auto 0" id="liveSearch">
<div style="display:flex;justify-content:space-between;align-items:center">
<b style="font-size:.75rem;letter-spacing:.1em;color:#8a97ad">ACTIVE TICKET SEARCH</b>
<span class="status amber" id="liveStatus"><span class="p-dot"></span>Searching</span>
</div>
<div class="route" style="margin-top:14px">Tashkent → Dubai</div>
<div class="meta2">27 September 2026 • 1 passenger</div>
<div style="color:var(--mut);font-size:.9rem" id="liveNote">BTicket is monitoring available tickets.</div>
<div class="progress" style="margin-top:14px"><i style="animation-duration:1.6s"></i></div>
</div>
</section>

<section class="section" id="destinations">
<div class="sec-head"><h2>Where would you go?</h2><p>Six destinations, one search. Choose where next.</p></div>
<div class="dest-grid six">
<div class="dest photo lz" data-bg="assets/img/dubai.jpg"><div class="tint"></div><div class="info"><div><b>Dubai</b><span>United Arab Emirates</span></div><span class="go">→</span></div></div>
<div class="dest photo lz" data-bg="assets/img/istanbul.jpg"><div class="tint"></div><div class="info"><div><b>Istanbul</b><span>Turkey</span></div><span class="go">→</span></div></div>
<div class="dest photo lz" data-bg="assets/img/seoul.jpg"><div class="tint"></div><div class="info"><div><b>Seoul</b><span>South Korea</span></div><span class="go">→</span></div></div>
<div class="dest photo lz" data-bg="assets/img/samarkand.jpg"><div class="tint"></div><div class="info"><div><b>Samarkand</b><span>Uzbekistan</span></div><span class="go">→</span></div></div>
<div class="dest photo lz" data-bg="assets/img/bukhara.jpg"><div class="tint"></div><div class="info"><div><b>Bukhara</b><span>Uzbekistan</span></div><span class="go">→</span></div></div>
<div class="dest photo lz" data-bg="assets/img/tashkent.jpg"><div class="tint"></div><div class="info"><div><b>Tashkent</b><span>Uzbekistan</span></div><span class="go">→</span></div></div>
</div>
</section>

<section class="section" id="how">
<div class="sec-head"><h2>How BTicket works</h2><p>From your request to your journey — we handle the searching.</p></div>
<div class="steps">'''

MID = "</div></section>"

POST = '''
<section class="section" style="padding-bottom:72px">
<div class="final-photo">
<div class="ph lz" data-bg="assets/img/train.jpg"></div>
<div class="ov"></div>
<div class="fc">
<h2>Where will you go next?</h2>
<p>Let BTicket find the ticket.</p>
<a class="btn-cta lg" style="text-decoration:none;display:inline-block" href="flights/" id="finalStart">Start searching →</a>
</div>
</div>
</section>
</main>

<script>
document.querySelectorAll(".tab[data-mode]").forEach(t => t.addEventListener("click", () => {
  document.querySelectorAll(".tab[data-mode]").forEach(x => x.classList.remove("active"));
  document.querySelectorAll("[id^=hp-]").forEach(x => x.classList.remove("active"));
  t.classList.add("active"); document.getElementById("hp-" + t.dataset.mode).classList.add("active");
}));
document.querySelectorAll("[data-swap]").forEach(b => b.addEventListener("click", () => {
  const pfx = b.dataset.swap, a = document.getElementById("h"+pfx+"-from"), t = document.getElementById("h"+pfx+"-to");
  const v = a.value; a.value = t.value; t.value = v;
}));
document.querySelectorAll("[data-go]").forEach(b => b.addEventListener("click", () => {
  const m = b.dataset.go, f = m === "flights" ? "f" : "t";
  const from = document.getElementById("h"+f+"-from").value, to = document.getElementById("h"+f+"-to").value;
  const date = document.getElementById("h"+f+"-date").value, pax = document.getElementById("h"+f+"-pax").value;
  const url = window.BT_ROOT + m + "/?from=" + encodeURIComponent(from) + "&to=" + encodeURIComponent(to) + "&date=" + date + "&pax=" + encodeURIComponent(pax);
  if (!btAuthed()) { btGate(url); return; }
  location.href = url;
}));
/* final CTA: gate for guests, direct for users */
(function(){
  const fs = document.getElementById("finalStart");
  if (fs) fs.addEventListener("click", e => {
    if (!btAuthed()) { e.preventDefault(); btGate(window.BT_ROOT + "flights/"); }
  });
})();
/* lazy-load destination and CTA photos */
(function(){
  var els = Array.prototype.slice.call(document.querySelectorAll("[data-bg]"));
  function load(el){ el.style.backgroundImage = "url(" + el.dataset.bg + ")"; el.classList.remove("lz"); }
  function check(){
    var vh = Math.max(window.innerHeight || 0, 600);
    els = els.filter(function(el){
      if (!el) return false;
      var r = el.getBoundingClientRect();
      if (r.top <= vh + 300 && r.bottom >= -300){ load(el); return false; }
      return true;
    });
  }
  check();
  window.addEventListener("scroll", check, { passive: true });
})();
const states = [
  {cl:"hard", label:"Hard to find", note:"BTicket is monitoring available tickets."},
  {cl:"search", label:"Searching", note:"BTicket is actively checking availability."},
  {cl:"found", label:"Found in 5 sec", note:"A matching ticket was found. Check your notifications."},
];
let si = 0;
setInterval(() => {
  si = (si + 1) % 3;
  const s = states[si];
  document.querySelectorAll(".st3 .st3c").forEach(c => c.classList.toggle("on", c.dataset.st === s.cl));
  const st = document.getElementById("liveStatus");
  st.className = "status " + (s.cl==="found" ? "green" : (s.cl==="search" ? "amber" : ""));
  st.innerHTML = '<span class="p-dot"></span>' + s.label;
  document.getElementById("liveNote").textContent = s.note;
}, 3200);
</script>
'''

steps_html = "".join(
    '<div class="step on"><div class="si">' + ICONS[s] + '</div><div class="sn">0' + str(s) + '</div><div class="sname">' + nm + '</div><p>' + tx + '</p></div>'
    for s, (nm, tx) in enumerate(STEPS, 1)
)
body = PRE + steps_html + MID + POST
open("index.html","w").write(page("BTicket — Your journey. We find the way.", body, "Flights"))
print("index.html bytes:", len(body))
