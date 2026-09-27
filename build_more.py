import os
from partials import page, phero

def write(path, title, body, active=None, guard=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(page(title, body, active, guard))
    print(path, len(body))

# ============ ACTIVE SEARCHES ============
AS = phero("Active searches", "Your automatic ticket monitoring. BTicket watches availability and target prices around the clock.", "Active searches")
AS += '''
<div class="container" style="padding-bottom:56px">
<div class="panel-card">
<h3>🔍 Your active searches</h3>
<div class="search-row">
<div><div class="route">Tashkent → Dubai</div><div class="prefs">27 September 2026 • 1 passenger • Target price: $300</div></div>
<span class="status amber" style="margin-left:8px"><span class="p-dot"></span>Searching</span>
<span class="badge" style="margin-left:2px">Availability: 🟡 Medium</span>
<div class="actions"><button class="btn-sm" type="button">Pause search</button><button class="btn-sm danger" type="button">Cancel search</button></div>
</div>
<div class="search-row">
<div><div class="route">Tashkent → Samarkand</div><div class="prefs">3 October 2026 • 2 passengers • Afrosiyob preferred</div></div>
<span class="status green" style="margin-left:8px"><span class="p-dot"></span>Found in 5 sec</span>
<span class="badge" style="margin-left:2px">Availability: 🟢 High</span>
<div class="actions"><button class="btn-sm" type="button">View ticket</button><button class="btn-sm danger" type="button">Cancel search</button></div>
</div>
<div class="search-row">
<div><div class="route">Tashkent → Istanbul</div><div class="prefs">14 October 2026 • 1 passenger • Target price: $260</div></div>
<span class="status amber" style="margin-left:8px"><span class="p-dot"></span>Searching</span>
<span class="badge" style="margin-left:2px">Availability: 🔴 Low</span>
<div class="actions"><button class="btn-sm" type="button">Pause search</button><button class="btn-sm danger" type="button">Cancel search</button></div>
</div>
</div>
<div class="panel-card" style="margin-top:18px">
<h3>💰 Price alerts</h3>
<div class="hist-row"><div><div class="route">Tashkent → Dubai</div><div class="date">Max $300 • 27 September</div></div><span class="badge-st ok" style="margin-left:auto">Active</span><button class="btn-sm danger" type="button">Delete</button></div>
<div class="hist-row"><div><div class="route">Tashkent → London</div><div class="date">Max $400 • 20 December</div></div><span class="badge-st ok" style="margin-left:auto">Active</span><button class="btn-sm danger" type="button">Delete</button></div>
</div>
<div class="score-card" style="margin-top:24px">
<div class="score-dot">🟡</div>
<div class="score-label">Medium availability</div>
<p>BTicket Availability Score is based on currently available booking inventory and your selected travel criteria.</p>
</div>
</div>'''
write("active-searches/index.html", "Active searches — BTicket", AS, guard=True)

# ============ MY BOOKINGS ============
MB = phero("My bookings", "Confirmed and previous bookings — with digital tickets always at hand.", "My bookings")
MB += '''
<div class="container" style="padding-bottom:56px">
<div class="stat-grid" style="margin-bottom:20px">
<div class="stat-card"><b>2</b><span>Upcoming trips</span></div>
<div class="stat-card"><b>5</b><span>Completed trips</span></div>
<div class="stat-card"><b>1</b><span>Cancelled</span></div>
<div class="stat-card"><b>120,000</b><span>UZS total saved</span></div>
</div>
<div class="panel-card">
<h3>🎫 Booking history</h3>
<div class="hist-row"><div><div class="route">Tashkent → Samarkand</div><div class="date">27 Sep 2026 • Afrosiyob 760F</div></div><span class="badge-st ok" style="margin-left:auto">CONFIRMED</span><button class="btn-sm" type="button">View ticket</button></div>
<div class="hist-row"><div><div class="route">Tashkent → Istanbul</div><div class="date">14 Oct 2026 • HY-201</div></div><span class="badge-st done" style="margin-left:auto">COMPLETED</span></div>
<div class="hist-row"><div><div class="route">Tashkent → Dubai</div><div class="date">02 Nov 2026 • EK-2129</div></div><span class="badge-st cancel" style="margin-left:auto">CANCELLED</span><button class="btn-sm" type="button">Refund</button></div>
</div>
<div class="panel-card" style="margin-top:18px">
<h3>🎟 Latest digital ticket</h3>
<div class="dticket">
<div class="dt-top"><div class="logo2"><span class="logo-mark" style="width:28px;height:28px;border-radius:9px">B</span>BTicket</div><span class="badge-st ok" style="background:rgba(255,255,255,.16);color:#fff">CONFIRMED</span></div>
<div class="dt-main">
<div class="dt-route">TAS <span class="ln"></span> SKD</div>
<div style="color:var(--mut);font-size:.85rem;margin-top:6px">Tashkent → Samarkand • 27 September 2026</div>
<div class="dt-cols">
<div><span>PASSENGER</span><b>Ulugbek M.</b></div>
<div><span>TRAIN</span><b>Afrosiyob 760F</b></div>
<div><span>DEPARTURE</span><b>07:28</b></div>
<div><span>ARRIVAL</span><b>11:05</b></div>
<div><span>SEAT</span><b>Car 5 · Seat 42</b></div>
<div><span>BOOKING ID</span><b>BT-8842-19</b></div>
</div>
<div class="dt-qr">
<div class="qr" id="qr"></div>
<div><b style="font-size:.95rem">Scan at the station gate</b><div style="color:var(--mut);font-size:.85rem;margin-top:4px">Show this QR code before boarding.</div></div>
</div>
<div class="dt-actions"><button class="dt-st" type="button">⬇ Download ticket</button><button class="dt-st" type="button">📱 Add to wallet</button><button class="dt-st" type="button">🔗 Share</button></div>
</div>
</div>
</div>
</div>
<script>
(function drawQr(){
  const qr = document.getElementById("qr");
  let cells = "";
  for (let i = 0; i < 49; i++){
    const finder = (i%7 < 2 || i%7 > 4) && (Math.floor(i/7) < 2 || Math.floor(i/7) > 4);
    cells += "<i style='opacity:" + (finder ? 1 : Math.random() > .5 ? 1 : 0) + "'></i>";
  }
  qr.innerHTML = cells;
})();
</script>'''
write("my-bookings/index.html", "My bookings — BTicket", MB, guard=True)

# ============ NOTIFICATIONS ============
NT = phero("Notifications", "Ticket found, bookings, price alerts and payments — all in one centre.", "Notifications")
NT += '''
<div class="container" style="padding-bottom:56px">
<div class="panel-card">
<h3>🔔 Notification centre</h3>
<div class="ntf-tabs">
<button class="ntf-tab active" data-ntf="all" type="button">All</button>
<button class="ntf-tab" data-ntf="tickets" type="button">Tickets</button>
<button class="ntf-tab" data-ntf="bookings" type="button">Bookings</button>
<button class="ntf-tab" data-ntf="alerts" type="button">Price alerts</button>
<button class="ntf-tab" data-ntf="payments" type="button">Payments</button>
<button class="ntf-tab" data-ntf="system" type="button">System</button>
</div>
<div id="ntfList">
<div class="ntf-row" data-cat="tickets"><div class="nic">🎟</div><div><b>Ticket found</b><p>Tashkent → Dubai</p></div><span class="ago">2 minutes ago</span></div>
<div class="ntf-row" data-cat="bookings"><div class="nic">✅</div><div><b>Booking confirmed</b><p>Tashkent → Samarkand</p></div><span class="ago">1 hour ago</span></div>
<div class="ntf-row" data-cat="alerts"><div class="nic">💰</div><div><b>Price alert</b><p>Ticket price dropped</p></div><span class="ago">Today</span></div>
<div class="ntf-row" data-cat="payments"><div class="nic">💳</div><div><b>Payment received</b><p>Booking BT-8842-19</p></div><span class="ago">Yesterday</span></div>
<div class="ntf-row" data-cat="system"><div class="nic">🛠</div><div><b>Scheduled maintenance</b><p>Oct 3, 02:00–03:00 (UTC+5)</p></div><span class="ago">3 days ago</span></div>
</div>
</div>
<div class="notif-grid" style="margin-top:20px">
<div class="notif-card"><div class="cap">🖥 DESKTOP</div><div class="win"><div class="top"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i></div><div class="body"><b>🎟 BTicket found a match!</b><div style="color:var(--mut);font-size:.78rem">Tashkent → Dubai • 27 Sep 2026</div></div></div></div>
<div class="notif-card" style="text-align:center"><div class="cap">📱 MOBILE</div><div class="phone" style="width:130px"><div class="notch"></div><div class="scr"><div style="background:#0e1b33;border-radius:10px;color:#fff;padding:9px;font-size:.68rem;font-weight:700">🎟 BTicket<div style="font-weight:400;margin-top:2px">Tashkent → Dubai — ticket ready.</div></div></div></div></div>
<div class="notif-card"><div class="cap">✈ TELEGRAM</div><div class="tg"><div class="bubble" style="font-size:.8rem"><b style="color:var(--royal)">BTicket Bot</b> · 2 min<br><br>🎟 <b>Ticket found!</b><br><span style="color:var(--blue);font-weight:700">View ticket →</span></div></div></div>
<div class="notif-card"><div class="cap">✉ EMAIL</div><div class="mail"><div class="mrow"><div class="av">B</div><div><div class="msub">BTicket found a match!</div><div class="mbody">Tashkent → Dubai • 27 Sep 2026</div></div></div></div></div>
</div>
</div>
<script>
document.querySelectorAll("[data-ntf]").forEach(t => t.addEventListener("click", () => {
  document.querySelectorAll("[data-ntf]").forEach(x => x.classList.remove("active"));
  t.classList.add("active");
  const cat = t.dataset.ntf;
  document.querySelectorAll("#ntfList .ntf-row").forEach(r => {
    r.style.display = (cat === "all" || r.dataset.cat === cat) ? "" : "none";
  });
}));
</script>'''
write("notifications/index.html", "Notifications — BTicket", NT, guard=True)
